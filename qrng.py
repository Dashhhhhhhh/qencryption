import cirq
import random

# Seed randomness with system entropy
random.seed()

# Create a random quantum circuit
qubit = cirq.LineQubit(0)
circuit = cirq.Circuit()

# Add random gates
if random.choice([True, False]):
    circuit.append(cirq.X(qubit))
else:
    circuit.append(cirq.H(qubit))

circuit.append(cirq.measure(qubit, key='result'))

print("Generated Circuit:")
print(circuit)
