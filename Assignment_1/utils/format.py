def text_to_numeric(plain: bytes):
    # TODO: Convert bytes to numeric value (big integer)
    ### YOUR CODE ###
    return int.from_bytes(plain, 'big', signed=False)

def numeric_to_text(value: int):
    byte_length = (value.bit_length() + 7) // 8
    return value.to_bytes(byte_length, 'big', signed=False)
