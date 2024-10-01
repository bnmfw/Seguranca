"""
Este modulo contem a implementacao do Xorshift
"""


class Xorshift:

    name = "Xorshift"

    def __init__(self, seed: int = None, mod: int = None):
        """
        Inicia o gerador de numeros aleatorios

        Args:
            state (int): Valor inicial.
            mod (int): Valor do mod, duh.
        """
        self.state = seed or 2**31 - 1
        self.mod = mod or 2**31 - 1

    def __call__(self) -> int:
        """
        Gera um numero aleatorio

        Returns:
            int: um numero aleatorio
        """
        self.state ^= self.state << 13
        self.state %= self.mod
        self.state ^= self.state >> 17
        self.state %= self.mod
        self.state ^= self.state << 5
        self.state %= self.mod
        return self.state


if __name__ == "__main__":
    from Report import relatorio

    bits = [40, 56, 80, 128, 168, 224, 256, 512, 1024, 2048, 4096]
    relatorio(Xorshift, bits)
