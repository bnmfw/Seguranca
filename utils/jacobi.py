"""
Implementa o operador jacobiano (Copiei da wikipedia https://en.wikipedia.org/wiki/Jacobi_symbol#Implementation_in_C++)
"""


def jacobi(a: int, n: int):
    a %= n
    t = 1
    r: int
    while a:
        while not a % 2:
            a >>= 1
            r = n % 8
            if r == 3 or r == 5:
                t = -t
        r = n
        n = a
        a = r
        if a % 4 == n % 4 == 3:
            t = -t
        a %= n
    return t if n == 1 else 0


if __name__ == "__main__":
    assert jacobi(2, 7) == 1
    assert jacobi(2, 5) == -1
    assert jacobi(19, 45) == 1
    assert jacobi(8, 21) == -1
    assert jacobi(3, 11) == 1
    assert jacobi(3, 13) == 1
    assert jacobi(5, 9) == 1
    assert jacobi(10, 15) == 0
    assert jacobi(-1, 7) == -1
    assert jacobi(-3, 7) == 1
    assert jacobi(-2, 11) == 1
    assert jacobi(0, 5) == 0
    assert jacobi(1, 101) == 1
    assert jacobi(1, 77) == 1
    assert jacobi(12345, 67891) == -1
    assert jacobi(98765, 43211) == -1
