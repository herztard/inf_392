from Crypto.Hash import SHA256


def get_hash(byte_string: bytes):
    hasher = SHA256.new()
    hasher.update(byte_string)
    return hasher.digest()


def get_hash_salted(byte_string: bytes, salt: bytes):
    hasher = SHA256.new()
    hasher.update(salt + byte_string)
    return salt + hasher.digest()


def verify_hash(byte_string: bytes, hash: bytes):
    h = get_hash(byte_string)
    return h == hash


def verify_hash_salted(byte_string: bytes, hash: bytes, salt_size: int):
    h = get_hash_salted(byte_string, hash[:salt_size])
    return h == hash
