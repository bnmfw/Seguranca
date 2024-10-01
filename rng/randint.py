class Randint:
    """
    Gera um numero inteiro dado ranges. Eh importante notar que fazer
    numero_aleatorio % maior_numero
    nao mantem a distribuicao uniforme!
    """

    def __init__(self, generator, max_number: int = None, seed=None) -> None:
        self.gen = generator(mod=max_number, seed=seed)
        for _ in range(10):
            self.gen()

    def __call__(self, value1: int, value2: int = None) -> int:
        """
        Gera um numero aleatorio.
        Se value2 == None:
            [0, value1]
        Se não:
            [value1, value2]

        Returns:
            int: Numero aleatorio
        """
        low: int = 0 if value2 is None else value1
        high: int = value1 if value2 is None else value2

        # Gera um rand em [0 : rand_max]
        rand: int = self.gen()

        # Mapeia rand para [0 : rand_max * (high - low)]
        rand *= high - low

        rand_mapped = rand

        # Mapeia rand para [0 : (high - low)]
        rand_mapped //= self.gen.mod

        # Faz com que o truncamento anterior seja um arredondamento case necessario
        if abs((rand_mapped + 1) * self.gen.mod - rand) < abs(
            rand_mapped * self.gen.mod - rand
        ):
            rand_mapped += 1

        # Mapeia rand para [low : high]
        rand_mapped += low

        return rand_mapped


if __name__ == "__main__":
    from rng.Xorshift import Xorshift
    from statistics import stdev, mean
    from math import sqrt

    randint = Randint(Xorshift)

    samples = 10**6
    r = [5, 25]
    print(f"Distribuicao aleatorio de {samples:.0e} numeros entre {r[0]} e {r[1]}")
    data = [randint(*r) for _ in range(samples)]
    media = mean(data)
    desvio = stdev(data)
    print(
        f"[MEDIA] ideal={(r[1]-r[0])/2+r[0]:.2f}\t"
        f"gerada={media:.2f}\t"
        f"erro={100*abs((r[1]-r[0])/2+r[0]-media)/((r[1]-r[0])/2):.2f}%"
    )

    print(
        f"[STDEV] ideal={(r[1]-r[0])/sqrt(12):.2f}\t"
        f"gerada={desvio:.2f}\t"
        f"erro={100*abs((r[1]-r[0])/sqrt(12)-desvio)/((r[1]-r[0])/sqrt(12)):.2f}%"
    )
