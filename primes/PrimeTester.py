"""
Prime tester base class
"""

from rng.randint import Randint
from rng.RNG import RNG

report = False


class PrimeTester:
    name = "Abstract Tester"

    def __init__(self, generator: RNG, max_number: int, seed=None) -> None:
        """
        Args:
            generator (RNG): RNG engine
            max_number (int): Maior numero checavel
            seed (int or list[int]): seed, depende da RNG engine
        """

        self.randint = Randint(generator=generator, max_number=max_number, seed=seed)

    def test(self, value: int) -> bool:
        """
        Testa se um determinado numero eh primo

        Args:
            value (int): valor a ser testado

        Returns:
            bool: se o valor eh provavelmente primo
        """
        pass

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
