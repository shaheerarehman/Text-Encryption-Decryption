# Text Encryption/Decryption

This Python project provides a command-line interface for text encryption and decryption using the Python `cryptography` module. The script allows users to supply a message and a key value to encrypt the message. The encrypted message can be written to a file, and the script can also read text from a specified file and decrypt a message using a supplied key value.

This project utilizes the Python module `tkinter` to create a graphical user interface (GUI) for user interaction. The GUI replaces the command-line interface (CLI) to enhance user ease. The `simpledialog` module from `tkinter` is imported to facilitate interactive prompts and input collection within the GUI.

## Setting Up the Project Locally

### Prerequisites

- Python version 3.12.0 or later installed on your system.
- Git installed on your system.
- (Optional) Virtualenv installed; if not, you can install it using pip:
  - For Linux/Unix OS: `pip3 install virtualenv`
  - For Windows OS: `pip install virtualenv`

### Installation Steps

1. **Fork the Repository:**
   - Click the "Fork" button on the top-right corner of this GitHub repository to create a fork in your own GitHub account.

2. **Clone your Forked Copy:**
   - Clone your forked copy of the repository to your local machine using the following command:
     ```bash
     git clone https://github.com/shaheerarehman/Text-Encryption-Decryption.git
     ```

3. **Navigate to the Project Directory:**
   - Change your current directory to the project folder:
     ```bash
     cd Text-Encryption-Decryption/
     ```

4. **Create a New Branch:**
   - Create a new branch to work on your changes. Replace `<branch-name>` with a descriptive branch name of your choice:
     ```bash
     git checkout -b <branch-name>
     ```

5. **Create a Virtual Environment:**
   - If you don't have virtualenv installed, you can install it using pip:
     - For Linux/Unix OS: `pip3 install virtualenv`
     - For Windows OS: `pip install virtualenv`
   - Create a new virtual environment in the project folder:
     ```bash
     virtualenv env
     ```

6. **Activate the Virtual Environment:**
   - For Linux/Unix OS:
     ```bash
     source env/bin/activate
     ```
   - For Windows OS:
     ```bash
     env\Scripts\activate
     ```

7. **Install Project Dependencies:**
   - Install the project's dependencies listed in the requirements.txt file:
     ```bash
     pip install -r requirements.txt
     ```

## Usage

### Encryption

To encrypt a message and save it to a file using the GUI, run the script ("python main_script.py") and choose "Encrypt." Enter the message, the key (press Cancel to generate a new key), and the file path when prompted.

### Decryption

To decrypt a message from a file using the GUI, run the script and choose "Decrypt." Enter the file path to the encrypted message and the key when prompted. If the key used for encryption is not provided during decryption, the script will prompt you to enter it.


