"""
Classe abstrata de RNG
"""

from abc import ABC, abstractmethod


class RNG(ABC):

    name = "RNG"

    @abstractmethod
    def __init__(self, seed: int = None, mod: int = None):
        """
        Inicia o gerador de numeros aleatorios

        Args:
            seed (int): Valor inicial. 2**31-1 eh um primo bem legal.
            mod (int): Valor do mod, duh.
        """
        pass

    @abstractmethod
    def __call__(self) -> int:
        """
        Gera um numero aleatorio

        Returns:
            int: um numero aleatorio
        """
        pass
