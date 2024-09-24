"""
Este modulo contem a implementacao do Xorshift
"""
class Xorshift:
    
    name = "Xorshift"

    def __init__(self, state: int = 2**31-1, mod: int = 2**31-1):
        """
        Inicia o gerador de numeros aleatorios

        Args:
            state (int): Valor inicial. 2**31-1 eh um primo bem legal.
        """
        self.state = state
        self.mod = mod
    
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