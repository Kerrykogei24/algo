from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Random import get_random_bytes

def rsa_encrypt(public_key, data):
    cipher = PKCS1_OAEP.new(public_key)
    encrypted_data = cipher.encrypt(data)
    return encrypted_data

def rsa_decrypt(private_key, encrypted_data):
    cipher = PKCS1_OAEP.new(private_key)
    decrypted_data = cipher.decrypt(encrypted_data)
    return decrypted_data

if __name__ == "__main__":
    key = RSA.generate(2048)

    data = b"Hello, RSA!"

    encrypted_data = rsa_encrypt(key.publickey(), data)
    decrypted_data = rsa_decrypt(key, encrypted_data)

    print("Encrypted data:", encrypted_data)
    print("Decrypted data:", decrypted_data)
