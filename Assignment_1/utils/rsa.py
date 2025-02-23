import random
from typing import Tuple
from Assignment_1.utils.generators import generate_prime_number
from Assignment_1.utils.math import gcd, modinv


def generate_rsa_keys(key_length=1024, e=65537):
    bit_length = key_length // 2

    # Generate two prime numbers for RSA
    p = generate_prime_number(bit_length)
    q = generate_prime_number(bit_length)

    while p == q:
        q = generate_prime_number(bit_length)

    # TODO: Finish RSA key generaiton
    ### YOUR CODE ###
    n = p * q
    phi = (p - 1) * (q - 1)
    d = modinv(e, phi)

    return ((e, n), (d, n))


def encrypt(number: int, key: Tuple[int, int]):
    # TODO: Finish RSA encryption (this function can be also used for decryption)
    ### YOUR CODE ###
    exponent, modulus = key
    cipher_number = pow(number, exponent, modulus)
    return cipher_number

