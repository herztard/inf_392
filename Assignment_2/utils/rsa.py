import random
from typing import Tuple
from Assignment_2.utils.generators import generate_prime_number
from Assignment_2.utils.math import gcd, modinv
from Assignment_2.utils.format import bytes_to_numeric, numeric_to_bytes

def generate_rsa_keys(key_length=1024, e=65537):
    bit_length = key_length // 2

    # Generate two prime numbers for RSA
    p = generate_prime_number(bit_length)
    q = generate_prime_number(bit_length)

    while p == q:
        q = generate_prime_number(bit_length)

    n = p * q
    phi = (p - 1) * (q - 1)

    while gcd(e, phi) != 1:
        e = random.randrange(2, phi)

    # Calculate decryption exponent d
    d = modinv(e, phi)

    return ((e, n), (d, n))


def encrypt_rsa(plain: bytes, key: Tuple[int, int]) -> bytes:
    v = bytes_to_numeric(plain)
    c = pow(v, key[0], key[1])
    return numeric_to_bytes(c)
