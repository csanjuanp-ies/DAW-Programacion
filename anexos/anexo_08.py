import random
import time
import sys

"""
************************************************************
Ampliación I
************************************************************

Diseña un programa que calcule el máximo de 5 números enteros. Intenta resolverlo con un ((candidato a valor máimo))
que se va actualizando al compararse con cada número. NO usar max.
"""


# def maximo_cinco(valores: list):
#     mayor = - sys.maxsize  # Otra aproximación es inicializar al primero y en la lista buscar desde el segundo
#     for valor in valores:
#         if valor > mayor:
#             mayor = valor
#     print(mayor)


# maximo_cinco([1, 3, 6, -1, 7])
"""
Diseña un programa que lea una cadena y un número entero k y 
nos diga cuántas palabras tienen una longitud de
k caracteres con listas y con diccionarios
"""


# def numero_palabras(cadena: str, longitud: int = 1):
#     cantidad_de_palabras = 0
#     for palabra in cadena.split(' '):
#         if len(palabra) == longitud:
#             cantidad_de_palabras += 1
#     print(cantidad_de_palabras)


# numero_palabras("Diseña una función que reciba dos listas y devuelva los elementos", 3)

"""
Diseña una función que reciba dos listas y devuelva los elementos que pertenecen a una o a otra, pero sin repetir
ninguno (unión de conjuntos).
Ejemplo: si recibe las listas [1, 2, 1] y [2, 3, 2, 4], devolver´a la lista [1, 2, 3, 4]. 
Sin usar conjuntos y usando conjuntos
comprueba la diferencia de tiempo de ejecución con 1.000.000 de elementos
"""


# def union_de_conjuntos_i(lista1: list, lista2: list):
#     conjunto = set(lista1) | set(lista2)
#     print(list(conjunto))
#
#
# def union_de_conjuntos_ii(lista1: list, lista2: list):
#     lista = []
#     for elemento in lista1:
#         if elemento not in lista:
#             lista.append(elemento)
#     for elemento in lista2:
#         if elemento not in lista:
#             lista.append(elemento)
#
#     print(lista)


# l1 = [random.randint(1, 9) for x in range(1000000)]  # [1, 2, 1]
# l2 = [random.randint(1, 9) for x in range(1000000)]  # [2, 3, 2, 4]
# inicio = time.time()
# union_de_conjuntos_i(l1, l2)
# fin = time.time()
# print(fin - inicio)
# inicio = time.time()
# union_de_conjuntos_ii(l1, l2)
# fin = time.time()
# print(fin - inicio)

"""
Guardamos en una matriz de m×n elementos la calificación 
obtenida por m estudiantes (a los que conocemos por
su número de lista) en la evaluación de n ejercicios 
entregados semanalmente (cuando un ejercicio no se ha entregado, la
calificación es −1).
Diseña funciones y procedimientos que efectúen los siguientes cálculos:
"""
# datos_alumnos = [
#     [5, 5, 7, 4],
#     [2, 5, 7, -1],
#     [3, -1, -1, 1],
#     [8, 8, 7, 9],
# ]

"""
Dado el número de un alumno, devolver el número de ejercicios entregados.
"""


# def numero_de_ejercicios_entregados(datos: list, alumno: int) -> int:
#     numero_ejercicios: int = 0
#     if alumno < len(datos):
#         numero_ejercicios = (len(datos[alumno]) - datos[alumno].count(-1))
#     return numero_ejercicios


# print(numero_de_ejercicios_entregados(datos_alumnos, 3))
"""
Dado el número de un alumno, devolver la media sobre los ejercicios entregados.
"""


# def media_de_ejercicios_entregados(datos: list, alumno: int) -> float:
#     media: float = -1
#     if alumno < len(datos):
#         valor = sum(datos[alumno]) + datos[alumno].count(-1)
#         media = (valor / numero_de_ejercicios_entregados(datos, alumno))
#     return media


# print(media_de_ejercicios_entregados(datos_alumnos, 3))
"""
Dado el número de un alumno, devolver la media sobre los ejercicios entregados si los entregó todos; en caso contrario,
la media es 0.
"""


# def media_de_ejercicios_todos_entregados(datos: list, alumno: int) -> float:
#     media: float = 0
#     # if alumno < len(datos) and -1 not in datos[alumno]:
#     if alumno < len(datos) and numero_de_ejercicios_entregados(datos, alumno) == len(datos[alumno]):
#         media = media_de_ejercicios_entregados(datos, alumno)
#
#     return media


# print(media_de_ejercicios_todos_entregados(datos_alumnos, 3))
"""
Devolver el número de todos los alumnos que han entregado todos los ejercicios y 
tienen una media superior a 3.5
puntos.
"""


# def media_de_ejercicios_todos_entregados_mas_tres_con_cinco(datos: list) -> int:
#     NOTA_EJERCICIO_NO_ENTREGADO = -1
#     NOTA_MINIMA = 3.5
#     numero_alumnos = 0
#     media: float = 0
#     for index_alumno, alumno in enumerate(datos):
#         if NOTA_EJERCICIO_NO_ENTREGADO not in alumno:
#             # if numero_de_ejercicios_entregados(datos, index_alumno) == len(datos[index_alumno]):
#             media = media_de_ejercicios_entregados(datos, index_alumno)
#             if media >= NOTA_MINIMA:
#                 numero_alumnos += 1
#
#     return numero_alumnos


# print(media_de_ejercicios_todos_entregados_mas_tres_con_cinco(datos_alumnos))
"""
Dado el número de un ejercicio, devolver la nota media obtenida por los estudiantes que lo presentaron.
"""


# def media_por_ejercicio(datos: list, numero_ejercicio: int) -> float:
#     NOTA_EJERCICIO_NO_ENTREGADO = -1
#     media: int = 0
#     numero_de_presentados = 0
#     if len(datos) > 0 and numero_ejercicio < len(datos[0]):
#         for alumno in datos:
#             if alumno[numero_ejercicio] > NOTA_EJERCICIO_NO_ENTREGADO:
#                 media += alumno[numero_ejercicio]
#                 numero_de_presentados += 1
#
#     return media / numero_de_presentados


# print(media_por_ejercicio(datos_alumnos, 0))
"""
Dado el número de un ejercicio, devolver la nota mas alta obtenida.
"""


# def nota_mas_alta_por_ejercicio(datos: list, numero_ejercicio: int) -> int:
#     nota_actual: int = -1
#     if len(datos) > 0 and numero_ejercicio < len(datos[0]):
#         for alumno in datos:
#             if alumno[numero_ejercicio] > nota_actual:
#                 nota_actual = alumno[numero_ejercicio]
#
#     return nota_actual


# print(nota_mas_alta_por_ejercicio(datos_alumnos, 2))
"""
Dado el númeroo de un ejercicio, devolver la nota más baja obtenida.
"""


# def nota_mas_baja_por_ejercicio(datos: list, numero_ejercicio: int) -> int:
#     nota_actual: int = 10
#     if len(datos) > 0 and numero_ejercicio < len(datos[0]):
#         for alumno in datos:
#             if -1 < alumno[numero_ejercicio] < nota_actual:
#                 nota_actual = alumno[numero_ejercicio]
#
#     return nota_actual


# print(nota_mas_baja_por_ejercicio(datos_alumnos, 2))
"""
Dado el número de un ejercicio, devolver el número de estudiantes que lo han presentado.
"""


# def numero_de_presentados_por_ejercicio(datos: list, numero_ejercicio: int) -> int:
#     total_presentados: int = 0
#     NOTA_EJERCICIO_NO_ENTREGADO = -1
#     if len(datos) > 0 and numero_ejercicio < len(datos[0]):
#         for alumno in datos:
#             if NOTA_EJERCICIO_NO_ENTREGADO < alumno[numero_ejercicio]:
#                 total_presentados += 1
#
#     return total_presentados


# print(numero_de_presentados_por_ejercicio(datos_alumnos, 0))

"""
************************************************************
Arrays
anexo_05/02.ipbynb
************************************************************
Para un array de tamaño N, encontrar otro array producto en el que cada elemento sea el producto de todos los elementos 
del array excepto del índice correspondiente.
"""
# n: int = 5
# nums: list[int] = [10, 3, 5, 6, 2]
# ret: list[int] = []
# multiplicacion: int = 1
# for valor in nums:
#     multiplicacion *= valor
# for elemento in nums:
#     if elemento > 0:
#         ret.append(int(multiplicacion / elemento))
#     else:
#         ret.append(0)
#
# print(ret)


"""
===================================================================
Dado un array encontrar los elementos repetidos más de una vez
"""
# A: list[int] = [2, 3, 1, 2, 3]
# B: dict[int, int] = {}
# for valor in A:
#     if valor in B.keys():
#         B[valor] += 1
#     else:
#         B[valor] = 1
# for clave, valor in B.items():
#     if valor > 1:
#         print(clave)
"""
===================================================================
Dado un array y un número encontrar todos los pares que sumen el número dado.
"""
# A: list[int] = [1, 2, 3, 4, 5, 6, 7]
# suma: int = 8
#
# lista_pares: set[(int, int)] = set()  # Conjunto para evitar duplicados

# for i in A:
#     B = A.copy()  # poco eficiente al hacer cada vez una copia
#     B.remove(i)  # Para que no salga el par conmigo mismo
#     for j in B:
#         if (j, i) not in lista_pares:
#             lista_pares.add((i, j))
# B = A.copy()  # poco eficiente al hacer cada vez una copia
# for i in A:
#     index_i = A.index(i)
#     B.remove(i)
#     for j in B:
#         if (j, i) not in lista_pares:
#             lista_pares.add((i, j))
#     B.insert(index_i, i)
#
# for i, v_i in enumerate(A):
#     for j, v_j in enumerate(A):
#         if (v_j, v_i) not in lista_pares and i != j:
#             lista_pares.add((v_i, v_j))
#
#
# for ele in lista_pares:
#     if sum(ele) == suma:
#         print(ele)

"""
************************************************************
Matrices
anexo_05/07.ipbynb
************************************************************
Escribir un programa para encontrar la transpuesta de una matriz cuadrada de tamaño N * N. 
La transposición de una matriz se obtiene cambiando filas a columnas y columnas a filas.
"""
# Arr = [[1, 1, 1, 1],
#        [2, 2, 2, 2],
#        [3, 3, 3, 3],
#        [4, 4, 4, 4]]
#
# # print(*Arr)
# lst = list(zip(*Arr))
# for fila in lst:
#     print(fila)

"""
Dada una matriz de NxN, hacerla de manera que las filas impares se imprimen de izq -> der, 
las pares al revés
"""
# data_list: list[list[int]] = [[45, 48, 54],
#                               [21, 89, 87],
#                               [70, 78, 15]]
#
#
# for index, row in enumerate(data_list):
#     if index % 2 == 1:
#         print(row[::-1])
#     else:
#         print(row)





"""
===================================================================
Dada una matriz de NxN, imprimirla en espiral
# """
# def spiral_print(filas: int, columnas: int, datos: list[list[int]]) -> None:
#     k: int = 0
#     l: int = 0
#
#     while k < filas and l < columnas:
#         for i in range(l, columnas):
#             print(datos[k][i], end=" ")
#
#         k += 1
#         for i in range(k, filas):
#             print(datos[i][columnas - 1], end=" ")
#
#         columnas -= 1
#         if k < filas:
#             for i in range(columnas - 1, (l - 1), -1):
#                 print(datos[filas - 1][i], end=" ")
#             filas -= 1
#         if l < columnas:
#             for i in range(filas - 1, k - 1, -1):
#                 print(datos[i][l], end=" ")
#             l += 1
#
#
# data = [[1, 2, 3, 4, 5, 6],
#         [7, 8, 9, 10, 11, 12],
#         [13, 14, 15, 16, 17, 18],
#         [19, 20, 21, 22, 23, 24]]
#
# rows = 4
# cols = 6
#
# spiral_print(rows, cols, data)
"""
************************************************************
Búsquedas
ampliación_II/08_Busquedas.py
************************************************************
************************************************************
Diccionarios
ampliación_II/09_Diccionarios.py
************************************************************
************************************************************
Clases
ampliación_II/11_Objetos.py
************************************************************
"""
