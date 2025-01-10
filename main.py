from qiskit import QuantumCircuit, Aer, execute

# Create a quantum circuit
circuit = QuantumCircuit(1, 1)
circuit.h(0)  # Apply Hadamard gate
circuit.measure(0, 0)

# Simulate the circuit
simulator = Aer.get_backend('qasm_simulator')
job = execute(circuit, simulator, shots=1000)
result = job.result()
counts = result.get_counts()

print("Simulation Result:", counts)
