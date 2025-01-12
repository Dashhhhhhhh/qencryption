import cirq
import cirq_ionq as ionq
import os
from dotenv import load_dotenv
import time

def main():
    # Load the environment variables from a custom file
    load_dotenv(dotenv_path='config.env')

    # Get the IonQ API key
    ionq_api_key = os.getenv('IONQ_API_KEY')
    if not ionq_api_key:
        print("Please set the 'IONQ_API_KEY' in the 'config.env' file.")
        return

    # Create IonQ service client
    service = ionq.Service(api_key=ionq_api_key)

    # Define a simple quantum circuit (Bell State)
    qubit1 = cirq.LineQubit(0)
    qubit2 = cirq.LineQubit(1)

    circuit = cirq.Circuit(
        cirq.H(qubit1),            # Apply Hadamard gate to qubit 1
        cirq.CNOT(qubit1, qubit2),  # Apply CNOT with qubit 1 as control and qubit 2 as target
        cirq.measure(qubit1, qubit2, key="result")  # Add measurement gates
    )

    print("Quantum Circuit:")
    print(circuit)

    # Submit the circuit to IonQ simulator
    print("Submitting circuit to IonQ simulator...")
    job = service.create_job(circuit=circuit, target="simulator", repetitions=100)

    # Poll job status until it's completed
    print("Waiting for job to complete...")
    while job.status() not in ["completed", "failed", "cancelled"]:
        print(f"Job status: {job.status()}. Retrying in 5 seconds...")
        time.sleep(5)

    if job.status() == "completed":
        # Get results
        results = job.results()

        # Extract measurement data using measurement_dict
        print("Results (measurement data):")
        print(results.measurement_dict())  # Call the method to get measurement outcomes
    else:
        print(f"Job failed with status: {job.status()}")

if __name__ == "__main__":
    main()
