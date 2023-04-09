"""
Nombre del Patrón: Iterator / Iterador

Definición: Proporciona un mecanismo para acceder a los elementos internos de forma secuencial

Problema: Devolver los números impares. Es fácilmente extendible a cualquier tipo de objeto compuesto

Uso: de la clase en las estructuras de control de bucles

Referencia: https://refactoring.guru/design-patterns/creational-patterns

"""


class NumerosImparesIterador(object):
    def __init__(self, container):
        self.container = container
        self.n = -1

    def __next__(self):
        self.n += 2
        if self.n > self.container.maximum:
            raise StopIteration
        return self.n

    def __iter__(self):
        return self


class NumerosImpares(object):
    def __init__(self, maximum):
        self.maximum = maximum

    def __iter__(self):
        return NumerosImparesIterador(self)



if __name__ == "__main__":
    numbers = NumerosImpares(7)

    for n in numbers:
        print(n)
