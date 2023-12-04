from encryption_module import generate_key, write_to_file, read_from_file, encrypt_message, decrypt_message
import os
import tkinter as tk
from tkinter import simpledialog

def encrypt_and_write(message, key, file_path):
    encrypted_message = encrypt_message(message, key)
    write_to_file(file_path, encrypted_message)
    print(f'Message encrypted and written to {file_path}. Key: {key.decode()}')

def read_and_decrypt(file_path, key):
    if not os.path.isfile(file_path):
        print(f'Error: File not found: {file_path}')
        return

    encrypted_message = read_from_file(file_path)
    decrypted_message = decrypt_message(encrypted_message, key)
    print(f'Decrypted message: {decrypted_message}')

def main():
    # Create a simple Tkinter console-based GUI
    root = tk.Tk()
    root.withdraw()  # Hide the main Tkinter window

    # Ask the user whether to encrypt or decrypt
    choice = simpledialog.askstring("Choose Action", "Encrypt or Decrypt?").lower()

    if choice == 'encrypt':
        message = simpledialog.askstring("Enter Message", "Enter the message to encrypt:")
        key = simpledialog.askstring("Enter Key", "Enter the key (press Cancel to generate a new key):")
        key = key.encode() if key else generate_key()
        file_path = simpledialog.askstring("Enter File Path", "Enter the file path to save the encrypted message:")
        encrypt_and_write(message, key, file_path)

    elif choice == 'decrypt':
        file_path = simpledialog.askstring("Enter File Path", "Enter the file path to read the encrypted message:")
        key = simpledialog.askstring("Enter Key", "Enter the key for decryption:")
        read_and_decrypt(file_path, key)

    else:
        print("Invalid choice. Please choose either 'Encrypt' or 'Decrypt'.")

if __name__ == "__main__":
    main()