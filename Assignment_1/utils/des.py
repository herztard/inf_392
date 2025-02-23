from Crypto.Cipher import DES
from Assignment_1.utils.generators import generate_bytes
from Assignment_1.utils.pad import add_pads, remove_pads
from Assignment_1.utils.hash import get_hash


# TODO: Define block size
BLOCK_SIZE = 8


# TODO: Implement DES encryption with ECB mode 

def encrypt_ecb(plain: bytes, key: bytes):
    ### YOUR CODE ###
    key_hash = get_hash(key, BLOCK_SIZE)
    des = DES.new(key_hash, DES.MODE_ECB)
    padded_plain = add_pads(plain, BLOCK_SIZE)
    return des.encrypt(padded_plain)

def decrypt_ecb(cipher: bytes, key: bytes):
    key_hash = get_hash(key, BLOCK_SIZE)
    des = DES.new(key_hash, DES.MODE_ECB)
    return remove_pads(des.decrypt(cipher))


# TODO: Implement DES encryption with CBC mode

def encrypt_cbc(plain: bytes, key: bytes):
    ### YOUR CODE ###
    key_hash = get_hash(key, BLOCK_SIZE)
    des = DES.new(key_hash, DES.MODE_CBC)
    padded_plain = add_pads(plain, BLOCK_SIZE)
    iv = generate_bytes(BLOCK_SIZE)
    return iv + des.encrypt(padded_plain)



def decrypt_cbc(cipher: bytes, key: bytes):
    key_hash = get_hash(key, BLOCK_SIZE)
    iv, cipher = cipher[:BLOCK_SIZE], cipher[BLOCK_SIZE:]
    des = DES.new(key_hash, DES.MODE_CBC, IV=iv)
    return remove_pads(des.decrypt(cipher))
