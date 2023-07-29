import random
import string

def mod_exp(base, exponent, modulus):
    result = 1
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent //= 2
        base = (base * base) % modulus
    return result

def generate_keypair(p):
    g = random.randint(2, p - 1)
    a = random.randint(2, p - 2)
    A = mod_exp(g, a, p)
    return (p, g, a, A)

def encrypt(p, g, A, plaintext):
    k = random.randint(2, p - 2)
    K = mod_exp(g, k, p)
    shared_secret = mod_exp(A, k, p)
    c1 = mod_exp(g, k, p)
    c2 = (plaintext * shared_secret) % p
    return (c1, c2)

def decrypt(p, a, ciphertext):
    c1, c2 = ciphertext
    shared_secret = mod_exp(c1, a, p)
    inverse_shared_secret = pow(shared_secret, -1, p)
    plaintext = (c2 * inverse_shared_secret) % p
    return plaintext

def avalanche_effect(p, g, A, plaintext):
    ciphertext = encrypt(p, g, A, plaintext)
    changed_bits = 0
    for i in range(len(plaintext)):
        for j in range(8):
            modified_plaintext = plaintext[:i] + bytes([plaintext[i] ^ (1 << j)]) + plaintext[i+1:]
            modified_ciphertext = encrypt(p, g, A, modified_plaintext)
            for bit1, bit2 in zip(ciphertext, modified_ciphertext):
                if bit1 != bit2:
                    changed_bits += bin(bit1 ^ bit2).count('1')
    return changed_bits / (len(plaintext) * 8)

def generate_random_data(length):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length)).encode()
