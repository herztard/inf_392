from Crypto.Cipher import DES
from Assignment_2.utils.generators import generate_bytes
from Assignment_2.utils.pad import add_pads, remove_pads
from Assignment_2.utils.hash import get_hash


BLOCK_SIZE = 8


def encrypt_ecb(plain: bytes, key: bytes):
    key_hash = get_hash(key, BLOCK_SIZE)
    plain = add_pads(plain, BLOCK_SIZE)
    des = DES.new(key_hash, DES.MODE_ECB)
    return des.encrypt(plain)


def decrypt_ecb(cipher: bytes, key: bytes):
    key_hash = get_hash(key, BLOCK_SIZE)
    des = DES.new(key_hash, DES.MODE_ECB)
    return remove_pads(des.decrypt(cipher))


def encrypt_cbc(plain: bytes, key: bytes):
    key_hash = get_hash(key, BLOCK_SIZE)
    iv = generate_bytes(BLOCK_SIZE)
    plain = add_pads(plain, BLOCK_SIZE)
    des = DES.new(key_hash, DES.MODE_CBC, IV=iv)
    return iv + des.encrypt(plain)


def decrypt_cbc(cipher: bytes, key: bytes):
    key_hash = get_hash(key, BLOCK_SIZE)
    iv, cipher = cipher[:BLOCK_SIZE], cipher[BLOCK_SIZE:]
    des = DES.new(key_hash, DES.MODE_CBC, IV=iv)
    return remove_pads(des.decrypt(cipher))
