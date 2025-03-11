from tinyec import registry
import secrets
from utils.ecc import encrypt_ecc, decrypt_ecc


plain = b'Hello'

curve = registry.get_curve('secp256r1')
private_key = secrets.randbelow(curve.field.n)
public_key = private_key * curve.g

encrypted, c_pub_key = encrypt_ecc(plain, public_key)

decrypted = decrypt_ecc(encrypted, c_pub_key, private_key)


print("Plain: %s" % (plain,))
print("Encrypted: %s" % (encrypted,))
print("Decrypted: %s" % (decrypted,))
