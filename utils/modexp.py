"""
Implementa exponenciacao modular rapida
"""

def modexp(base, exp, mod):
    result = 1
    base = base % mod 
    while exp > 0:
        
        if exp % 2:
            result = (result * base) % mod
        
        base = (base * base) % mod
        exp //= 2
    
    return result
