from qiskit import QuantumCircuit, Aer, execute, IBMQ
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt


def create_circuit():
    """
    Create a simple quantum circuit with 2 qubits and 2 classical bits.
    The circuit puts the first qubit in superposition and entangles it with the second qubit.
    """
    # Create a quantum circuit with 2 qubits and 2 classical bits
    circuit = QuantumCircuit(2, 2)

    # Add quantum gates
    circuit.h(0)         # Apply a Hadamard gate to qubit 0 (creates superposition)
    circuit.cx(0, 1)     # Apply a CNOT gate with qubit 0 as control and qubit 1 as target

    # Measure the qubits into the classical bits
    circuit.measure([0, 1], [0, 1])

    return circuit


def simulate_circuit(circuit):
    """
    Simulate the quantum circuit using the Qiskit Aer simulator.
    """
    simulator = Aer.get_backend('qasm_simulator')  # QASM simulator for quantum circuits
    result = execute(circuit, simulator, shots=1000).result()
    counts = result.get_counts()
    return counts


def plot_results(simulated_counts, hardware_counts=None):
    """
    Plot the results from simulation and hardware execution (if available).
    """
    # Plot simulated results
    print("Simulated Results:", simulated_counts)
    plot_hi
