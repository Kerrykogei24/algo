import tkinter as tk
from tkinter import messagebox
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import PKCS1_OAEP
import time
import sys
import string
import random

# Function to generate random data of a given length
def generate_random_data(length):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length)).encode()

def rsa_encrypt(key, data):
    cipher = PKCS1_OAEP.new(key).encrypt(data)
    return cipher

def rsa_decrypt(key, encrypted_data):
    data = PKCS1_OAEP.new(key).decrypt(encrypted_data)
    return data

def run_algorithm(encrypt_func, decrypt_func, key, data):
    # Encryption
    start_time = time.time()
    encrypted_data = encrypt_func(key, data)
    encryption_time = time.time() - start_time

    # Decryption
    start_time = time.time()
    decrypted_data = decrypt_func(key, encrypted_data)
    decryption_time = time.time() - start_time

    result = f"Encryption Time: {encryption_time:.3f}\nDecryption Time: {decryption_time:.3f}\n\n"
    return result

def test_algorithm(public_key, private_key, data):
    public_key = RSA.import_key(public_key)
    private_key = RSA.import_key(private_key)
    data = data.encode()

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
