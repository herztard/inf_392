from utils.generators import generate_prime_number
from utils.math import find_primitive_root
from random import randint

def generate_public_components():
    # TODO: Generate public components: p and g
    ### YOUR CODE ###
    return (p, g)

def generate_private_key(p):
    # TODO: Generate private key
    ### YOUR CODE ###

def compute_public_key(private_key, p, g):
    # TODO: Compute the public key given the private key and public components
    ### YOUR CODE ###

def compute_shared_secret(other_public_key, private_key, p):
    # TODO: Compute the shared key
    ### YOUR CODE ###
