import sys
import os

# Add the local ./lib directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'lib'))

import cirq


def quantum_random_number():
    """
    Generate a random number using a quantum circuit.
    """
    try:
        # Create a single qubit
        qubit = cirq.LineQubit(0)

        # Create a quantum circuit
        circuit = cirq.Circuit()

        # Apply a Hadamard gate to create a superposition state
        circuit.append(cirq.H(qubit))

        # Measure the qubit
        circuit.append(cirq.measure(qubit, key='result'))

        # Print the quantum circuit
        print("Quantum Circuit:")
        print(circuit)

        # Simulate the circuit
        simulator = cirq.Simulator()
        result = simulator.run(circuit, repetitions=1)

        # Get the measurement result
        random_bit = result.measurements['result'][0][0]
        print(f"Random Bit: {random_bit}")

        return random_bit

    except Exception as e:
        print(f"An error occurred while generating a quantum random number: {e}")
        return None


if __name__ == "__main__":
    print("Quantum Random Number Generator")
    random_number = quantum_random_number()
    print(f"Generated Random Number: {random_number}")
