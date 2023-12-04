from cryptography.fernet import Fernet

def generate_key():
    """
    Generate a key for encryption and decryption.
    """
    return Fernet.generate_key()

def write_to_file(file_path, encrypted_message):
    """
    Write encrypted message to a file.
    :param file_path: Path to the file.
    :param encrypted_message: Encrypted message to be written.
    """
    with open(file_path, 'wb') as file:
        file.write(encrypted_message)

def read_from_file(file_path):
    """
    Read encrypted message from a file.
    :param file_path: Path to the file.
    :return: Encrypted message read from the file.
    """
    with open(file_path, 'rb') as file:
        return file.read()

def encrypt_message(message, key):
    """
    Encrypt a message using a key.
    :param message: Message to be encrypted.
    :param key: Key for encryption.
    :return: Encrypted message.
    """
    cipher_suite = Fernet(key)
    encrypted_message = cipher_suite.encrypt(message.encode())
    return encrypted_message

def decrypt_message(encrypted_message, key):
    """
    Decrypt a message using a key.
    :param encrypted_message: Encrypted message.
    :param key: Key for decryption.
    :return: Decrypted message.
    """
    cipher_suite = Fernet(key)
    decrypted_message = cipher_suite.decrypt(encrypted_message).decode()
    return decrypted_message
