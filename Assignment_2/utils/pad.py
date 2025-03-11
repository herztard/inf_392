def add_pads(byte_string, block_size):
    n = block_size - (len(byte_string) % block_size)
    return byte_string + bytes([n]) * n


def remove_pads(byte_string: bytes):
    n = int(byte_string[-1])
    return byte_string[:-n]
