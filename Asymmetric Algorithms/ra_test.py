import tkinter as tk
from tkinter import messagebox
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
import time

# Create the RSA key pair and save them as PEM strings
def generate_rsa_keypair():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )

    public_key = private_key.public_key()

    private_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )

    public_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    return public_pem, private_pem

def rsa_encrypt(key, data):
    cipher = key.encrypt(
        data.encode('utf-8'),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return cipher

def rsa_decrypt(key, encrypted_data):
    data = key.decrypt(
        encrypted_data,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return data.decode('utf-8')

def run_algorithm(encrypt_func, decrypt_func, key, data):
    # Encryption
    start_time = time.time()
    encrypted_data = encrypt_func(key, data)
    encryption_time = time.time() - start_time

    # Decryption
    start_time = time.time()
    decrypted_data = decrypt_func(key, encrypted_data)
    decryption_time = time.time() - start_time

    result = f"Encryption Time: {encryption_time:.3f} seconds\nDecryption Time: {decryption_time:.3f} seconds\n\n"
    return result

def test_algorithm(public_key_pem, private_key_pem, data):
    public_key = serialization.load_pem_public_key(public_key_pem, backend=default_backend())
    private_key = serialization.load_pem_private_key(private_key_pem, password=None, backend=default_backend())
    data = data.encode('utf-8')  # Convert data to bytes

    result = run_algorithm(rsa_encrypt, rsa_decrypt, public_key, data)
    return result

# Create the UI
window = tk.Tk()
window.title("RSA Algorithm Test")
window.geometry("400x400")

# Public Key Input Label
public_key_label = tk.Label(window, text="Public Key (PEM format):")
public_key_label.pack()

# Public Key Input Field
public_key_entry = tk.Text(window, width=40, height=5)
public_key_entry.pack(pady=10)

# Private Key Input Label
private_key_label = tk.Label(window, text="Private Key (PEM format):")
private_key_label.pack()

# Private Key Input Field
private_key_entry = tk.Text(window, width=40, height=5)
private_key_entry.pack(pady=10)

# Data Input Label
data_label = tk.Label(window, text="Data to Encrypt/Decrypt:")
data_label.pack()

# Data Input Field
data_entry = tk.Entry(window, width=40)
data_entry.pack(pady=10)

def run_test():
    public_key = public_key_entry.get("1.0", tk.END).strip()
    private_key = private_key_entry.get("1.0", tk.END).strip()
    data = data_entry.get().strip()

    if public_key and private_key and data:
        result = test_algorithm(public_key, private_key, data)
        messagebox.showinfo("RSA Algorithm Test Results", result)
    else:
        messagebox.showwarning("Error", "Please enter the public key, private key, and data.")

# Run Test Button
test_button = tk.Button(window, text="Run Test", command=run_test)
test_button.pack(pady=10)

# Start the UI loop
window.mainloop()
