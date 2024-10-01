"""
Manejador de contexto pra contar o tempo mais tolo do mundo
"""

from time import process_time


class Crono:
    def __enter__(self):
        self.total = process_time()
        return self

    def __exit__(self, i, hate, error_handling):
        self.total = process_time() - self.total


if __name__ == "__main__":
    from time import sleep

    with Crono() as cronometer:
        sleep(10)
    print(cronometer.total)
    print("Esse teste eh engracado por que sleep n afeta o process time")
