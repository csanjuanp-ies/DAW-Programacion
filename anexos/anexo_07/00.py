"""
Nombre del Patrón: strategy/estrategia

Definición: Define una familia de algoritmos, encapsulados de forma separada, y hace que sean intercambiables.
Permite que el algoritmo varía independientemente de quién lo use.

Problema: A veces la herencia nos obliga a reescribir mucho código al sobresciribir métodos, tras un análisis
más detallado, podemos aislar lo que varía en clases separadas haciéndolas intercambiables

Uso: Relaciones de composición, permite cambiar el comportamiento durante la ejecución

Referencia: https://refactoring.guru/design-patterns/creational-patterns

"""
from abc import ABC, abstractmethod


class FlyBehaviour(ABC):
    """
    Aisla los comportamientos de volar, esta clase abstracta sirve de interfaz en otros lenguales
    """
    @abstractmethod
    def fly(self):
        pass


class FlyWithWings(FlyBehaviour):
    """
    Un comportamiento de volar, volar con alas
    """
    def fly(self):
        return "Fly"


class FlyNoWay(FlyBehaviour):
    """
    Otro comportamiento de volar, en este caso no vuela
    """
    def fly(self):
        return "No Fly"


class QuackBehaviour(ABC):
    """
    Aisla los comportamientos de Hacedr Cuac, esta clase abstracta sirve de interfaz en otros lenguales
    """
    @abstractmethod
    def quack(self):
        pass


class Quack(QuackBehaviour):
    """
    Un comportamiento de hacer cuac
    """
    def quack(self):
        return "Quack"


class Duck(ABC):
    """
    Esta clase modela lo general de un pato
    """
    def __init__(self):
        self._fly_behavior: FlyBehaviour | None = None
        self._quack_behavior: QuackBehaviour | None = None

    def perfom_fly(self):
        return self._fly_behavior.fly()

    def perfom_quack(self):
        return self._quack_behavior.quack()

    @staticmethod
    def swin():
        return "Swin"

    @abstractmethod
    def __str__(self):
        pass

    @property
    def fly(self):
        return self._fly_behavior

    @fly.setter
    def fly(self, fb: FlyBehaviour):
        self._fly_behavior = fb


class MallardDuck(Duck):
    """
    Un tipo de pato
    """
    def __init__(self):
        super().__init__()
        self._fly_behavior = FlyWithWings()
        self._quack_behavior = Quack()

    def __str__(self):
        return "Mallar Duck"


class ModelDuck(Duck):
    """
    Otro tipo de pato
    """
    def __init__(self):
        super().__init__()
        self.__fly_behavior = FlyNoWay()
        self._quack_behaviour = Quack()

    def __str__(self):
        return "Model Duck"


if __name__ == "__main__":
    mallar = MallardDuck()
    print(mallar.swin())
    print(mallar.perfom_fly())
    print(mallar.perfom_quack())
    mallar.fly = FlyNoWay()  # Cambiamos el comportamiento en ejecución de mallar
    print(mallar.perfom_fly())
