import os
from quantum_encrypt import encrypt_message, decrypt_message

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def validate_bits(bits):
    return all(bit in '01' for bit in bits)

def validate_key(key, text_length):
    return len(key) >= text_length and all(c in '01' for c in key)

def interactive_console():
    DEFAULT_ENCRYPTED_FILE = "encrypted_output.txt"
    DEFAULT_DECRYPTED_FILE = "decrypted_output.txt"

    while True:
        clear_screen()
        print("Quantum BB84 Encryption Console")
        print("==============================")
        print("1. Encrypt a message")
        print("2. Encrypt with custom bits and key")
        print("3. Decrypt a message")
        print("4. Exit")
        
        choice = input("\nSelect an option (1-4): ").strip()
        
        if choice == '4':
            print("Goodbye!")
            break
        elif choice == '3':
            clear_screen()
            print("BB84 Decryption")
            print("==============")
            
            # Get input file with default
            input_file = input(f"\nEnter input filename (default: {DEFAULT_ENCRYPTED_FILE}, or 'back' to return): ").strip()
            if input_file.lower() == 'back':
                continue
            if not input_file:
                input_file = DEFAULT_ENCRYPTED_FILE
                
            try:
                # Read encrypted text
                with open(input_file, 'r', encoding='utf-8') as f:
                    encrypted_text = f.read().strip()
                
                if not encrypted_text:
                    raise ValueError("File is empty")
                
                # Decrypt
                decrypted_text = decrypt_message(encrypted_text)
                
                # Save decrypted text to file
                with open(DEFAULT_DECRYPTED_FILE, 'w', encoding='utf-8') as f:
                    f.write(decrypted_text)
                
                print("\nDecrypted message:")
                print("-----------------")
                print(decrypted_text)
                print(f"\nDecrypted text also saved to: {DEFAULT_DECRYPTED_FILE}")
                
            except FileNotFoundError:
                print(f"\nError: File '{input_file}' not found")
            except ValueError as e:
                print(f"\nError: {str(e)}")
            except Exception as e:
                print(f"\nUnexpected error: {str(e)}")
            
            input("\nPress Enter to continue...")
                
        elif choice == '1' or choice == '2':
            clear_screen()
            print("BB84 Encryption")
            print("==============")
            
            # Get input text
            text = input("\nEnter text to encrypt (or 'back' to return): ").strip()
            if text.lower() == 'back':
                continue

            custom_bits = None
            custom_key = None
            if choice == '2':
                while True:
                    bits = input("\nEnter your bits (0s and 1s only): ").strip()
                    if validate_bits(bits):
                        custom_bits = bits
                        break
                    print("Invalid input! Please use only 0s and 1s.")
                
                while True:
                    key = input("\nEnter your key (0s and 1s, must be at least as long as the text): ").strip()
                    if validate_key(key, len(text)):
                        custom_key = key
                        break
                    print("Invalid input! Key must be 0s and 1s and at least as long as the text.")
                
            # Get output file name with default
            output_file = input(f"Enter output filename (default: {DEFAULT_ENCRYPTED_FILE}): ").strip()
            if not output_file:
                output_file = DEFAULT_ENCRYPTED_FILE
                
            try:
                # Calculate required bits based on text length
                text_length = len(text) * 8  # 8 bits per character
                
                # Perform encryption with dynamic bit size
                print("\nEncrypting...")
                encrypted_text = encrypt_message(text, key_multiplier=4)  # 4x multiplier for safety
                
                # Save to file
                with open(output_file, 'w', encoding='utf-8') as f:
                    f.write(encrypted_text)
                    
                print(f"\nSuccess! Encrypted text saved to: {output_file}")
                input("\nPress Enter to continue...")
                
            except Exception as e:
                print(f"\nError: {str(e)}")
                input("\nPress Enter to continue...")
        else:
            print("\nInvalid option!")
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    interactive_console()
