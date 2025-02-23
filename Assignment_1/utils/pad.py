# TODO: Implement PKCS#7 padding (https://en.wikipedia.org/wiki/Padding_(cryptography))

def add_pads(byte_string, block_size):
    ### YOUR CODE ###
    padding_length = block_size - (len(byte_string) % block_size)
    return byte_string + bytes([padding_length]) * padding_length



def remove_pads(byte_string: bytes):
    ### YOUR CODE ###
    padding_length = byte_string[-1]
    return byte_string[:-padding_length]