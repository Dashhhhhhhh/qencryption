from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt


def generate_random_numbers(num_qubits, shots):
    """
    Generate random numbers using a quantum circuit.
    
    Parameters:
    - num_qubits (int): Number of qubits used for randomness.
    - shots (int): Number of measurements (random numbers generated).
    
    Returns:
    - dict: A dictionary with bitstrings as keys and their frequencies as values.
    """
    # Create a quantum circuit with the given number of qubits
    circuit = QuantumCircuit(num_qubits, num_qubits)

    # Apply a Hadamard gate to each qubit to create superposition
    for qubit in range(num_qubits):
        circuit.h(qubit)

    # Measure each qubit
    circuit.measure(range(num_qubits), range(num_qubits))

    # Simulate the circuit
    simulator = Aer.get_backend('qasm_simulator')
    job = execute(circuit, simulator, shots=shots)
    result = job.result()

    # Get measurement results
    counts = result.get_counts()
    return counts


def plot_results(counts):
    """
    Plot the results of the QRNG test as a histogram.
    
    Parameters:
    - counts (dict): The measurement results from the quantum circuit.
    """
    print("Generated Random Numbers:")
    for bitstring, frequency in counts.items():
        print(f"{bitstring}: {frequency}")
    
    # Plot the histogram
    plot_histogram(counts, title="Quantum Random Number Generator (QRNG) Results")
    plt.show()


if __name__ == "__main__":
    # Define parameters
    NUM_QUBITS = 4  # Number of qubits to use (bitstring length)
    SHOTS = 1024    # Number of random numbers to generate

    # Generate random numbers
    random_counts = generate_random_numbers(NUM_QUBITS, SHOTS)

    # Plot the results
    plot_results(random_counts)
