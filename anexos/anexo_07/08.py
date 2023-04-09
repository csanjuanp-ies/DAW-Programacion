"""
Nombre del Patrón: Template / Plantilla

Definición: Proporciona un esqueleto para un algoritmo en un método, difiere algunos pasos del algoritmo a las
sublclases. Permite a las subclases redefoinir ciertos pasos del algortimo sin cambiar la estructura del mismo

Problema: Modelado de preparar cafes / tee

Uso: Desacoplar la lógica del algortimo de la implementación del mismo.

Referencia: https://refactoring.guru/design-patterns/creational-patterns

"""
import abc
from typing import final


class Bebida(metaclass=abc.ABCMeta):
    @final
    def servir_bebida(self):
        """
        Este es el agoritmo que vamos a implementar
        """
        self.hervir_agua()
        self.elaborar()
        self.poner_en_vaso()
        if self.cliente_quiere_condimentos():
            self.add_condimentos()

    def hervir_agua(self):
        print("Hirviendo")

    def poner_en_vaso(self):
        print("Poniendo en vaso...")

    @abc.abstractmethod
    def elaborar(self):
        pass

    @abc.abstractmethod
    def add_condimentos(self):
        pass

    def cliente_quiere_condimentos(self):
        return True


class Caffe(Bebida):
    #  No evita que se sobrescriba, solo lo marca
    #  def servir_bebida(self):
    #     pass

    def elaborar(self):
        print("Elaborando Caffe")

    def add_condimentos(self):
        print("Añadiendo Leche y/o Azucar")

    def cliente_quiere_condimentos(self):
        leche = input("¿Quiere Leche (S/N)?").upper()
        azucar = input("¿Quiere Azucar (S/N)?").upper()
        if leche == 'S' or azucar == 'S':
            return True
        else:
            return False


class Te(Bebida):
    def elaborar(self):
        print("Elaborando Té")

    def add_condimentos(self):
        print("Añadiendo Limón")


if __name__ == "__main__":
    te = Te()
    te.servir_bebida()
    cafe = Caffe()
    cafe.servir_bebida()
