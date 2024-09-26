"""
Este modulo contem a implementacao do Xorshift
"""


class Xorshift:

    name = "Xorshift"

    def __init__(self, state: int = 2**31 - 1, mod: int = None):
        """
        Inicia o gerador de numeros aleatorios

        Args:
            state (int): Valor inicial. 2**31-1 eh um primo bem legal.
            mod (int): Valor do mod, duh.
        """
        self.state = state
        self.mod = 2**31 - 1 if mod is None else mod

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
