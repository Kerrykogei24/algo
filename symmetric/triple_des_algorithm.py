from Crypto.Cipher import DES3
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

def triple_des_encrypt(key, data):
    cipher = DES3.new(key, DES3.MODE_ECB)
    padded_data = pad(data, DES3.block_size)
    encrypted_data = cipher.encrypt(padded_data)
    return encrypted_data

def triple_des_decrypt(key, encrypted_data):
    cipher = DES3.new(key, DES3.MODE_ECB)
    decrypted_data = cipher.decrypt(encrypted_data)
    unpadded_data = unpad(decrypted_data, DES3.block_size)
    return unpadded_data

if __name__ == "__main__":
    key = get_random_bytes(16)
    data = b"Hello, 3DES!"

    encrypted_data = triple_des_encrypt(key, data)
    decrypted_data = triple_des_decrypt(key, encrypted_data)

    print("Encrypted data:", encrypted_data)
    print("Decrypted data:", decrypted_data)
