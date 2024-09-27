from utils.modexp import modexp
from utils.jacobi import jacobi
from .primes import primes_until
from .PrimeTester import PrimeTester
from math import sqrt

report = False


class Solovay(PrimeTester):
    name = "Solovay"

    def __init__(self, generator, max_number: int) -> None:
        super().__init__(generator=generator, max_number=max_number)

    def test(self, value: int) -> bool:
        if value == 2:
            return True
        if not value % 2 or value < 3:
            return False
        a = self.randint(2, value - 1)
        j = jacobi(a, value)
        if j == 0:
            return False
        return modexp(a, (value - 1) // 2, value) == j % value


if __name__ == "__main__":
    from .primes import primes_until
    from rng.Xorshift import Xorshift

    max_value = 10**4
    m = Solovay(Xorshift, max_value)
    tests = 1
    is_prime = lambda v: m.bulk_test(v, tests)
    primos = set(primes_until(max_value))
    primes = [i for i in range(2, max_value) if is_prime(i)]

    print(f"Calculei que estes sao todos os primos ate {max_value}")
    for i, v in enumerate(primes):
        print(v, end="\t" if (i + 1) % 17 else "\n")
    print()

    print(f"\nEstes sao numeros que erroneamente assumi primos:")
    for i, v in enumerate(set(primes) - primos):
        print(v, end="\t" if (i + 1) % 17 else "\n")
    print()

    print(f"Tentativas de checagem de primaridade para cada primo = {tests}")
