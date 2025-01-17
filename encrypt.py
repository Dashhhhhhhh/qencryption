import sys
import cirq
import random
import requests
import os
import json
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# BB84 Implementation
def generate_bb84_key(num_bits):
    use_quantum = os.getenv("USE_QUANTUM_HARDWARE", "false").lower() == "true"
    
    # Generate random bases and bits
    alice_bases = [random.choice(['Z', 'X']) for _ in range(num_bits)]
    alice_bits = [random.randint(0, 1) for _ in range(num_bits)]

    # Simulate Alice's qubits
    qubits = [cirq.NamedQubit(f'q{i}') for i in range(num_bits)]
    circuit = cirq.Circuit()

    for i in range(num_bits):
        if alice_bits[i] == 1:
            circuit.append(cirq.X(qubits[i]))
        if alice_bases[i] == 'X':
            circuit.append(cirq.H(qubits[i]))

    # Add measurement operations
    for i in range(num_bits):
        circuit.append(cirq.measure(qubits[i], key=f'm{i}'))

    if use_quantum:
        # Use IonQ quantum hardware
        api_key = os.getenv("IONQ_API_KEY")
        service = cirq.IonQService(api_key=api_key)
        job = service.run(program=circuit, repetitions=1)
        results = job.results()
    else:
        # Use simulator
        sim = cirq.Simulator()
        results = sim.run(circuit)

    return alice_bits, alice_bases, qubits, circuit

def key_to_bits(key):
    """Convert a list of integers (key) into a binary string."""
    return ''.join(str(bit) for bit in key)

def encrypt_text_with_bb84(text, output_file, key):
    # Convert text to binary
    binary_text = ''.join(format(ord(char), '08b') for char in text)
    
    # Convert key to binary string
    binary_key = key_to_bits(key)

    # Ensure the key is as long as the binary text
    if len(binary_key) < len(binary_text):
        raise ValueError("Key length is shorter than the text length.")

    # XOR binary text with the key
    encrypted_binary = ''.join(str(int(binary_text[i]) ^ int(binary_key[i])) 
                              for i in range(len(binary_text)))

    # Convert binary to text
    encrypted_text = ''.join(chr(int(encrypted_binary[i:i+8], 2)) 
                            for i in range(0, len(encrypted_binary), 8))

    # Write encrypted text using UTF-8 encoding
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(encrypted_text)

def generate_bits_from_key(text, multiplier=4):
    """Generate required number of bits based on input text length."""
    required_bits = len(text) * 8  # 8 bits per character
    total_bits = required_bits * multiplier  # Add extra bits for safety margin
    return total_bits

def main():
    # Load environment variables
    api_key = os.getenv("IONQ_API_KEY")
    use_quantum = os.getenv("USE_QUANTUM_HARDWARE", "false").lower() == "true"
    
    if use_quantum and not api_key:
        raise ValueError("IonQ API key not found in environment variables")

    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}

    # Input and output files
    output_file = "encrypted_output.txt"

    # Get text input from user
    text = input("Enter the text to encrypt: ").strip()
    if not text:
        raise ValueError("Text input cannot be empty")

    # Calculate required number of bits based on text length
    num_bits = generate_bits_from_key(text)

    # Generate key using BB84
    alice_bits, alice_bases, qubits, alice_circuit = generate_bb84_key(num_bits)

    # Simulate Alice's measurements
    sim = cirq.Simulator()
    alice_results = sim.run(alice_circuit)

    # Simulate Bob's measurements with random bases
    bob_bases = [random.choice(['Z', 'X']) for _ in range(num_bits)]
    bob_circuit = cirq.Circuit()

    for i in range(num_bits):
        if bob_bases[i] == 'X':
            bob_circuit.append(cirq.H(qubits[i]))
        bob_circuit.append(cirq.measure(qubits[i], key=f'm{i}'))

    bob_results = sim.run(bob_circuit, repetitions=1)
    bob_measurements = [int(bob_results.measurements[f'm{i}'].item()) for i in range(num_bits)]

    # Key reconciliation
    key = [alice_bits[i] for i in range(num_bits) if alice_bases[i] == bob_bases[i]]

    # Ensure the key is as long as the binary text
    binary_text = ''.join(format(ord(char), '08b') for char in text)
    if len(key) < len(binary_text):
        raise ValueError("Key length is shorter than the text length.")

    # Encrypt the text
    encrypt_text_with_bb84(text, output_file, key)

    print(f"Text encrypted successfully. Encrypted text written to: {output_file}")

if __name__ == "__main__":
    main()
