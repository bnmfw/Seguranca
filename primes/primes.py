"""
Implementa um algoritmo que calcula todos os primos ate n
"""


class Primes:
    def __init__(self) -> None:
        self.primes = [2, 3, 5, 7, 11, 13]

    def __call__(self, value) -> list:
        if value < self.primes[-1]:
            return self.primes

        for i in range(self.primes[-1] + 2, value + 1):
            is_prime = True
            for p in self.primes:
                if p * p > i:
                    break
                if not i % p:
                    is_prime = False
                    break
            if is_prime:
                self.primes.append(i)

        return self.primes


primes_until = Primes()

if __name__ == "__main__":
    print(primes_until(1000))
