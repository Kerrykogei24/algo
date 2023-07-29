from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

def aes_encrypt(key, data):
    cipher = AES.new(key, AES.MODE_ECB)
    padded_data = pad(data, AES.block_size)
    encrypted_data = cipher.encrypt(padded_data)
    return encrypted_data

def aes_decrypt(key, encrypted_data):
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted_data = cipher.decrypt(encrypted_data)
    unpadded_data = unpad(decrypted_data, AES.block_size)
    return unpadded_data

if __name__ == "__main__":
    key = get_random_bytes(16)
    data = b"Hello, AES!"

    encrypted_data = aes_encrypt(key, data)
    decrypted_data = aes_decrypt(key, encrypted_data)

    print("Encrypted data:", encrypted_data)
    print("Decrypted data:", decrypted_data)
