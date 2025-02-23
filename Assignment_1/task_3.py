from utils.hash import get_hash_salted
from utils.generators import generate_bytes 


HASH_SIZE = 64

pairs = [
    ["Hello", "Hello"],
    ["Hello", "Blockhain"],
    ["Hello Blockhain", "Hello Blockhain"],
    ["Hello Blockhain", "Hello  Blockhain"],
]

for index, pair in enumerate(pairs):
    print("CASE %s/%s" % (index + 1, len(pairs)))

    text_1, text_2 = pair

    b_message_1 = text_1.encode('utf-8')
    b_message_2 = text_2.encode('utf-8')

    salt = generate_bytes(16)
    hash_1 = get_hash_salted(b_message_1, salt, HASH_SIZE)
    hash_2 = get_hash_salted(b_message_2, salt, HASH_SIZE)

    print("Message 1 (length: %s): %s" % (len(b_message_1), b_message_1,))
    print("Message 2 (length: %s): %s" % (len(b_message_2), b_message_2,))
    print("Hash 1 (length: %s): %s" % (len(hash_1), hash_1,))
    print("Hash 2 (length: %s): %s" % (len(hash_2), hash_2,))
    print("Hash 1 == Hash 2: %s" % (hash_1 == hash_2,))

    print()
