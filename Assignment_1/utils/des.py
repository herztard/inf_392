from Crypto.Cipher import DES
from utils.generators import generate_bytes
from utils.pad import add_pads, remove_pads
from utils.hash import get_hash


# TODO: Define block size
BLOCK_SIZE =


# TODO: Implement DES encryption with ECB mode 

def encrypt_ecb(plain: bytes, key: bytes):
    ### YOUR CODE ###


def decrypt_ecb(cipher: bytes, key: bytes):
    key_hash = get_hash(key, BLOCK_SIZE)
    des = DES.new(key_hash, DES.MODE_ECB)
    return remove_pads(des.decrypt(cipher))


# TODO: Implement DES encryption with CBC mode

def encrypt_cbc(plain: bytes, key: bytes):
    ### YOUR CODE ###


def decrypt_cbc(cipher: bytes, key: bytes):
    key_hash = get_hash(key, BLOCK_SIZE)
    iv, cipher = cipher[:BLOCK_SIZE], cipher[BLOCK_SIZE:]
    des = DES.new(key_hash, DES.MODE_CBC, IV=iv)
    return remove_pads(des.decrypt(cipher))
