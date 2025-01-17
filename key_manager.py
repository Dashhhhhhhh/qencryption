import os
import json
import time
import hashlib
from pathlib import Path
from typing import Dict, Optional, Tuple
import base64

class KeyManager:
    def __init__(self, storage_dir: str = "keys"):
        self.storage_dir = Path(storage_dir)
        self.storage_dir.mkdir(exist_ok=True)
        self.key_file = self.storage_dir / "keystore.json"
        self._load_keys()

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

    def store_key(self, key: str, identifier: str, metadata: Dict = None) -> None:
        """Store a key with its hash and optional metadata"""
        if metadata is None:
            metadata = {}
        
        key_hash = self._hash_key(key)
        self.keys[identifier] = {
            "key": base64.b64encode(key.encode()).decode(),
            "hash": key_hash,
            "created": time.time(),
            "metadata": metadata
        }
        self._save_keys()

    def get_key(self, identifier: str) -> Optional[str]:
        """Retrieve a key and verify its hash"""
        if identifier in self.keys:
            try:
                stored_key = base64.b64decode(self.keys[identifier]["key"].encode()).decode()
                stored_hash = self.keys[identifier]["hash"]
                
                if self._verify_key_hash(stored_key, stored_hash):
                    return stored_key
                else:
                    print("Warning: Key hash verification failed!")
                    return None
            except:
                return None
        return None

    def verify_all_keys(self) -> Dict[str, bool]:
        """Verify all stored keys against their hashes"""
        verification_results = {}
        for key_id in self.keys:
            try:
                stored_key = base64.b64decode(self.keys[key_id]["key"].encode()).decode()
                stored_hash = self.keys[key_id]["hash"]
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
