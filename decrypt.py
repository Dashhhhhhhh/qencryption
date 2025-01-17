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

    # Simulate measurements
    sim = cirq.Simulator()
    results = sim.run(circuit)

    return alice_bits, alice_bases, qubits, circuit

def decrypt_text_with_bb84(input_file):
    # Read encrypted text using UTF-8 encoding
    with open(input_file, 'r', encoding='utf-8') as f:
        encrypted_data = f.read().strip()

    # Split into text and key parts
    try:
        encrypted_text, key_bits = encrypted_data.split(':', 1)
    except ValueError:
        raise ValueError("Invalid encrypted text format - missing separator")

    # Convert encrypted text to binary
    encrypted_binary = ''.join(format(ord(char), '08b') for char in encrypted_text)

    # XOR encrypted binary with the key
    decrypted_binary = ''.join(
        str(int(encrypted_binary[i]) ^ int(key_bits[i])) 
        for i in range(len(encrypted_binary))
    )

    # Convert binary to text
    decrypted_text = ''.join(
        chr(int(decrypted_binary[i:i+8], 2)) 
        for i in range(0, len(decrypted_binary), 8)
    )
    return decrypted_text

def main():
    # Load IonQ API key from environment variables
    api_key = os.getenv("IONQ_API_KEY")
    if not api_key:
        raise ValueError("IonQ API key not found in environment variables")

    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}

    # Input and output files
    input_file = "encrypted_output.txt"

    try:
        # Decrypt the text directly from file
        decrypted_text = decrypt_text_with_bb84(input_file)
        print(f"Text decrypted successfully. Decrypted text: {decrypted_text}")
        
        # Save to decrypted file
        with open("decrypted_output.txt", 'w', encoding='utf-8') as f:
            f.write(decrypted_text)
            
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
