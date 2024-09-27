from utils.modexp import modexp
from .PrimeTester import PrimeTester

report = False


class Fermat(PrimeTester):
    name = "Fermat"

    def __init__(self, generator, max_number: int) -> None:
        super().__init__(generator=generator, max_number=max_number)

    def test(self, value: int) -> bool:

        a = self.randint(1, value - 1)
        return modexp(a, value - 1, 1) != 1


if __name__ == "__main__":
    from .primes import primes_until
    from rng.Xorshift import Xorshift

    max_value = 10**4
    m = Fermat(Xorshift, max_value)
    tests = 40
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
