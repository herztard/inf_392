from Assignment_1.utils.generators import generate_prime_number
from Assignment_1.utils.math import find_primitive_root
from random import randint

def generate_public_components():
    # TODO: Generate public components: p and g
    ### YOUR CODE ###
    p = generate_prime_number(64)

    g = find_primitive_root(p)

    return (p, g)

def generate_private_key(p):
    # TODO: Generate private key
    ### YOUR CODE ###
    return randint(2, p - 2)

def compute_public_key(private_key, p, g):
    # TODO: Compute the public key given the private key and public components
    ### YOUR CODE ###
    return pow(g, private_key, p)

def compute_shared_secret(other_public_key, private_key, p):
    # TODO: Compute the shared key
    ### YOUR CODE ###
    return pow(other_public_key, private_key, p)