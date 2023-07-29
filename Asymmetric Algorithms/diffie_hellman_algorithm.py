import random

def mod_exp(base, exponent, modulus):
    result = 1
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent //= 2
        base = (base * base) % modulus
    return result

def generate_shared_secret(p, g, a, A):
    K = mod_exp(A, a, p)
    return K
