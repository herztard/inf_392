from utils.rsa import generate_rsa_keys, encrypt_rsa
from utils.hash import get_hash
from utils.aes import encrypt_cbc, decrypt_cbc
from typing import Tuple


# TODO: complete the function
def encrypt_and_mac(plain: bytes, key: bytes, mac_key: Tuple[int, int]) -> bytes:
    ### YOUR CODE ###
    concat = b''
    key_hash = get_hash(key)
    encrypted = encrypt_cbc(plain, key_hash)

    h = get_hash(plain)

    mac = encrypt_rsa(h, mac_key)

    mac_size_bytes = len(mac).to_bytes(2, byteorder='big')
    concat = encrypted + mac + mac_size_bytes

    return concat
    


def decrypt_and_verify_mac_and_encrypt(cipher: bytes, key: str, mac_key: Tuple[int, int]) -> bytes:
    key_hash = get_hash(key)

    mac_size = int.from_bytes(cipher[-2:])

    encrypted = cipher[:-2 - mac_size]
    mac = cipher[-2 - mac_size:-2]

    decrypted = decrypt_cbc(encrypted, key_hash)

    h = get_hash(decrypted)
    mac_h = encrypt_rsa(mac, mac_key)

    assert h == mac_h

    return decrypted
    


plain = b'Hello'
key = b'Some key'

public_key, private_key = generate_rsa_keys()

encrypted = encrypt_and_mac(plain, key, private_key)

decrypted = decrypt_and_verify_mac_and_encrypt(encrypted, key, public_key)


print("Plain: %s" % (plain,))
print("Key: %s" % (key,))
print("Encrypted: %s" % (encrypted,))
print("Decrypted: %s" % (decrypted,))
