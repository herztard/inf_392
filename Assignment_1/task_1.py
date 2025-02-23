from utils.pad import add_pads, remove_pads

BLOCK_SIZE = 8

texts = [
    "Hello",
    "Blockhain",
    "Hello Blockhain",
]

for index, text in enumerate(texts): 
    print("CASE %s/%s" % (index + 1, len(texts)))

    b_text = text.encode('utf-8')
    b_text_padded = add_pads(b_text, BLOCK_SIZE)
    b_textunpadded = remove_pads(b_text_padded)

    print("Byte string (length: %s): %s" % (len(b_text), b_text,))
    print("Byte string after adding paddings (length: %s): %s" % (len(b_text_padded), b_text_padded,))
    print("Byte string after removing paddings (length: %s): %s" % (len(b_textunpadded), b_textunpadded,))

    print()
