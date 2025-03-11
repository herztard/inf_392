from tinyec import registry
from .aes import encrypt_cbc, decrypt_cbc
import secrets
import hashlib


def ecc_point_to_256_bit_key(point):
    sha = hashlib.sha256(int.to_bytes(point.x, 32, 'big'))
    sha.update(int.to_bytes(point.y, 32, 'big'))
    return sha.digest()


# TODO: complete the function
def encrypt_ecc(plain: bytes, public_key):
    curve = registry.get_curve('secp256r1')
    c_priv_key = secrets.randbelow(curve.field.n)
    c_pub_key = c_priv_key * curve.g
    
    ### YOUR CODE ###
    shared_point = c_priv_key * public_key
    symmetric_key = ecc_point_to_256_bit_key(shared_point)
    encrypted = encrypt_cbc(plain, symmetric_key)
    return encrypted, c_pub_key


# TODO: complete the function
def decrypt_ecc(cipher: bytes, c_pub_key, private_key):
    ### YOUR CODE ###
    curve = registry.get_curve('secp256r1')
    shared_point = private_key * c_pub_key
    symmetric_key = ecc_point_to_256_bit_key(shared_point)
    decrypted = decrypt_cbc(cipher, symmetric_key)
    return decrypted
