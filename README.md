# 🔐 Secure CLI Password Manager

A lightweight, secure command-line interface (CLI) tool built with Python to store and retrieve credentials. This project demonstrates the implementation of **AES-128 symmetric encryption** and **SQL database management** to ensure sensitive data confidentiality.

## 🚀 Overview

This tool addresses the problem of insecure password storage by providing a local, encrypted vault. Unlike simple text-based storage, this application encrypts passwords *before* they are saved to the database, ensuring that even if the database file is stolen, the credentials remain unreadable without the encryption key.

## ✨ Features

* **AES Encryption:** Uses the `cryptography` library (Fernet) to encrypt passwords at rest.
* **Persistent Storage:** robust data management using a local **SQLite** database.
* **Key Management:** Automated generation and handling of the encryption key (`secret.key`).
* **CRUD Operations:** Full functionality to **C**reate (add) and **R**ead (retrieve) credentials.
* **Hidden Input:** Secure password masking during entry (using `getpass`).

## 🛠️ Technologies Used

* **Language:** Python 3.x
* **Database:** SQLite3
* **Security:** `cryptography` library (Fernet/AES)
* **Interface:** Command Line Interface (CLI)

## ⚙️ Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YOUR-USERNAME/secure-password-manager.git](https://github.com/YOUR-USERNAME/secure-password-manager.git)
    cd secure-password-manager
    ```

2.  **Install dependencies:**
    You need the `cryptography` library for encryption functions.
    ```bash
    pip install cryptography
    ```

3.  **Run the application:**
    ```bash
    python password_manager.py
    ```

## 📖 Usage Guide

Upon running the script, you will be presented with a menu:

1.  **Add a new password:**
    * Prompts for the **Service Name** (e.g., "Gmail").
    * Prompts for the **Username**.
    * Securely prompts for the **Password** (input is hidden).
    * Encrypts and saves the data to `passwords.db`.

2.  **Retrieve a password:**
    * Asks for the **Service Name**.
    * Fetches the encrypted blob from the database.
    * Decrypts it using `secret.key` and displays the credentials.

## 📂 Project Structure

* `password_manager.py`: The main application logic.
* `passwords.db`: The SQLite database file (automatically created).
* `secret.key`: The generated encryption key (automatically created - **keep this safe!**).

## 🔮 Future Improvements

* [ ] Implement a "Master Password" login requirement at startup.
* [ ] Add functionality to Delete or Update existing passwords.
* [ ] Create a graphical user interface (GUI) using Tkinter.

## ⚠️ Disclaimer

This project is created for **educational purposes** to demonstrate cybersecurity concepts (Encryption & Database Security). While it uses strong encryption standards, it is recommended to use established commercial password managers for critical sensitivity data.

---
*Created by Nikhil Varade*
