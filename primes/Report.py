from .Miller import Miller
from .Solovay import Solovay
from .PrimeTester import PrimeTester
from rng.Xorshift import Xorshift
from rng.RNG import RNG
from rng.randint import Randint
from utils.Time import Crono


def relatorio(
    checker1: PrimeTester,
    checker2: PrimeTester,
    engine: RNG,
    bits: list[int],
    tests: int = 1,
    samples: int = 10**6,
):
    print(f"{'='*70}")
    print(f"\nRelatorio de Qualidade do {checker1.name} vs {checker2.name}:")
    print(f"\nAmostras={samples:.0e}")

    for bit in bits:
        print(f"\n[BITS={bit}]")

        seed: int = 2**bit - bit * 400  # Tanto faz
        c1: PrimeTester = checker1(engine, 2**bit, seed=seed)
        c2: PrimeTester = checker2(engine, 2**bit, seed=seed)
        rng: Randint = Randint(engine, max_number=2**bit, seed=seed)

        disagree: list = []

        # Primos grandes so podem ser 6k-1 ou 6k+1, nao vale a pena ir de 2 em 2, eu vou de 6 em 6 e olho o antecessor e sucessor

        with Crono() as cronometer:
            rand: int = rng(2 ** (bit - 1), 2**bit)

            # Rand vira um abaixo de multiplo de 6
            rand -= rand % 6
            rand -= 1
            is_prime_1, is_prime_2 = False, False

            under = True
            while not (is_prime_2 and is_prime_1):

                is_prime_1 = c1.bulk_test(rand, tests)
                is_prime_2 = c2.bulk_test(rand, tests)

                rand += 2 if under else 4

                under = not under

        print(f"Tempo={cronometer.total:.2f} segundos" f"\t Primo={rand}")


if __name__ == "__main__":
    bits = [40, 56, 80, 128, 168, 224, 256, 512, 1024, 2048, 4096]
    relatorio(Miller, Solovay, Xorshift, bits, 100)
