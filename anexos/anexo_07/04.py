"""
Nombre del Patrón: singleton/singleton

Definición: Define una interfaz de tal manera que solo se puede tener una única instancia de la clase

Problema: Por ejemplo las configuraciones de una aplicación

Uso: Mantener una única instancia de un objeto.

Referencia: https://refactoring.guru/design-patterns/creational-patterns

"""


class Singleton:
    __instance = None
    __value = 0

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def __str__(self):
        return "Mi Objeto: " + str(self.__value)

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, val: int):
        self.__value = val

    @classmethod
    def get_instance(cls):
        return cls.__instance


if __name__ == "__main__":
    miObjeto1 = Singleton()
    print(miObjeto1)        # 0
    miObjeto2 = Singleton()
    miObjeto2.value = 5
    print(miObjeto1)        # 5
    print(Singleton.get_instance().value)   # 5
    print(id(miObjeto1))  # Debería mostrar el mismo id los dos objetos
    print(id(miObjeto2))
