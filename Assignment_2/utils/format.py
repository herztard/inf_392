def bytes_to_numeric(plain: bytes):
    value = int.from_bytes(plain, 'big')
    return value

def numeric_to_bytes(value: int):
    byte_length = (value.bit_length() + 7) // 8
    return value.to_bytes(byte_length, 'big', signed=False)
