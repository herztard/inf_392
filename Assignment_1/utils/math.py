import random

def gcd(a, b):
    """Compute the greatest common divisor of a and b."""
    while b:
        a, b = b, a % b
    return a

def extended_gcd(a, b):
    """Extended Euclidean Algorithm."""
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = extended_gcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    """Compute the modular inverse of a modulo m."""
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % m

def is_prime(n, k=128):
    """Test if a number is prime."""
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False
    # Rabin-Miller primality test
    s = 0
    d = n - 1
    while d % 2 == 0:
        d //= 2
        s += 1
    for _ in range(k):
        a = random.randint(2, n - 1)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def factorize(n):
    """Factorize n and return its factors."""
    factors = []
    # Handle even numbers
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    # Handle odd factors
    i = 3
    while i * i <= n:
        while n % i == 0:
            factors.append(i)
            n //= i
        i += 2
    if n > 2:
        factors.append(n)
    return factors

def find_primitive_root(p):
    """Find a primitive root for prime p."""
    if p == 2:
        return 1
    phi = p - 1
    factors = set(factorize(phi))
    for g in range(2, phi + 1):
        if all(pow(g, phi // f, p) != 1 for f in factors):
            return g
    return None
