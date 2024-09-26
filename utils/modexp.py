"""
Implementa exponenciacao modular (provavelmente) segura
"""


def modexp(base: int, power: int, mod: int):
    k = 20
    result = 1
    while power > k:
        result *= base**k
        result %= mod
        power -= k
    result *= base**power
    return result % mod
