import getpass
import sqlite3
from cryptography.fernet import Fernet

# ----------------- KEY MANAGEMENT -----------------
# We need a key to encrypt/decrypt. 
# If we lose this key, all passwords are lost forever!
def load_key():
    try:
        # Try to read the key from a file
        with open("secret.key", "rb") as key_file:
            key = key_file.read()
        return key
    except FileNotFoundError:
        # If file doesn't exist, generate a new key and save it
        key = Fernet.generate_key()
        with open("secret.key", "wb") as key_file:
            key_file.write(key)
        return key

# Initialize the encryption tool with our key
key = load_key()
cipher_suite = Fernet(key)

# ----------------- DATABASE SETUP -----------------
# We use SQLite because it's built into Python (no install needed).
def init_db():
    conn = sqlite3.connect("passwords.db")
    cursor = conn.cursor()
    
    # Create table if it doesn't exist
    # Notice we store 'encrypted_password' - NOT plain text!
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS credentials (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            service TEXT NOT NULL,
            username TEXT NOT NULL,
            encrypted_password BLOB NOT NULL
        )
    ''')
# Run the DB setup once when the script starts
init_db()
print("System Ready: Database connected and Encryption Key loaded.")    

def add_password(service, username, password):
    conn = sqlite3.connect("passwords.db")
    cursor = conn.cursor()

    # 1. Encrypt the password
    # .encode() converts string to bytes, which is required for encryption
    encrypted_pwd = cipher_suite.encrypt(password.encode())

    # 2. Store it in the database
    cursor.execute(
        "INSERT INTO credentials (service, username, encrypted_password) VALUES (?, ?, ?)",
        (service, username, encrypted_pwd)
    )
    conn.commit()
    conn.close()
    print(f"\n[+] Success! Password for {service} saved securely.")

def get_password(service):
    conn = sqlite3.connect("passwords.db")
    cursor = conn.cursor()

    # Find the entry by service name
    cursor.execute("SELECT username, encrypted_password FROM credentials WHERE service=?", (service,))
    result = cursor.fetchone()
    conn.close()

    if result:
        username = result[0]
        encrypted_pwd = result[1]

        # Decrypt the password
        decrypted_pwd = cipher_suite.decrypt(encrypted_pwd).decode()

        print(f"\n--- Credentials for {service} ---")
        print(f"Username: {username}")
        print(f"Password: {decrypted_pwd}")
    else:
        print(f"\n[!] No password found for {service}")



# ----------------- MAIN MENU -----------------
while True:
    print("\n--- Secure Password Manager ---")
    print("1. Add a new password")
    print("2. Retrieve a password")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        s = input("Enter Service Name (e.g., Gmail): ")
        u = input("Enter Username: ")
        p = getpass.getpass("Enter Password: ")
        add_password(s, u, p)

    elif choice == '2':
        s = input("Enter Service Name to retrieve: ")
        get_password(s)

    elif choice == '3':
        break
    else:
        print("Invalid choice!")


