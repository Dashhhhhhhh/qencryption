import cirq
import random
import os
from dotenv import load_dotenv
from key_manager import KeyManager
import cirq_ionq

load_dotenv()

def is_valid_api_key(api_key: str) -> bool:
    """Check if the API key is valid format"""
    if not api_key or not api_key.strip():
        return False
    # Check for minimum length and basic format
    key = api_key.strip()
    return len(key) >= 20 and "." not in key and " " not in key

def generate_bb84_key(num_bits):
    """Generate quantum key with size constraints"""
    if isinstance(num_bits, tuple):  # Fix for tuple input
        num_bits = num_bits[0]
    
    api_key = os.getenv("IONQ_API_KEY")
    use_simulator = os.getenv("USE_IONQ_SIMULATOR", "true").lower() == "true"
    valid_key = is_valid_api_key(api_key)
    
    # IONQ has limits on circuit size, use chunks if needed
    MAX_IONQ_BITS = 10  # Adjust this value based on IONQ limits
    
    if valid_key and num_bits > MAX_IONQ_BITS:
        print(f"Warning: Number of bits ({num_bits}) exceeds IONQ limit. Using local simulator.")
        valid_key = False
    
    alice_bases = [random.choice(['Z', 'X']) for _ in range(num_bits)]
    alice_bits = [random.randint(0, 1) for _ in range(num_bits)]
    qubits = [cirq.LineQubit(i) for i in range(num_bits)]
    circuit = cirq.Circuit()

    for i in range(num_bits):
        if alice_bits[i] == 1:
            circuit.append(cirq.X(qubits[i]))
        if alice_bases[i] == 'X':
            circuit.append(cirq.H(qubits[i]))
        circuit.append(cirq.measure(qubits[i], key=f'm{i}'))

    if not valid_key:
        print("Using local simulator for quantum operations.")
        sim = cirq.Simulator()
        results = sim.run(circuit)
    else:
        try:
            print(f"Using IONQ {'simulator' if use_simulator else 'QPU'}...")
            service = cirq_ionq.Service(api_key=api_key)
            target = "simulator" if use_simulator else "qpu"
            job = service.create_job(circuit=circuit, repetitions=1, target=target)
            results = job.results()
        except Exception as e:
            print(f"IONQ service failed ({str(e)}). Falling back to local simulator.")
            sim = cirq.Simulator()
            results = sim.run(circuit)

    return alice_bits, alice_bases, qubits, circuit

def encrypt_message(text, key_multiplier=4):
    """Main encryption function that returns the encrypted text and the key"""
    try:
        # Calculate required bits based on text length and multiplier
        required_bits = len(text) * 8  # 8 bits per character
        num_bits = required_bits * key_multiplier  # Generate extra bits for safety
        
        print(f"Generating quantum key for {num_bits} bits...")

        # Generate initial key
        alice_bits, alice_bases, qubits, _ = generate_bb84_key(num_bits)
        
        # Simulate Bob's measurements
        bob_bases = [random.choice(['Z', 'X']) for _ in range(num_bits)]
        bob_circuit = cirq.Circuit()
        
        for i in range(num_bits):
            if bob_bases[i] == 'X':
                bob_circuit.append(cirq.H(qubits[i]))
            bob_circuit.append(cirq.measure(qubits[i], key=f'm{i}'))

        sim = cirq.Simulator()
        bob_results = sim.run(bob_circuit, repetitions=1)
        
        # Key reconciliation
        key = [alice_bits[i] for i in range(num_bits) if alice_bases[i] == bob_bases[i]]
        print(f"Debug: Total bits generated: {num_bits}")
        print(f"Debug: Bits after reconciliation: {len(key)}")
        
        # Convert text to binary
        binary_text = ''.join(format(ord(char), '08b') for char in text)
        required_length = len(binary_text)
        print(f"Debug: Required bits for text: {required_length}")
        
        # If key is too short, generate additional key material
        while len(key) < required_length:
            print(f"Debug: Key too short ({len(key)} < {required_length}), generating more bits...")
            additional_bits = required_length - len(key)
            extra_bits = additional_bits * key_multiplier  # Use same multiplier for consistency
            
            # Generate additional key material
            more_alice_bits, more_alice_bases, more_qubits, _ = generate_bb84_key(extra_bits)
            more_bob_bases = [random.choice(['Z', 'X']) for _ in range(extra_bits)]
            
            # Reconcile additional key bits
            additional_key = [more_alice_bits[i] for i in range(extra_bits) 
                             if more_alice_bases[i] == more_bob_bases[i]]
            key.extend(additional_key)
        
        # Trim key to exact length needed
        key = key[:required_length]
        print(f"Debug: Final key length: {len(key)}")
        
        # Perform encryption
        binary_key = ''.join(str(bit) for bit in key)
        encrypted_binary = ''.join(str(int(binary_text[i]) ^ int(binary_key[i])) 
                                  for i in range(len(binary_text)))
        
        encrypted_text = ''.join(chr(int(encrypted_binary[i:i+8], 2)) 
                               for i in range(0, len(encrypted_binary), 8))
        
        return encrypted_text, binary_key

    except Exception as e:
        print(f"Encryption failed: {str(e)}")
        return None, None

def decrypt_message(encrypted_text, key):
    """Decrypt a message using the same XOR principle as encryption."""
    # Remove any whitespace/newlines
    encrypted_text = encrypted_text.strip()
    
    try:
        # Convert to bits
        text_bits = ''.join(format(ord(c), '08b') for c in encrypted_text)
        
        if len(key) < len(text_bits):
            raise ValueError("Key is too short for decryption")
        
        # Decrypt using XOR
        decrypted_bits = ''.join(
            str(int(text_bits[i]) ^ int(key[i])) 
            for i in range(len(text_bits))
        )
        
        # Convert bits back to text
        decrypted_bytes = bytes(
            int(decrypted_bits[i:i+8], 2) 
            for i in range(0, len(decrypted_bits), 8)
        )
        return decrypted_bytes.decode('utf-8')
    
    except (ValueError, UnicodeDecodeError) as e:
        raise ValueError(f"Decryption failed: {str(e)}")  # Fixed missing quote
