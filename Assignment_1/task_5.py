from utils.des import encrypt_cbc, decrypt_cbc


pairs = [
    ["Hello Blockhain", "Hello"],
    ["Hello Blockhain", "Hello"],
    ["Hello", "ABC"],
    ["Hello", "ABC"],
]

for index, pair in enumerate(pairs):
    print("CASE %s/%s" % (index + 1, len(pairs)))

    text, key = pair

    b_text = text.encode('utf-8')
    b_key = key.encode('utf-8')

    ciphertext = encrypt_cbc(b_text, b_key)
    ciphertext_decrypted = decrypt_cbc(ciphertext, b_key)

    print("DES (CBC): Text (length: %s): %s" % (len(b_text), b_text,))
    print("DES (CBC): Key (length: %s): %s" % (len(b_key), b_key,))
    print("DES (CBC): Ciphertext (length: %s): %s" % (len(ciphertext), ciphertext,))
    print("DES (CBC): Decrypted Ciphertext (length: %s): %s" % (len(ciphertext_decrypted), ciphertext_decrypted,))

    print()
