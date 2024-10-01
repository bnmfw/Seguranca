from statistics import stdev, mean
from math import sqrt
from .LFG import LFG
from .Xorshift import Xorshift
from utils.Time import Crono


def relatorio(generator, bits: list[int], samples: int = 10**6):
    print(f"{'='*70}")
    print(f"\nRelatorio de Qualidade do {generator.name}:")
    print(f"\nAmostras={samples:.0e}")

    for bit in bits:
        rand = generator(mod=2**bit)
        with Crono() as cronometer:
            data = [rand() for _ in range(samples)]

        print(f"\n[BITS={bit}]")
        print(
            f"Tempo={cronometer.total:.2f} segundos"
            f"\tRepeticoes={len(data)-len(set(data))}"
        )

        if bit > 512:
            print("Numeros grandes de mais para coletar estatisticas")
            continue
        media = mean(data)
        desvio = stdev(data)
        print(
            f"[MEDIA] ideal={rand.mod/2:.4e}\t"
            f"gerada={media:.4e}\t"
            f"erro={100*abs(rand.mod/2-media)/(rand.mod/2):.2f}%"
        )

        print(
            f"[STDEV] ideal={rand.mod/sqrt(12):.4e}\t"
            f"gerada={desvio:.4e}\t"
            f"erro={100*abs(rand.mod/sqrt(12)-desvio)/(rand.mod/sqrt(12)):.2f}%"
        )


if __name__ == "__main__":
    bits = [40, 56, 80, 128, 168, 224, 256, 512, 1024, 2048, 4096]
    relatorio(Xorshift, bits)
    relatorio(LFG, bits)
