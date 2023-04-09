"""
Nombre del Patrón: Proxy / Proxy

Definición: Proporciona un mecanismo de subrogación a otro objeto para controlar el acceso

Problema:

Uso: Controlar el acceso a clases desde otras

Referencia: https://refactoring.guru/design-patterns/creational-patterns

"""
from abc import ABC, abstractmethod


class Subject(ABC):
    """
    La interfaz Asunto declara operaciones comunes para RealSubject y
    el apoderado. Siempre que el cliente trabaje con RealSubject usando esta
    interfaz, podrá pasarle un proxy en lugar de un sujeto real.
    """
    @abstractmethod
    def request(self) -> None:
        pass


class RealSubject(Subject):
    """
    El RealSubject contiene cierta lógica comercial central. Por lo general, RealSubjects son
    capaz de hacer algún trabajo útil que también puede ser muy lento o sensible -
    p. ej. corregir los datos de entrada. Un Proxy puede resolver estos problemas sin ningún
    cambio en el código de RealSubject.
    """
    def request(self) -> None:
        print("RealSubject: Handling request.")


class Proxy(Subject):
    def __init__(self, real_subject):
        self._real_subject = real_subject

    def request(self) -> None:
        """
        Las aplicaciones más comunes del patrón Proxy son la carga diferida,
        almacenamiento en caché, control de acceso, registro, etc. Un Proxy puede realizar una
        de estas cosas y luego, dependiendo del resultado, pasar la ejecución
        al mismo método en un objeto RealSubject vinculado.
        """

        if self.check_access():
            self._real_subject.request()
            self.log_access()

    def check_access(self):
        print("Proxy: Checking access prior to firing a real request.")
        return True

    def log_access(self):
        print("Proxy: Logging the time of request.", end="")


def client_code(subject: Subject):
    """
    Se supone que el código del cliente funciona con todos los objetos (tanto sujetos como
    proxies) a través de la interfaz Asunto para admitir ambos sujetos reales
    y apoderados. En la vida real, sin embargo, los clientes trabajan principalmente con sus verdaderos
    sujetos directamente. En este caso, para implementar el patrón más fácilmente,
    puede extender su proxy de la clase del sujeto real.
    """
    subject.request()


if __name__ == "__main__":
    print("Client: Executing the client code with a real subject:")
    real_subject = RealSubject()
    client_code(real_subject)

    print("")

    print("Client: Executing the same client code with a proxy:")
    proxy = Proxy(real_subject)
    client_code(proxy)
