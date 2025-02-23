from utils.dh import generate_public_components, generate_private_key, compute_public_key, compute_shared_secret


p, g = generate_public_components()

alice_priv_key = generate_private_key(p)
alice_pub_key = compute_public_key(alice_priv_key, p, g)

bob_priv_key = generate_private_key(p)
bob_pub_key = compute_public_key(bob_priv_key, p, g)


alice_shared_key = compute_shared_secret(bob_pub_key, alice_priv_key, p)
bob_shared_key = compute_shared_secret(alice_pub_key, bob_priv_key, p)

print("Prime (p): %s" % (p,))
print("Primitive Root (g): %s" % (g,))
print("Alice's private key: %s" % (alice_priv_key,))
print("Alice's public key: %s" % (alice_pub_key,))
print("Bob's private key: %s" % (bob_priv_key,))
print("Bob's public key: %s" % (bob_pub_key,))
print("Alice's shared key: %s" % (alice_shared_key,))
print("Bob's shared key: %s" % (bob_shared_key,))
print("Alice's shared key == Bob's shared key: %s" % (alice_shared_key == bob_shared_key,))
