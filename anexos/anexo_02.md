# Anexo 2
## Faqs
### POO avanzado
#### Propiedades de clase
Una propiedad de clase es aquella definida en el ámbito de la clase y es común a todas las 
instancias que creemos. Para acceder utilizaremos el nombre de clase o el nombre del objeto 
o instancia. 
Si accedemos a la variable de clase a través del nombre del objeto y la modificamos, crearemos 
una nueva variable de instancia con el mismo nombre en dicho objeto exclusivamente, no en los 
demás, quedando expuesta a los demás objetos como variable de clase. 
```
class Coche:
    numero_instancias = 0  # variable de clase

    def __init__(self, matricula, color):
        self.matricula = matricula  # Variables de instancia
        self.color = color  # Variable de instancia
        Coche.numero_instancias += 1  # Acceso a variable clase

    def __str__(self):
        return f"{self.matricula}-{self.color}",
 		     "(Clase:{Coche.numero_instancias})"

    def __repr__(self):
        return self.__str__()


c1 = Coche("ABC-1900", "rojo")
print(f"{c1=}")
c2 = Coche("XYZ-5600", "verde")
print(f"{c1=}")
print(f"{c2=}")

Coche.numero_instancias = 5  # Se accede a la de clase
print(f"{c1=}")
print(f"{c2=}")

c1.numero_instancias = 7  # se crea una de instancia en c1
print(f"{c1=}")
print(f"{c2=}")  
print(f"{c1.numero_instancias=}")
print(f"{c2.numero_instancias=}")  # Accedemos la la de clase
Coche.numero_instancias = 5 
print(f"{c1.numero_instancias=}")
print(f"{c2.numero_instancias=}")
```


***Resultado***
```
C:/Python/Proyectos/pruebas/a.py
c1=ABC-1900 - rojo (Clase:1)
c1=ABC-1900 - rojo (Clase:2)
c2=XYZ-5600 - verde (Clase:2)
c1=ABC-1900 - rojo (Clase:5)
c2=XYZ-5600 - verde (Clase:5)
c1=ABC-1900 - rojo (Clase:5)
c2=XYZ-5600 - verde (Clase:5)
c1.numero_instancias=7
c2.numero_instancias=5
c1.numero_instancias=7
c2.numero_instancias=5
```

**¿Cómo invoco a un método definido en una clase base desde una clase derivada que lo ha 
sobrescrito?**

Usa la función incorporada super():
```
class Derived(Base):
    def meth(self):
        super(Derived, self).meth()
```
### Iteradores
Se presenta un problema potencial al crear un iterador sobre una estructura de datos si devolvemos la propia estructura 
de datos como el iterador en vez de una clase nueva que gestione los datos. 
Si entregamos la propia estructura y creamos varios iteradores, todos compartirán el estado siendo unos dependientes 
de otros.
```
class Dias:
    def __init__(self):
        self.dias = ["L", "M", "X", "J", "V"]

    def __iter__(self):
        self._index = 0
        return self

    def __next__(self):
        if self._index < 0  or self._index > len(self.dias):
            raise StopIteration
        else:
            ret = self.dias[self._index]
            self._index += 1
        return ret


dias = Dias()
iter_uno = iter(dias)
iter_dos = iter(dias)
print(next(iter_uno))  # L
print(next(iter_dos))  # M
```

En el ejemplo anterior vemos como ambos iteradores comparten estado, ya que el comportamiento esperado es que el segundo 
empiece también en L, no sigua por la M del primero.

```
class Dias:
    def __init__(self):
        self.dias = ["L", "M", "X", "J", "V"]

    def __iter__(self):
        return DiasIterador(self.dias)


class DiasIterador:
    def __init__(self, values):
        self.dias = values
        self._index = 0

    def __next__(self):
        if self._index < 0  or self._index > len(self.dias):
            raise StopIteration
        else:
            ret = self.dias[self._index]
            self._index += 1
        return ret


dias = Dias()
iter_uno = iter(dias)
iter_dos = iter(dias)
print(next(iter_uno))  # L
print(next(iter_dos))  # L
```

### Varios
#### ¿Por qué los valores por defecto se comparten entre objetos?
Considera esta función:
```
def foo(key, value, mydict={}):
    # Danger: el diccionario se comparte entre llamadas
    mydict[key] = value
    return mydict

print(foo(5, 3))
print(foo(6, 3))

# {5: 3}
# {5: 3, 6: 3} Guarda el resultado anterior entre llamadas
```
La primera vez que llamas a esta función, mydict solamente contiene un único elemento. La segunda vez, mydict contiene 
dos elementos debido a que cuando comienza la ejecución de foo(6, 3), mydict comienza conteniendo un elemento de 
partida.
A menudo se esperaría que una invocación a una función cree nuevos objetos para valores por defecto. Eso no es lo que 
realmente sucede. Los valores por defecto se crean exactamente una sola vez, cuando se define la función. Si se 
cambia el objeto, como el diccionario en este ejemplo, posteriores invocaciones a la función estarán referidas al 
objeto cambiado.
Por definición, los objetos inmutables como números, cadenas, tuplas y None están asegurados frente al cambio. Cambios 
en objetos mutables como diccionarios, listas e instancias de clase pueden llevar a confusión.
Debido a esta característica es una buena práctica de programación el no usar valores mutables como valores por 
defecto. En su lugar usa None como valor por defecto dentro de la función, comprueba si el parámetro es None y crea 
una nueva lista/un nuevo diccionario/cualquier otra cosa que necesites. Por ejemplo:

No usar:
```
def foo(mydict={}):
    ...
```
Pero sí:
```
def foo(mydict=None):
    if mydict is None:
       mydict = {} # create a new dict for local namespace
```

#### ¿Cuál es la forma más eficiente de concatenar muchas cadenas conjuntamente?
Los objetos str y bytes son inmutables, por tanto, concatenar muchas cadenas en una sola es ineficiente debido a que 
cada concatenación crea un nuevo objeto. En el caso más general, el coste total en tiempo de ejecución es cuadrático 
en relación con la longitud de la cadena final.
Para acumular muchos objetos str, la forma recomendada sería colocarlos en una lista y llamar al método str.join() 
al final:
```
chunks = []
for s in my_strings:
    chunks.append(s)
result = ''.join(chunks)
```

#### ¿Cómo puedo crear una lista multidimensional?
Seguramente hayas intentado crear un array multidimensional de la siguiente forma:
```
A = [[None] * 2] * 3
```
Esto parece correcto si lo muestras en pantalla:
```
print(A)
# [[None, None], [None, None], [None, None]]
```
Pero cuando asignas un valor, se muestra en múltiples sitios:
```
A[0][0] = 5
print(A)
# [[5, None], [5, None], [5, None]]
```

La razón es que replicar una lista con * no crea copias, solo crea referencias a los objetos existentes. El *3 crea 
una lista conteniendo 3 referencias a la misma lista de longitud dos. Cambios a una fila se mostrarán en todas las 
filas, lo cual, seguramente, no es lo que deseas.
El enfoque recomendado sería crear, primero, una lista de la longitud deseada y, después, rellenar cada elemento 
con una lista creada en ese momento:
```
A = [None] * 3
for i in range(3):
     A[i] = [None] * 2
```
Esto genera una lista conteniendo 3 listas distintas de longitud dos. También puedes usar una comprensión de lista:
```
w, h = 2, 3
A = [[None] * w for i in range(h)]
```

#### ¿Por qué list.sort() no devuelve la lista ordenada?
En situaciones donde el rendimiento es importante, hacer una copia de la lista solo para ordenarlo sería un 
desperdicio. Por lo tanto, list.sort() ordena la lista en su lugar. Para recordar este hecho, no devuelve la lista 
ordenada. De esta manera, no se dejará engañar por sobrescribir accidentalmente una lista cuando necesite una copia 
ordenada, pero también deberá mantener la versión sin ordenar.
Si desea crear una nueva lista, use la función incorporada sorted() en su lugar. Esta función crea una nueva lista a 
partir de un iterativo proporcionado, la ordena y la retorna. 



#### Polimorfismo
Por defecto Python no implementa el polimorfismo en los métodos, con la siguiente estructura es posible
```
# person.py
 
 from datetime import date
 from functools import singledispatchmethod
 
 class BirthInfo:
     @singledispatchmethod
     def __init__(self, birth_date):
         raise ValueError(f"No soportado: {birth_date}")

    @__init__.register(date)
    def _from_date(self, birth_date):
        self.date = birth_date

    @__init__.register(str)
    def _from_isoformat(self, birth_date):
        self.date = date.fromisoformat(birth_date)

    @__init__.register(int)
    @__init__.register(float)
    def _from_timestamp(self, birth_date):
        self.date = date.fromtimestamp(birth_date)

    def age(self):
        return date.today().year - self.date.year
class Person:
    def __init__(self, name, birth_date):
        self.name = name
        self._birth_info = BirthInfo(birth_date)

    @property
    def age(self):
        return self._birth_info.age()

    @property
    def birth_date(self):
        return self._birth_info.date

>>> from person import Person
>>> john = Person("John Doe", date(1998, 5, 15))
>>> john.age
>>> john.birth_date
>>> jane = Person("Jane Doe", "2000-11-29")
>>> jane.age
>>> jane.birth_date
>>> linda = Person("Linda Smith", 1011222000)
>>> linda.age
>>> linda.birth_date
>>> david = Person("David Smith", {"year": 2000, "month": 7, "day": 25})

```