"""
Nombre del Patrón: command/comando

Definición: Encapsula una petición como un objeto, permitiendo parametrizar a los clientes diferentes peticiones,
colas o logs y permite deshacer operaciones.

Problema: Creación de un control remoto para diversos aparatos

Uso: Crear comandos/operaciones

Referencia: https://refactoring.guru/design-patterns/creational-patterns

"""
import abc


class Luz:
    def __init__(self, nombre):
        self._encendido = False
        self._nombre = nombre

    def on(self):
        self._encendido = True
        return f"Luz {self._nombre} encendida..."

    def off(self):
        self._encendido = False
        return f"Luz {self._nombre} apagada..."


class Command(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def execute(self):
        pass

    @abc.abstractmethod
    def undo(self):
        pass


class EncenderLuz(Command):
    def __init__(self, luz):
        self.luz = luz

    def execute(self):
        return self.luz.on()

    def undo(self):
        return self.luz.off()


class ApagarLuz(Command):
    def __init__(self, luz):
        self.luz = luz

    def execute(self):
        return self.luz.off()

    def undo(self):
        return self.luz.on()


if __name__ == "__main__":
    class ControlRemoto:
        def __init__(self):
            self._slot = []
            luz_salon = Luz("Luz salón")
            self._slot.append(EncenderLuz(luz_salon))
            self._slot.append(ApagarLuz(luz_salon))
            self._undo = None

        def set_comando(self, slot, comando):
            self._slot[slot] = comando

        def run_comando(self, slot):
            if slot < len(self._slot):
                self._undo = self._slot[slot]
                return self._slot[slot].execute()
            return "No existe el slot"

        def undo(self):
            return self._undo.undo()


    cr = ControlRemoto()
    print(cr.run_comando(0))
    print(cr.run_comando(1))
    print(cr.run_comando(2))
    print(cr.undo())
