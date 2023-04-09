"""
Nombre del Patrón: factory/factoría

Definición: Define un interfaz para crear un objeto, pero delega la decisión de la creación en subclases. Existe
un método factoría que tiene que ser implementado por las subclases.

Problema: Desarrollar una aplicación para crear pizzas en diferentes ciudades de la misma cadena

Uso: Permite extender la aplicación al delegar la creación de objetos en sublclases

Referencia: https://refactoring.guru/design-patterns/creational-patterns

"""
import abc

"""
Primero los tipos de objetos que vamos a crear
"""


class Pizza(metaclass=abc.ABCMeta):
    def __init__(self):
        self.name = ""
        self.dough = ""
        self.sauce = ""
        self.toppings = []

    def prepare(self):
        return "Preparing..." + str(self.toppings)

    def bake(self):
        return "Baking..."

    def cut(self):
        return "Cutting..."

    def box(self):
        return "Boxing..."

    def get_name(self):
        return self.name


class NYPizzaStyleCheese(Pizza):
    def __init__(self):
        super().__init__()
        self.name = "NYPizza Cheese"
        self.toppings.append("Margarina")


class NYPizzaStylePeperoni(Pizza):
    def __init__(self):
        super().__init__()
        self.name = "NYPizza Pepperoni"
        self.toppings.append("Margarina")


class CHPizzaStyle(Pizza):
    def __init__(self):
        super().__init__()
        self.name = "CHPizza"
        self.toppings.append("Tomatoe")


"""
Cramos las clases que crean los objetos, las factorías
"""


class PizzaStore(metaclass=abc.ABCMeta):
    def __init__(self):
        self.pizza = None

    def order_pizza(self, tipo: str):
        self.create_pizza(tipo)
        print(self.pizza.prepare())
        print(self.pizza.bake())
        print(self.pizza.cut())
        print(self.pizza.box())

    @abc.abstractmethod
    def create_pizza(self, tipo: str):
        pass


class NYPizzaStore(PizzaStore):
    def create_pizza(self, tipo: str):
        if tipo == "cheese":
            self.pizza = NYPizzaStyleCheese()
        elif tipo == "peperoni":
            self.pizza = NYPizzaStylePeperoni()
        else:
            self.pizza = NYPizzaStyleCheese()


class CHPizzaStore(PizzaStore):
    def create_pizza(self, tipo: str):
        self.pizza = CHPizzaStyle()


if __name__ == "__main__":
    nyf = NYPizzaStore()
    nyf.order_pizza("cheese")
    print(nyf.pizza.get_name())

    chf = CHPizzaStore()
    chf.order_pizza("")
    print(chf.pizza.get_name())
