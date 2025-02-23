from utils.format import text_to_numeric, numeric_to_text
from utils.rsa import generate_rsa_keys, encrypt


public_key, private_key = generate_rsa_keys()
message = b"Hello Blockhain"
message_numeric = text_to_numeric(message)
cipher = encrypt(message_numeric, private_key)
decrypted = encrypt(cipher, public_key)
message_decrypted = numeric_to_text(decrypted)


print("Public key: %s" % (public_key,))
print("Private key: %s" % (private_key,))
print("Message: %s" % (message,))
print("Message numeric: %s" % (message_numeric,))
print("Cipher numeric: %s" % (cipher,))
print("Decrypted numeric: %s" % (decrypted,))
print("Decrypted message: %s" % (message_decrypted,))
