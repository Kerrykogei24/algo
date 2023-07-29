import os
import time
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

def generate_random_key(key_size):
    return os.urandom(key_size // 8)

def generate_random_data(data_size):
    return os.urandom(data_size // 8)

def encrypt_decrypt_time(key_size, data_size):
    key = generate_random_key(key_size)
    data = generate_random_data(data_size)

    backend = default_backend()
    cipher = Cipher(algorithms.IDEA(key), modes.ECB(), backend=backend)

    encryptor = cipher.encryptor()
    start_time = time.time()
    ciphertext = encryptor.update(data) + encryptor.finalize()
    encryption_time = time.time() - start_time

    decryptor = cipher.decryptor()
    start_time = time.time()
    decrypted_data = decryptor.update(ciphertext) + decryptor.finalize()
    decryption_time = time.time() - start_time

    assert decrypted_data == data  # Verify decryption correctness

    return encryption_time, decryption_time
