from Crypto.Hash import MD4


def get_hash(byte_string: bytes, block_size: int):
    # TODO: Generate hash using MD4 and truncate the hash to the given block_size
    ### YOUR CODE ###


def get_hash_salted(byte_string: bytes, salt: bytes, block_size: int):
    # TODO: Generate salted hash using MD4
    # Hint: truncate the hash to the given size: block_size - len(salt)
    ### YOUR CODE ###


def verify_hash(byte_string: bytes, hash: bytes):
    h = get_hash(byte_string)
    return h == hash


def verify_hash_salted(byte_string: bytes, hash: bytes, salt_size: int):
    h = get_hash_salted(byte_string, hash[:salt_size])
    return h == hash
