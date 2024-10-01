"""
Este modulo contem a implementacao do Lagged Fibonacci Generator
"""


class LFG:

    name = "Lagged Fibonacci Generator"

    def __init__(
        self,
        small: int = 24,
        big: int = 55,
        seed: list[int] = None,
        mod: int = None,
    ) -> None:
        """
        Inicia o gerador de numeros aleatorios

        Args:
            small (int): offset menor.
            big (int): offset maior.
            state_queue (list[int]): lista de estados.
            mod (int): expoente do modulo da funcao. Usa 2**31-1 como padrao, que eh primo
        """
        assert big > small, f"l={big} deve ser maior que k={small}"
        self.small = small
        self.big = big
        self.mod = 2**31 - 1 if mod is None else mod
        if seed is None:
            seed = [((i + 3) ** i - i * 13) % mod for i in range(big)]
        self.state_queue = seed

    def __call__(self) -> int:
        """
        Gera um numero aleatorio

        Returns:
            int: um numero aleatorio
        """
        value = self.state_queue[-self.small] + self.state_queue[-self.big]
        value %= self.mod
        self.state_queue.pop(0)
        self.state_queue.append(value)
        return value


if __name__ == "__main__":
    from Report import relatorio

    bits = [40, 56, 80, 128, 168, 224, 256, 512, 1024, 2048, 4096]
    relatorio(LFG, bits)
