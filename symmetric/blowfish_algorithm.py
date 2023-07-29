from Crypto.Cipher import Blowfish
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

def blowfish_encrypt(key, data):
    cipher = Blowfish.new(key, Blowfish.MODE_ECB)
    padded_data = pad(data, Blowfish.block_size)
    encrypted_data = cipher.encrypt(padded_data)
    return encrypted_data

def blowfish_decrypt(key, encrypted_data):
    cipher = Blowfish.new(key, Blowfish.MODE_ECB)
    decrypted_data = cipher.decrypt(encrypted_data)
    unpadded_data = unpad(decrypted_data, Blowfish.block_size)
    return unpadded_data

if __name__ == "__main__":
    key = get_random_bytes(16)
    data = b"Hello, Blowfish!"

    encrypted_data = blowfish_encrypt(key, data)
    decrypted_data = blowfish_decrypt(key, encrypted_data)

    print("Encrypted data:", encrypted_data)
    print("Decrypted data:", decrypted_data)
