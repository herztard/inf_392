import random
from typing import Tuple
from utils.generators import generate_prime_number
from utils.math import gcd, modinv


def generate_rsa_keys(key_length=1024, e=65537):
    bit_length = key_length // 2

    # Generate two prime numbers for RSA
    p = generate_prime_number(bit_length)
    q = generate_prime_number(bit_length)

    while p == q:
        q = generate_prime_number(bit_length)

    # TODO: Finish RSA key generaiton
    ### YOUR CODE ###

    return ((e, n), (d, n))


def encrypt(number: int, key: Tuple[int, int]):
    # TODO: Finish RSA encryption (this function can be also used for decryption)
    ### YOUR CODE ###
    return cipher_number

