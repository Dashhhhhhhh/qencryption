import sys
sys.path.insert(0, './lib')  # Add the local library folder to the Python path

import cirq
import random
import requests
import os
import json

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

    # Simulate measurements
    sim = cirq.Simulator()
    results = sim.run(circuit)

    return alice_bits, alice_bases, qubits, circuit

def encrypt_text_with_bb84(text, output_file, key):
    # Convert text to binary
    binary_text = ''.join(format(ord(char), '08b') for char in text)

    # Ensure the key is as long as the binary text
    if len(key) < len(binary_text):
        raise ValueError("Key length is shorter than the text length.")

    # XOR binary text with the key
    encrypted_binary = ''.join(str(int(binary_text[i]) ^ key[i]) for i in range(len(binary_text)))

    # Convert binary to text
    encrypted_text = ''.join(chr(int(encrypted_binary[i:i+8], 2)) for i in range(0, len(encrypted_binary), 8))

    # Write encrypted text using UTF-8 encoding
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(encrypted_text)

def main():
    # Load IonQ API key from config.json
    with open('config.json', 'r') as config_file:
        config = json.load(config_file)
        api_key = config.get("IONQ_API_KEY")
        if not api_key:
            raise ValueError("IonQ API key not found in config.json")

    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}

    # Input and output files
    output_file = "encrypted_output.txt"

    # Get text input from user
    text = input("Enter the text to encrypt: ")

    # Generate key using BB84
    num_bits = 128  # Example key length
    alice_bits, alice_bases, qubits, circuit = generate_bb84_key(num_bits)

    # Simulate Bob's measurements with random bases
    bob_bases = [random.choice(['Z', 'X']) for _ in range(num_bits)]
    bob_measurements = []

    for i in range(num_bits):
        if bob_bases[i] == 'X':
            circuit.append(cirq.H(qubits[i]))
        circuit.append(cirq.measure(qubits[i], key=f'm{i}'))

    # Send to IonQ for execution (optional, local simulation used here)
    # Note: Replace with IonQ API call if necessary
    sim = cirq.Simulator()
    results = sim.run(circuit, repetitions=1)

    for i in range(num_bits):
        bob_measurements.append(int(results.measurements[f'm{i}'].item()))

    # Key reconciliation
    key = [alice_bits[i] for i in range(num_bits) if alice_bases[i] == bob_bases[i]]

    # Encrypt the text
    encrypt_text_with_bb84(text, output_file, key)

    print(f"Text encrypted successfully. Encrypted text written to: {output_file}")

if __name__ == "__main__":
    main()
