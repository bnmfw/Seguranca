from rng.Xorshift import Xorshift
from rng.LFG import LFG
from rng.randint import Randint
from utils.modexp import modexp
from primes.primes import primes_until

report = False


class Miller:
    name = "Miller Rabin"

    def __init__(self, generator) -> None:
        """
        Args:
            generator (LFG or Xorshift): RNG engine
        """

        self.randint = Randint(generator=generator)

    def test(self, value: int) -> bool:
        """
        Testa se um determinado numero eh primo

        Args:
            value (int): valor a ser testado

        Returns:
            bool: se o valor eh provavelmente primo
        """

        m = value - 1
        k = 0
        while not m % 2:
            k += 1
            m //= 2
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

    def bulk_test(self, value: int, runs: int) -> bool:
        """
        Testa o valor varias vezes para as diferentes

        Args:
            value (int): valor a ser testado
            runs (int): numero de testes
        """
        for _ in range(runs):
            if not self.test(value):
                return False
        return True


if __name__ == "__main__":
    m = Miller(Xorshift)
    tests = 2
    is_prime = lambda v: m.bulk_test(v, tests)
    max_value = 10**4
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
