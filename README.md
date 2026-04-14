# Kcryption — File Encryptor & Decryptor

A lightweight desktop app for encrypting and decrypting files using a password-based key. Built with Python, Tkinter, and the `cryptography` library.

---

## Features

- Browse and select any file from your filesystem
- Encrypt files in-place using a password-derived Fernet key
- Decrypt files back to their original content
- Dark-themed, minimal UI

---

## Prerequisites

- Python 3.8 or higher
- `tkinter` (included with most Python installations)

---

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/Kcryption.git
   cd Kcryption
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

Run the app:

```bash
python kcryption.py
```

1. Click **Browse File** to select the file you want to encrypt or decrypt.
2. Enter your password in the input field.
3. Click **Encrypt File** to encrypt, or **Decrypt File** to decrypt.

> **Note:** The same password must be used to decrypt a file that was encrypted with it. Encryption modifies the file in-place.

---

## How It Works

Kcryption uses [Fernet](https://cryptography.io/en/latest/fernet/) symmetric encryption from the `cryptography` library. The password you enter is padded/truncated to form a valid 44-character base64 Fernet key, which is then used to encrypt or decrypt the selected file.

---

## Built With

- [Python 3](https://www.python.org/)
- [Tkinter](https://docs.python.org/3/library/tkinter.html) — GUI
- [cryptography](https://cryptography.io/) — Fernet encryption

---

## Credits

Built by Kwasi GA
