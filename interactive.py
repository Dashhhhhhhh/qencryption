import os
from quantum_encrypt import encrypt_message, decrypt_message, generate_bb84_key
from key_manager import KeyManager
import time
import cirq
import cirq_ionq # New import
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def validate_bits(bits):
    return all(bit in '01' for bit in bits)

def validate_key(key, text_length):
    return len(key) >= text_length and all(c in '01' for c in key)

def list_stored_keys():
    """Display all stored keys and their metadata"""
    with KeyManager() as km:
        keys = km.list_keys()
        if not keys:
            print("\nNo keys stored.")
            return
        
        print("\nStored Keys:")
        print("-" * 50)
        for key_id, data in keys.items():
            created = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(data['metadata'].get('created', time.time())))
            print(f"Key ID: {key_id}")
            print(f"Created: {created}")
            print(f"Metadata: {data['metadata']}")
            print("-" * 50)

def delete_stored_key():
    """Delete a stored key"""
    key_id = input("\nEnter key ID to delete (or 'back' to return): ").strip()
    if key_id.lower() == 'back':
        return
        
    with KeyManager() as km:
        if km.delete_key(key_id):
            print(f"\nKey {key_id} deleted successfully.")
        else:
            print(f"\nKey {key_id} not found.")

def delete_all_stored_keys():
    """Delete all stored keys"""
    confirmation = input("\nAre you sure you want to delete all keys? This action cannot be undone (yes/no): ").strip().lower()
    if confirmation == 'yes':
        with KeyManager() as km:
            if km.delete_all_keys():
                print("\nAll keys deleted successfully.")
            else:
                print("\nFailed to delete all keys.")
    else:
        print("\nDeletion of all keys canceled.")

def is_valid_api_key(api_key: str) -> bool:
    """Check if the API key is valid format"""
    if not api_key or not api_key.strip():
        return False
    key = api_key.strip()
    return len(key) >= 20 and "." not in key and " " not in key

def test_qpu():
    """Test the QPU simulator or hardware"""
    print("\nTesting QPU...")
    api_key = os.getenv("IONQ_API_KEY")
    use_simulator = os.getenv("USE_IONQ_SIMULATOR", "true").lower() == "true"
    
    print("Backend configuration:")
    print("--------------------")
    valid_key = is_valid_api_key(api_key)
    print(f"IONQ API Key: {'Valid' if valid_key else 'Invalid or not available'}")
    print(f"API Key Status: {'✓ Valid format' if valid_key else '✗ Invalid format or missing'}")
    
    if not valid_key:
        print("\nWarning: Invalid API key format. Using local simulator instead.")
        try:
            sim = cirq.Simulator()
            qubits = [cirq.LineQubit(0)]
            circuit = cirq.Circuit(cirq.H(qubits[0]), cirq.measure(qubits[0], key='m'))
            results = sim.run(circuit)
            print("✓ Test completed successfully using local Cirq simulator")
        except Exception as e:
            print(f"✗ Local simulator test failed: {str(e)}")
    else:
        try:
            service = cirq_ionq.Service(api_key=api_key)
            qubits = [cirq.LineQubit(0)]
            circuit = cirq.Circuit(cirq.H(qubits[0]), cirq.measure(qubits[0], key='m'))
            target = "simulator" if use_simulator else "qpu"
            print(f"\nAttempting to connect to IONQ cloud ({target})...")
            job = service.create_job(circuit=circuit, repetitions=1, target=target)
            results = job.results()
            print(f"✓ Test completed successfully using IONQ {target}")
        except Exception as e:
            print(f"✗ IONQ cloud test failed: {str(e)}")
            print("\nFalling back to local simulator...")
            try:
                sim = cirq.Simulator()
                results = sim.run(circuit)
                print("✓ Test completed successfully using local Cirq simulator")
            except Exception as e:
                print(f"✗ Local simulator test failed: {str(e)}")
    
    input("\nPress Enter to continue...")

def show_api_key_status():
    """Display the current API key status and configuration"""
    print("\nAPI Key Status")
    print("=============")
    api_key = os.getenv("IONQ_API_KEY")
    use_simulator = os.getenv("USE_IONQ_SIMULATOR", "true").lower() == "true"
    
    print(f"API Key: {api_key if api_key else 'Not set'}")
    print(f"API Key Valid: {'✓ Yes' if is_valid_api_key(api_key) else '✗ No'}")
    print(f"Mode: {'IONQ Simulator' if use_simulator else 'IONQ QPU'} (when API key valid)")
    print(f"Key Length: {len(api_key.strip()) if api_key else 0} characters")
    input("\nPress Enter to continue...")

def get_file_location(default_file: str, operation: str) -> str:
    """Get file location with proper path handling"""
    while True:
        file_path = input(f"\nEnter {operation} file location (default: {default_file}, or 'back' to return): ").strip()
        if file_path.lower() == 'back':
            return None
        if not file_path:
            file_path = default_file
        
        file_path = os.path.abspath(file_path)
        directory = os.path.dirname(file_path)
        try:
            os.makedirs(directory, exist_ok=True)
            return file_path
        except Exception as e:
            print(f"Error creating directory: {str(e)}")
            continue

def store_encryption_key(key: str, text_length: int, output_file: str) -> str:
    """Store encryption key and return key ID"""
    with KeyManager() as km:
        key_id = km.generate_key_id()
        km.store_key(key, key_id, {
            "text_length": text_length,
            "output_file": output_file,
            "created": time.strftime('%Y-%m-%d %H:%M:%S')
        })
        return key_id

def decrypt_with_key_id():
    """Get decryption key using only key ID"""
    while True:
        key_id = input("\nEnter key ID (or 'back' to return): ").strip()
        if key_id.lower() == 'back':
            return None
        if not key_id:
            print("Error: Key ID is required")
            continue
            
        with KeyManager() as km:
            key = km.get_key(key_id)
            if key:
                print("Key successfully retrieved.")
                return key
            print("Failed to retrieve key. Please check the Key ID and try again.")
        
        retry = input("\nWould you like to try another Key ID? (y/n): ").strip().lower()
        if retry != 'y':
            return None

def interactive_console():
    DEFAULT_OUTPUT_DIR = "output"
    DEFAULT_ENCRYPTED_FILE = os.path.join(DEFAULT_OUTPUT_DIR, "encrypted_output.txt")
    DEFAULT_DECRYPTED_FILE = os.path.join(DEFAULT_OUTPUT_DIR, "decrypted_output.txt")
    
    os.makedirs(DEFAULT_OUTPUT_DIR, exist_ok=True)

    while True:
        clear_screen()
        api_key = os.getenv("IONQ_API_KEY")
        use_simulator = os.getenv("USE_IONQ_SIMULATOR", "true").lower() == "true"
        
        if not api_key or not api_key.strip():
            mode = "Local Simulator (No API Key)"
        else:
            mode = f"IONQ {'Simulator' if use_simulator else 'QPU'}"
        
        print(f"Quantum BB84 Encryption Console ({mode})")
        print("=" * (28 + len(mode)))
        print("1. Encrypt a message")
        print("2. Encrypt with custom bits and key")
        print("3. Decrypt a message")
        print("4. List stored keys")
        print("5. Delete a key")
        print("6. Delete all keys")
        print("7. Test QPU")
        print("8. Show API key status")
        print("9. Exit")
        
        choice = input("\nSelect an option (1-9): ").strip()
        
        if choice == '9':
            print("Goodbye!")
            break
        elif choice == '8':
            clear_screen()
            show_api_key_status()
        elif choice == '4':
            clear_screen()
            print("Stored Keys")
            print("===========")
            list_stored_keys()
            input("\nPress Enter to continue...")
        elif choice == '5':
            clear_screen()
            print("Delete Key")
            print("==========")
            key_id = input("Enter key ID to delete: ").strip()
            with KeyManager() as km:
                km.delete_key(key_id)
            input("\nKey deleted. Press Enter to continue...")
        elif choice == '6':
            clear_screen()
            print("Delete All Keys")
            print("===============")
            with KeyManager() as km:
                km.keys.clear()
                km._save_keys()
            input("\nAll keys deleted. Press Enter to continue...")
        elif choice == '1':
            clear_screen()
            print("Encrypt a Message")
            print("=================")
            
            text = input("\nEnter text to encrypt: ").strip()
            if not text:
                print("Error: Text cannot be empty")
                input("\nPress Enter to continue...")
                continue
            
            output_file = get_file_location(DEFAULT_ENCRYPTED_FILE, "output")
            if not output_file:
                continue
                
            try:
                print("\nEncrypting...")
                encrypted_text, key = encrypt_message(text, key_multiplier=4)
                
                if encrypted_text is None or key is None:
                    print("Encryption failed!")
                    input("\nPress Enter to continue...")
                    continue
                
                key_id = store_encryption_key(key, len(text), output_file)
                
                with open(output_file, 'w', encoding='utf-8') as f:
                    f.write(encrypted_text)
                
                print("\nEncryption successful!")
                print("--------------------")
                print(f"Output file: {output_file}")
                print(f"Key ID: {key_id}")
                print("\nIMPORTANT: Save this Key ID - you will need it to decrypt the file!")
                
            except Exception as e:
                print(f"\nError during encryption: {str(e)}")
            
            input("\nPress Enter to continue...")
        elif choice == '2':
            clear_screen()
            print("Encrypt with Custom Bits and Key")
            print("===============================")
            
            text = input("\nEnter text to encrypt: ").strip()
            custom_bits = input("\nEnter custom bits (0s and 1s only): ").strip()
            custom_key = input("\nEnter custom key (0s and 1s, must be at least as long as the text): ").strip()
            
            if not validate_bits(custom_bits) or not validate_key(custom_key, len(text) * 8):
                print("Invalid bits or key! Please use only 0s and 1s and ensure the key is long enough.")
                input("\nPress Enter to continue...")
                continue
            
            encrypted_text = encrypt_message(text, custom_key)
            print(f"\nEncrypted text: {encrypted_text}")
            
            with KeyManager() as km:
                key_id = km.generate_key_id()
                km.store_key(custom_key, key_id, {"text_length": len(text)})
                print(f"Key stored with ID: {key_id}")
            
            with open(DEFAULT_ENCRYPTED_FILE, 'w') as f:
                f.write(encrypted_text)
            print(f"Encrypted text saved to {DEFAULT_ENCRYPTED_FILE}")
            input("\nPress Enter to continue...")
        elif choice == '3':
            clear_screen()
            print("Decrypt a Message")
            print("=================")
            
            input_file = get_file_location(DEFAULT_ENCRYPTED_FILE, "input")
            if not input_file:
                continue
                
            output_file = get_file_location(DEFAULT_DECRYPTED_FILE, "output")
            if not output_file:
                continue
            
            key = decrypt_with_key_id()
            if not key:
                input("\nPress Enter to continue...")
                continue
            
            try:
                with open(input_file, 'r', encoding='utf-8') as f:
                    encrypted_text = f.read().strip()
                
                if not encrypted_text:
                    raise ValueError("Input file is empty")
                
                decrypted_text = decrypt_message(encrypted_text, key)
                print(f"\nDecrypted message:")
                print("-----------------")
                print(decrypted_text)
                
                with open(output_file, 'w', encoding='utf-8') as f:
                    f.write(decrypted_text)
                print(f"\nDecrypted text saved to: {output_file}")
                    
            except Exception as e:
                print(f"\nError: {str(e)}")
            
            input("\nPress Enter to continue...")
        elif choice == '7':
            clear_screen()
            test_qpu()

if __name__ == "__main__":
    interactive_console()
