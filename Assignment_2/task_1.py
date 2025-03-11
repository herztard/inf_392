from utils.rsa import generate_rsa_keys, encrypt_rsa
from utils.hash import get_hash
from utils.aes import encrypt_cbc, decrypt_cbc
from typing import Tuple


# TODO: complete the function
def mac_then_encrypt(plain: bytes, key: bytes, mac_key: Tuple[int, int]) -> bytes:
    ### YOUR CODE ###
    hash_value = get_hash(plain)

    mac = encrypt_rsa(hash_value, mac_key)

    mac_size = len(mac).to_bytes(2, byteorder='big')
    combined_data = plain + mac + mac_size

    key_hash = get_hash(key)
    encrypted = encrypt_cbc(combined_data, key_hash)

    return encrypted



def decrypt_and_verify_mac_then_encrypt(cipher: bytes, key: str, mac_key: Tuple[int, int]) -> bytes:
    key_hash = get_hash(key)

    decrypted = decrypt_cbc(cipher, key_hash)

    mac_size = int.from_bytes(decrypted[-2:])

    plain = decrypted[:-2 - mac_size]
    mac = decrypted[-2 - mac_size:-2]

    h = get_hash(plain)
    mac_h = encrypt_rsa(mac, mac_key)

    assert h == mac_h

    return plain
    

plain = b'Hello'
key = b'Some key'

public_key, private_key = generate_rsa_keys()

encrypted = mac_then_encrypt(plain, key, private_key)

decrypted = decrypt_and_verify_mac_then_encrypt(encrypted, key, public_key)


print("Plain: %s" % (plain,))
print("Key: %s" % (key,))
print("Encrypted: %s" % (encrypted,))
print("Decrypted: %s" % (decrypted,))
