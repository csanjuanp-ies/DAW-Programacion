"""
Nombre del Patrón: State / Estado

Definición: Permite a un objeto cambiar su propio comportamiento cuando el estado interno cambia.

Problema: Grafo con dos nodos A, B interconectados con dos flechas A->B y B->A

Uso: Definición de gráfos de comportamiento

Referencia: https://refactoring.guru/design-patterns/creational-patterns

"""
from abc import ABC, abstractmethod


class Context:
    """
    El Contexto define la interfaz de interés para los clientes. También mantiene
    una referencia a una instancia de una subclase de estado, que representa el estado actual
    estado del Contexto.
    """

    _state = None

    def __init__(self, state) -> None:
        self.transition_to(state)

    def transition_to(self, state):
        print(f"Context: Transition to {type(state).__name__}")
        self._state = state
        self._state.context = self

    def request1(self):
        self._state.handle1()

    def request2(self):
        self._state.handle2()


class State(ABC):
    """
    La clase base State declara métodos que ConcreteState debería
    implementar y también proporciona una referencia inversa al objeto Contexto,
    asociado al Estado. Esta referencia inversa puede ser utilizada por los Estados para
    transición del Contexto a otro Estado.
    """

    def __init__(self):
        self._context = None

    @property
    def context(self) -> Context:
        return self._context

    @context.setter
    def context(self, context) -> None:
        self._context = context

    @abstractmethod
    def handle1(self) -> None:
        pass

    @abstractmethod
    def handle2(self) -> None:
        pass


class ConcreteStateA(State):
    def handle1(self) -> None:
        print("ConcreteStateA handles request1.")
        print("ConcreteStateA wants to change the state of the context.")
        self.context.transition_to(ConcreteStateB())

    def handle2(self) -> None:
        print("ConcreteStateA handles request2.")


class ConcreteStateB(State):
    def handle1(self) -> None:
        print("ConcreteStateB handles request1.")

    def handle2(self) -> None:
        print("ConcreteStateB handles request2.")
        print("ConcreteStateB wants to change the state of the context.")
        self.context.transition_to(ConcreteStateA())


if __name__ == "__main__":
    context = Context(ConcreteStateA())
    context.request1()
    context.request2()
