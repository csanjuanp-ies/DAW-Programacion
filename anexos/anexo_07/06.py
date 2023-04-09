"""
Nombre del Patrón: Adaptador / Adapter

Definición - Adaptador: Convierte el interfa de una clase en otra interfaz para adaptar dos APIs diferentes. Hace que
dos clases que no podían trabajar juntas, ahora a través de esta clase adaptador sí.

Problema: Usar dos clases PErro y gato de la misma forma

Uso: Adaptar APIs

Referencia: https://refactoring.guru/design-patterns/creational-patterns

"""
import abc
# clases generadas por otros


class Perro:
    def ladrar(self):
        return "Ladrando..."


class Gato:
    def maullar(self):
        return "Maullando..."


# Implementación del patrón


class Animal(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def hacer_ruido(self):
        pass


class AdaptadorPerro(Animal):
    def __init__(self, objeto: Perro):
        self._obj = objeto

    def hacer_ruido(self):
        return self._obj.ladrar()

    def __getattr__(self, item):
        return self._obj.__getattribute__(item)


class AdaptadorGato(Animal):
    def __init__(self, objeto: Gato):
        self._obj = objeto

    def hacer_ruido(self):
        return self.maullar()

    def __getattr__(self, item):
        return self._obj.__getattribute__(item)


if __name__ == "__main__":
    for inx in [AdaptadorPerro(Perro()), AdaptadorGato(Gato())]:
        print(inx.hacer_ruido())
