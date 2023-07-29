import time
from elgamal_algorithm import *
from diffie_hellman_algorithm import *
from dsa_algorithm import *
from rsa_algorithm import *
import math


def calculate_entropy(data):
    if not data:
        return 0.0

    entropy = 0.0
    data_size = len(data)
    frequency_dict = {}

    for byte in data:
        frequency_dict[byte] = frequency_dict.get(byte, 0) + 1

    for freq in frequency_dict.values():
        probability = freq / data_size
        entropy -= probability * math.log2(probability)

    return entropy

def measure_time(func, *args):
    start_time = time.time()
    result = func(*args)
    end_time = time.time()
    elapsed_time = end_time - start_time
    return result, elapsed_time

def run_diffie_hellman_tests():
    # Similar structure as elgamal tests
    pass

def run_dsa_tests():
    # Similar structure as elgamal tests
    pass

def run_rsa_tests():
    # Similar structure as elgamal tests
    pass

if __name__ == "__main__":
    print("ElGamal Performance Analysis:")
    run_elgamal_tests()

    print("Diffie-Hellman Performance Analysis:")
    run_diffie_hellman_tests()

    print("DSA Performance Analysis:")
    run_dsa_tests()

    print("RSA Performance Analysis:")
    run_rsa_tests()
