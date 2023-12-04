# Import necessary modules
from cryptography.fernet import Fernet  # Module for encryption/decryption
import argparse  # Module for parsing command-line arguments
import tkinter as tk  # Module for GUI
from tkinter import filedialog  # Submodule for file dialog in GUI

# Function to generate an encryption key
def generate_key():
    return Fernet.generate_key()

# Function to save an encryption key to a file
def save_key(key, filename):
    with open(filename, 'wb') as key_file:
        key_file.write(key)

# Function to load an encryption key from a file
def load_key(filename):
    return open(filename, 'rb').read()

# Function to encrypt a message using a key
def encrypt_message(message, key):
    cipher_suite = Fernet(key)
    encrypted_message = cipher_suite.encrypt(message.encode())
    return encrypted_message

# Function to decrypt an encrypted message using a key
def decrypt_message(encrypted_message, key):
    cipher_suite = Fernet(key)
    decrypted_message = cipher_suite.decrypt(encrypted_message).decode()
    return decrypted_message

# Function to write content to a file
def write_to_file(filename, content):
    with open(filename, 'wb') as file:
        file.write(content)

# Function to read content from a file
def read_from_file(filename):
    with open(filename, 'rb') as file:
        return file.read()

# Function for the command-line interface
def command_line_interface():
    # Create an argument parser
    parser = argparse.ArgumentParser(description="Text Encryption/Decryption")

    # Define command-line arguments
    parser.add_argument("--encrypt", action="store_true", help="Encrypt a message")
    parser.add_argument("--decrypt", action="store_true", help="Decrypt a message")
    parser.add_argument("--message", type=str, help="Message to encrypt/decrypt")
    parser.add_argument("--keyfile", type=str, help="File containing the encryption key")
    parser.add_argument("--infile", type=str, help="Input file for decryption")
    parser.add_argument("--outfile", type=str, help="Output file for encryption")

    # Parse the command-line arguments
    args = parser.parse_args()

    # Encryption process
    if args.encrypt:
        # Generate a key
        key = generate_key()
        # Save the key to a file
        save_key(key, args.keyfile)
        # Get the message to encrypt (from command line or user input)
        message = args.message.encode() if args.message else input("Enter message to encrypt: ").encode()
        # Encrypt the message using the key
        encrypted_message = encrypt_message(message, key)
        # Write the encrypted message to a file
        write_to_file(args.outfile, encrypted_message)
        print(f"Message encrypted and saved to {args.outfile}. Key saved to {args.keyfile}")

    # Decryption process
    elif args.decrypt:
        # Load the key from a file
        key = load_key(args.keyfile)
        # Read the encrypted message from a file
        encrypted_message = read_from_file(args.infile)
        # Decrypt the message using the key
        decrypted_message = decrypt_message(encrypted_message, key)
        print(f"Decrypted message: {decrypted_message}")

# Function for the GUI interface
def gui_interface():
    # Create a Tkinter root window
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Ask the user to select a key file using a file dialog
    key_file = filedialog.askopenfilename(title="Select Key File", filetypes=[("Key Files", "*.key")])
    if not key_file:
        print("Key file not selected. Exiting.")
        return

    # Ask the user whether to encrypt or decrypt
    action = input("Do you want to (e)ncrypt or (d)ecrypt? ").lower()

    # Encryption process in GUI
    if action == 'e':
        # Load the key from the selected file
        key = load_key(key_file)
        # Get the message to encrypt from user input
        message = input("Enter message to encrypt: ")
        # Encrypt the message using the key
        encrypted_message = encrypt_message(message.encode(), key)
        # Ask the user to select a file to save the encrypted message
        output_file = filedialog.asksaveasfilename(title="Save Encrypted Message", defaultextension=".enc")
        if output_file:
            # Write the encrypted message to the selected file
            write_to_file(output_file, encrypted_message)
            print(f"Message encrypted and saved to {output_file}")

    # Decryption process in GUI
    elif action == 'd':
        # Load the key from the selected file
        key = load_key(key_file)
        # Ask the user to select an encrypted message file
        input_file = filedialog.askopenfilename(title="Select Encrypted Message File", filetypes=[("Encrypted Files", "*.enc")])
        if input_file:
            # Read the encrypted message from the selected file
            encrypted_message = read_from_file(input_file)
            # Decrypt the message using the key
            decrypted_message = decrypt_message(encrypted_message, key)
            print(f"Decrypted message: {decrypted_message}")

# Execute the command-line interface function if the script is run directly
if __name__ == "__main__":
    command_line_interface()
