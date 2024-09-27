from .Miller import Miller
from .Fermat import Fermat
from rng.Xorshift import Xorshift
from .Solovay import Solovay
from time import process_time


def relatorio(checker1, checker2, engine, bits: list[int], samples: int = 10**6):
    print(f"{'='*70}")
    print(f"\nRelatorio de Qualidade do {checker1.name} vs {checker2.name}:")
    print(f"\nAmostras={samples:.0e}")

    for bit in bits:
        print(f"\n[BITS={bit}]")
        disagree = []

        c1 = checker1(engine, 2**bit)
        c2 = checker2(engine, 2**bit)
        rng = engine(mod=2**bit)
        start_time = process_time()
        for _ in range(samples):
            v = rng()
            if not v % 2:
                v += 1
            c1v = c1.test(v)
            c2v = c2.test(v)
            if c1v != c2v:
                disagree.append((c1v, v))
        end_time = process_time()

        print(f"Tempo={end_time-start_time:.2f} segundos")

        if not disagree:
            print("Ambos Testes concordam sobre a primalidade de todos so numeros!")
            continue

        print("Numero que os testadores discoradam:")
        print(checker1.name.ljust(15), checker2.name.ljust(15), "Numero")
        for c1, n in disagree:
            print(
                ("PRIME" if c1 else "NOT PRIME").ljust(15),
                ("NOT PRIME" if c1 else "PRIME").ljust(15),
                n,
            )


if __name__ == "__main__":
    bits = [40, 56, 80, 128, 168, 224, 256, 512, 1024, 2048, 4096]
    relatorio(Miller, Solovay, Xorshift, bits, 100)
