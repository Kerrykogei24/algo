import random


import time
import random

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
    x = random.randint(2, p - 2)
    y = mod_exp(g, x, p)
    return (p, g, x, y)

def sign(p, g, x, message):
    k = random.randint(2, p - 2)
    r = mod_exp(g, k, p) % (p - 1)
    k_inv = pow(k, -1, p - 1)
    s = (k_inv * (message + x * r)) % (p - 1)
    return (r, s)

def verify(p, g, y, message, signature):
    r, s = signature
    if 0 < r < p - 1 and 0 < s < p - 1:
        w = pow(s, -1, p - 1)
        u1 = (message * w) % (p - 1)
        u2 = (r * w) % (p - 1)
        v = (mod_exp(g, u1, p) * mod_exp(y, u2, p)) % p
        return v == r
    return False
