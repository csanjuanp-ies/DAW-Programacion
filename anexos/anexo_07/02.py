"""
Nombre del Patrón: decorator/decorador

Definición: Añade responsabilidad adicional a un objeto de forma dinámica. Proporciona flexibilidad alternativa a la
herencia.

Problema: Desarrollar una aplicación para creación de cafés y sus condimientos

Uso: Por sí solo no se suele utilizar, junto a otros patrones: Factoría o Constructor

Referencia: https://refactoring.guru/design-patterns/creational-patterns

"""
import abc


class Bebida(metaclass=abc.ABCMeta):
    def __init__(self):
        self._descripcion = "Bebida desconocida"

    def get_descripcion(self):
        return self._descripcion

    @abc.abstractmethod
    def coste(self):
        pass


class DecoradorBebidas(Bebida, metaclass=abc.ABCMeta):  # Al ser también abstracta evitamos implementar coste
    def __init__(self):
        super().__init__()
        self._bebida = None

    @abc.abstractmethod
    def get_descripcion(self):
        pass


# Creamos varias bebidas para nuestro cafe
class Expreso(Bebida):
    def __init__(self):
        super().__init__()
        self._descripcion = "Expreso"

    def coste(self):
        return 1.99


class HouseBlend(Bebida):
    def __init__(self):
        super().__init__()
        self._descripcion = "House Blend"

    def coste(self):
        return 0.89


# Creamos varios condimientos para los cafés
class Mocka(DecoradorBebidas):
    def __init__(self, bebida):
        super().__init__()
        self._bebida = bebida

    def get_descripcion(self):
        return self._bebida.get_descripcion() + ", Mocka"

    def coste(self):
        return self._bebida.coste() + 0.20


class Soy(DecoradorBebidas):
    def __init__(self, bebida):
        super().__init__()
        self._bebida = bebida

    def get_descripcion(self):
        return self._bebida.get_descripcion() + ", Spy"

    def coste(self):
        return self._bebida.coste() + .40


class App:
    @staticmethod
    def run():
        # Un expreso solo
        bebida_1 = Expreso()
        print(bebida_1.get_descripcion(), bebida_1.coste())

        # Un HouseBlend con doble de Mocka y Soy
        bebida_2 = HouseBlend()
        bebida_2 = Mocka(bebida_2)
        bebida_2 = Mocka(bebida_2)
        bebida_2 = Soy(bebida_2)
        print(bebida_2.get_descripcion(), bebida_2.coste())


App.run()
