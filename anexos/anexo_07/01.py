"""
Nombre del Patrón: observer/observador

Definición: Define una relación de uno a muchos entre objetos de tal manera que cuando el objeto de la relación uno
cambia su estado, todos los que dependen de él son notificados de dicho cambio.

Problema: Desarrollo de una estación meteorológica en la que el hardware detecta cambios y los comunica a través
de un evento al software. A ese software de recogida se le podrán añadir diferentes pantallas de visualización
que cambiarán automáticamente los datos cuando cambienlos del software de recogida.

Uso: Distribución de datos

Referencia: https://refactoring.guru/design-patterns/creational-patterns

"""
import abc
import random


class VisualizableInterfaz(metaclass=abc.ABCMeta):
    """
    Implementa las características básicas de todas las pantallas
    """
    @abc.abstractmethod
    def display(self):
        pass


class ObservadorInterfaz(metaclass=abc.ABCMeta):
    """
    El interfaz para todas las pantallas que quieren ser notificadas
    """
    @abc.abstractmethod
    def update(self, msg):
        pass


class ObservadoInterfaz(metaclass=abc.ABCMeta):
    """
    El interfaz del software que va a recibir los cambios de los datos y gestionar el traslado de los mismos a otras
    partes del código
    """
    @abc.abstractmethod
    def set_observador(self, obs):
        pass

    @abc.abstractmethod
    def remove_observador(self, obs):
        pass

    @abc.abstractmethod
    def notify(self):
        pass


class DatosDelTiempo(ObservadoInterfaz):
    def __init__(self):
        self._lista_observadores = []
        self._valor = None

    def set_observador(self, obs):
        self._lista_observadores.append(obs)

    def remove_observador(self, obs):
        self._lista_observadores.remove(obs)

    def notify(self):
        for ele in self._lista_observadores:
            ele.update(self._valor)

    def set_valor(self, valor):
        self._valor = valor
        self.notify()

    def event_cambio_condiciones(self):
        """
        Este evento se llamaría desde el hardware externo cuando los sensores detecten un cambio en el tiempo
        """
        # Esta línea simula los datos, en la realidad este evento se lanzaría automáticamente y solo
        # se recogerían los datos del sensor uy se trasladarían mediante set_valor.
        self.set_valor(random.randint(1, 100))


class CondicionesActuales(ObservadorInterfaz, VisualizableInterfaz):
    """
    Una pantalla con las condiciones actuales
    """
    def __init__(self):
        self._msg = None

    def update(self, msg):
        self._msg = msg

    def display(self):
        print(f"Condiciones Actuales: {self._msg}")


class Estadisticas(ObservadorInterfaz, VisualizableInterfaz):
    """
    Una pantalla con las estadísticas de los últimos días
    """
    def __init__(self):
        self._msg = None

    def update(self, msg):
        self._msg = msg

    def display(self):
        print(f"Estadísticas: {self._msg}")


if __name__ == "__main__":
    # Creación de los sensores y dispositivos que traten los datos
    datos_de_tiempo_sensor = DatosDelTiempo()
    cond_actual = CondicionesActuales()
    estadisticas = Estadisticas()
    datos_de_tiempo_sensor.set_observador(cond_actual)
    datos_de_tiempo_sensor.set_observador(estadisticas)
    print("=" * 80)
    # Se ha producido un cambio de datos
    datos_de_tiempo_sensor.event_cambio_condiciones()
    cond_actual.display()
    estadisticas.display()
    print("=" * 80)
    # Se ha producido un cambio de datos
    datos_de_tiempo_sensor.event_cambio_condiciones()
    cond_actual.display()
    estadisticas.display()
    print("=" * 80)
    print("Condiciones actuales ya no observan")
    datos_de_tiempo_sensor.remove_observador(cond_actual)
    datos_de_tiempo_sensor.event_cambio_condiciones()
    cond_actual.display()
    estadisticas.display()
    # Liberación de recursos, no es necesario pero para proyectos hardware mejor asegurarse
    del cond_actual
    del estadisticas
    del datos_de_tiempo_sensor
