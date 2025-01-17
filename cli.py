import sys
import os
from quantum_encrypt import encrypt_message

def main():
    if len(sys.argv) < 2:
        print("Usage: python cli.py <text_to_encrypt> [output_file]")
        sys.exit(1)
    
    text = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else "encrypted_output.txt"
    
    try:
        encrypted_text = encrypt_message(text)
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(encrypted_text)
        print(f"Text encrypted successfully. Written to: {output_file}")
    except Exception as e:
        print(f"Error during encryption: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
