"""
Implementa exponenciacao modular (provavelmente) segura
"""


def modexp(base, exp, mod):
    result = 1
    base = base % mod  # Take mod of base to simplify the computation
    while exp > 0:
        # If exp is odd, multiply base with the result
        if exp % 2 == 1:
            result = (result * base) % mod
        # Square the base and halve the exponent
        base = (base * base) % mod
        exp //= 2
    return result
