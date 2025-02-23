from utils.des import encrypt_ecb, decrypt_ecb


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

    ciphertext = encrypt_ecb(b_text, b_key)
    ciphertext_decrypted = decrypt_ecb(ciphertext, b_key)

    print("DES (ECB): Text (length: %s): %s" % (len(b_text), b_text,))
    print("DES (ECB): Key (length: %s): %s" % (len(b_key), b_key,))
    print("DES (ECB): Ciphertext (length: %s): %s" % (len(ciphertext), ciphertext,))
    print("DES (ECB): Decrypted Ciphertext (length: %s): %s" % (len(ciphertext_decrypted), ciphertext_decrypted,))

    print()
