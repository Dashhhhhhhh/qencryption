import os
import json
import time
import hashlib
import cirq
import random
from pathlib import Path
from typing import Dict, Optional, Tuple
import base64

class KeyManager:
    def __init__(self, storage_dir: str = "keys"):
        self.storage_dir = Path(storage_dir)
        self.storage_dir.mkdir(exist_ok=True)
        self.key_file = self.storage_dir / "keystore.json"
        self._load_keys()
        self.simulator = cirq.Simulator()

    def _load_keys(self) -> None:
        """Load keys from storage"""
        if self.key_file.exists():
            try:
                with open(self.key_file, 'r') as f:
                    self.keys = json.load(f)
            except json.JSONDecodeError:
                self.keys = {}
        else:
            self.keys = {}

    def _save_keys(self) -> None:
        """Save keys to storage"""
        with open(self.key_file, 'w') as f:
            json.dump(self.keys, f, indent=2)

    def _hash_key(self, key: str) -> str:
        """Create SHA-256 hash of the key"""
        return hashlib.sha256(key.encode()).hexdigest()

    def _verify_key_hash(self, key: str, stored_hash: str) -> bool:
        """Verify if key matches stored hash"""
        return self._hash_key(key) == stored_hash

    def _quantum_encrypt(self, data: str) -> Tuple[str, str]:
        """Encrypt data using quantum circuit"""
        # Convert data to binary
        binary_data = ''.join(format(ord(c), '08b') for c in data)
        num_bits = len(binary_data)
        
        # Create quantum circuit
        qubits = [cirq.NamedQubit(f'q{i}') for i in range(num_bits)]
        circuit = cirq.Circuit()
        
        # Generate random bases for BB84
        bases = [random.choice(['X', 'Z']) for _ in range(num_bits)]
        key_bits = [random.randint(0, 1) for _ in range(num_bits)]
        
        # Prepare qubits
        for i in range(num_bits):
            if key_bits[i]:
                circuit.append(cirq.X(qubits[i]))
            if bases[i] == 'X':
                circuit.append(cirq.H(qubits[i]))
            
        # Measure in computational basis
        circuit.append([cirq.measure(q, key=str(i)) for i, q in enumerate(qubits)])
        
        # Get results
        results = self.simulator.run(circuit)
        measured_bits = []
        for i in range(num_bits):
            # Extract integer value directly
            bit = int(results.measurements[str(i)][0])
            measured_bits.append(str(bit))
        
        # XOR with original data
        encrypted_bits = ''.join(
            str(int(binary_data[i]) ^ int(measured_bits[i]))
            for i in range(num_bits)
        )
        
        # Store as string directly
        bases_key = ''.join('1' if b == 'X' else '0' for b in bases)
        
        return encrypted_bits, bases_key

    def _quantum_decrypt(self, encrypted_data: str, bases_key: str) -> str:
        """Decrypt data using quantum circuit"""
        try:
            # Convert bases back to X/Z
            bases = ['X' if b == '1' else 'Z' for b in bases_key]
            num_bits = len(encrypted_data)
            
            # Create quantum circuit for decryption
            qubits = [cirq.NamedQubit(f'q{i}') for i in range(num_bits)]
            circuit = cirq.Circuit()
            
            # Prepare qubits based on encrypted bits
            for i in range(num_bits):
                # Convert string bit to integer
                if int(encrypted_data[i]) == 1:
                    circuit.append(cirq.X(qubits[i]))
                if bases[i] == 'X':
                    circuit.append(cirq.H(qubits[i]))
                    
            # Measure
            circuit.append([cirq.measure(q, key=str(i)) for i, q in enumerate(qubits)])
            
            # Get results
            results = self.simulator.run(circuit)
            decrypted_bits = []
            for i in range(num_bits):
                # Extract integer value directly
                bit = int(results.measurements[str(i)][0])
                decrypted_bits.append(str(bit))
            
            # Convert bits back to text
            decrypted_text = ''
            for i in range(0, len(decrypted_bits), 8):
                byte_bits = ''.join(decrypted_bits[i:i+8])
                decrypted_text += chr(int(byte_bits, 2))
            
            return decrypted_text
            
        except Exception as e:
            print(f"Quantum decryption failed: {str(e)}")
            return None

    def store_key(self, key: str, identifier: str, metadata: Dict = None) -> None:
        """Store a key with quantum encryption"""
        if metadata is None:
            metadata = {}
        
        # Encrypt the key quantum mechanically
        encrypted_key, bases_key = self._quantum_encrypt(key)
        key_hash = self._hash_key(key)
        
        self.keys[identifier] = {
            "key": encrypted_key,
            "bases": bases_key,
            "hash": key_hash,
            "created": time.time(),
            "metadata": metadata,
            "quantum_encrypted": True
        }
        self._save_keys()

    def get_key(self, identifier: str) -> Optional[str]:
        """Retrieve and decrypt a quantum-encrypted key"""
        if identifier in self.keys:
            try:
                key_data = self.keys[identifier]
                if not key_data.get("quantum_encrypted", False):
                    return super().get_key(identifier)
                    
                encrypted_key = key_data["key"]
                bases_key = key_data["bases"]
                stored_hash = key_data["hash"]
                
                # Quantum decrypt
                decrypted_key = self._quantum_decrypt(encrypted_key, bases_key)
                if decrypted_key and self._verify_key_hash(decrypted_key, stored_hash):
                    return decrypted_key
                else:
                    print(f"Warning: Key hash verification failed for key_id: {identifier}")
            except Exception as e:
                print(f"Error retrieving key: {str(e)}")
        else:
            print(f"Error: Key with identifier '{identifier}' not found.")
        return None

    def verify_all_keys(self) -> Dict[str, bool]:
        """Verify all stored keys against their hashes"""
        verification_results = {}
        for key_id in self.keys:
            try:
                key_data = self.keys[key_id]
                if key_data.get("quantum_encrypted", False):
                    stored_key = self._quantum_decrypt(key_data["key"], key_data["bases"])
                else:
                    stored_key = base64.b64decode(key_data["key"].encode()).decode()
                stored_hash = key_data["hash"]
                verification_results[key_id] = self._verify_key_hash(stored_key, stored_hash)
            except:
                verification_results[key_id] = False
        return verification_results

    def delete_key(self, identifier: str) -> bool:
        """Securely delete a key"""
        if identifier in self.keys:
            # Overwrite key data before deletion
            self.keys[identifier]["key"] = "0" * len(self.keys[identifier]["key"])
            self._save_keys()
            del self.keys[identifier]
            self._save_keys()
            return True
        return False

    def delete_all_keys(self) -> bool:
        """Securely delete all keys"""
        try:
            for key_id in list(self.keys.keys()):
                self.keys[key_id]["key"] = "0" * len(self.keys[key_id]["key"])
            self._save_keys()
            self.keys.clear()
            self._save_keys()
            return True
        except Exception as e:
            print(f"Error deleting all keys: {str(e)}")
            return False

    def rotate_key(self, identifier: str, new_key: str) -> bool:
        """Rotate an existing key with hash update"""
        if identifier in self.keys:
            metadata = self.keys[identifier].get("metadata", {})
            metadata["previous_rotation"] = time.time()
            metadata["previous_hash"] = self.keys[identifier]["hash"]
            self.store_key(new_key, identifier, metadata)
            return True
        return False

    def list_keys(self) -> Dict:
        """List all stored key identifiers with creation times and verification status"""
        keys_info = {}
        for k, v in self.keys.items():
            try:
                if v.get("quantum_encrypted", False):
                    stored_key = self._quantum_decrypt(v["key"], v["bases"])
                else:
                    stored_key = base64.b64decode(v["key"].encode()).decode()
                is_valid = self._verify_key_hash(stored_key, v["hash"])
            except:
                is_valid = False
            
            keys_info[k] = {
                "created": v["created"],
                "metadata": v.get("metadata", {}),
                "verified": is_valid
            }
        return keys_info

    def validate_key(self, key: str) -> bool:
        """Validate key format (must be binary string)"""
        return all(bit in '01' for bit in key)

    def generate_key_id(self, prefix: str = "key") -> str:
        """Generate a unique key identifier"""
        timestamp = int(time.time())
        return f"{prefix}_{timestamp}"

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Ensure proper cleanup on exit"""
        self._save_keys()
