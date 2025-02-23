import random
from Assignment_1.utils.math import is_prime

def generate_bytes(size: int):
    # TODO: Generate random bytes of the given size
    ### YOUR CODE ###
    return bytes(random.getrandbits(8) for _ in range(size))

def generate_prime_candidate(length):
    """Generate an odd integer randomly."""
    p = random.getrandbits(length)
    p |= (1 << length - 1) | 1
    return p

def generate_prime_number(length=1024):
    """Generate a prime number of specified length."""
    p = 0
    while not is_prime(p, 128):
        p = generate_prime_candidate(length)
    return p

