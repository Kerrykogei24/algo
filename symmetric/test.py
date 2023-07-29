import tkinter as tk
from tkinter import messagebox
from Crypto.Random import get_random_bytes
from matplotlib import pyplot as plt

from des_algorithm import des_encrypt, des_decrypt
from triple_des_algorithm import triple_des_encrypt, triple_des_decrypt
from aes_algorithm import aes_encrypt, aes_decrypt
from blowfish_algorithm import blowfish_encrypt, blowfish_decrypt
import time
import sys
import string
import random

def generate_random_data(length):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length)).encode()



algorithm_names = []
encryption_times = []

def run_algorithm(algorithm_name, encrypt_func, decrypt_func, key, data):
    # Encryption
    start_time = time.time()
    encrypted_data = encrypt_func(key, data)
    encryption_time = time.time() - start_time

    # Decryption
    start_time = time.time()
    decrypted_data = decrypt_func(key, encrypted_data)
    decryption_time = time.time() - start_time

    # Avalanche effect
    total_bits = len(data) * 8
    changed_bits = 0
    for i in range(len(data)):
        for j in range(8):
            modified_data = bytearray(data)
            modified_data[i] ^= 1 << j
            encrypted_modified_data = encrypt_func(key, bytes(modified_data))
            changed_bits += bin(int.from_bytes(encrypted_modified_data, byteorder=sys.byteorder)).count('1')
    avalanche_effect = changed_bits / total_bits

    algorithm_names.append(algorithm_name)
    encryption_times.append(encryption_time)
   

    result = f"{algorithm_name}\nEncryption Time: {encryption_time:.3f} seconds\nDecryption Time: {decryption_time:.3f} seconds\nAvalanche Effect: {avalanche_effect:.3f}\n\n"
    return result

def test_algorithms(data):
    data = data.encode()

    # Test DES
    des_key = get_random_bytes(8)
    des_result = run_algorithm("DES", des_encrypt, des_decrypt, des_key, data)

    # Test 3DES
    triple_des_key = get_random_bytes(16)
    triple_des_result = run_algorithm("3DES", triple_des_encrypt, triple_des_decrypt, triple_des_key, data)

    # Test AES
    aes_key = get_random_bytes(16)
    aes_result = run_algorithm("AES", aes_encrypt, aes_decrypt, aes_key, data)

    # Test Blowfish
    blowfish_key = get_random_bytes(16)
    blowfish_result = run_algorithm("Blowfish", blowfish_encrypt, blowfish_decrypt, blowfish_key, data)

  


 
    # Display results in a messagebox
    result_text = des_result + triple_des_result + aes_result + blowfish_result   
    messagebox.showinfo("Algorithm Test Results", result_text)

    plt.bar(algorithm_names, encryption_times)
    plt.xlabel("Algorithms")
    plt.ylabel("Encryption Time (seconds)")
    plt.title("Comparison of Encryption Time for Different Algorithms")
    plt.show()


# Create the UI
window = tk.Tk()
window.title("Algorithm Test")
window.geometry("400x300")

# Data Input Label
data_label = tk.Label(window, text="Data to Encrypt/Decrypt:")
data_label.pack()

# Data Input Field
data_entry = tk.Entry(window, width=40)
data_entry.pack(pady=10)

def run_test():
    data = data_entry.get().strip()
    if data:
        test_algorithms(data)
    else:
        messagebox.showwarning("Error", "Please enter data for encryption/decryption.")

# Run Test Button
test_button = tk.Button(window, text="Run Test", command=run_test)
test_button.pack(pady=10)

# Start the UI loop
window.mainloop()
