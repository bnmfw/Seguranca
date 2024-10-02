from utils.modexp import modexp
from .PrimeTester import PrimeTester
from rng.RNG import RNG

report = False


class Miller(PrimeTester):
    name = "Miller Rabin"

    def __init__(self, generator: RNG, max_number: int, seed=None) -> None:
        super().__init__(generator=generator, max_number=max_number, seed=seed)

    def test(self, value: int) -> bool:

        if not value % 2:
            return False
        m = value - 1
        k = 0
        while not m % 2:
            k += 1
            m >>= 2
        if report:
            print(f"{value} = 2^{k}*{m}+1")

        a = self.randint(1, value - 1)

        if report:
            print(f"{a=}\t{m=}\t{value=}\t{modexp(a, m, value)=}")
        if modexp(a, m, value) == 1:
            return True

        for i in range(k):
            if report:
                print(f"\t{i=}\t{2**i*m=}\t{modexp(a, 2 ** i * m, value)=}")
            if modexp(a, 2**i * m, value) == value - 1:
                return True
        return False


if __name__ == "__main__":
    from .primes import primes_until
    from rng.Xorshift import Xorshift

    max_value = 10**4
    m = Miller(Xorshift, max_value)
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
