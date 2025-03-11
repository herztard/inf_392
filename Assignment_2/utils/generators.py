import random
from Assignment_2.utils.math import is_prime

def generate_bytes(size: int):
    numbers = []
    for _ in range(size):
        numbers.append(random.randint(0, 255))
    return bytes(numbers)

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

