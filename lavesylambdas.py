alumnos = ["Ana", "Iu", "Eva", "Victoria", "Ramon"]


def ultimaLetra(cadena):
    return cadena[-1]


ordenado = sorted(alumnos)
print(ordenado)
ordenado = sorted(alumnos, key=len)
print(ordenado)
ordenado = sorted(alumnos, key=ultimaLetra)
print(ordenado)
maslargo = max(alumnos, key=len)
print(maslargo)
maslargo = max(alumnos, key=ultimaLetra)
print(maslargo)

clase = [
    {"nombre": "Ana", "nota": 7},
    {"nombre": "Eva", "nota": 3},
    {"nombre": "Iu", "nota": 6},
    {"nombre": "Luis", "nota": 8},
    {"nombre": "Pep", "nota": 5},
]


def getNota(elemento):
    return elemento["nota"]


maslisto = max(clase, key=getNota)
print(maslisto)
peor = min(clase, key=getNota)
print(peor)

# Funciones lambda: Son funciones anónimas que se definen al momento
# lambda argumentos: expresion que se devuelve
maslisto = max(clase, key=lambda x: x["nota"])
print(maslisto)
# lo que hace el código de antes es recorrer la lista, obtener la nota de cada elemento
# ordenar por ese valor (es decir, por nota) y devolver el que tenga el valor máximo

suma_lambda = lambda x, y: x + y
print(suma_lambda(3, 4))
pornotas = sorted(clase, key=lambda alumno: alumno["nota"])
print(pornotas)

# Hay una función predefinida de python que es 'map'
# aplica una función a todos los elementos de un iterable
numeros = [1, 2, 3, 4, 5]


def cuadrado(x):
    return x ** 2


cuadrados = list(map(cuadrado, numeros))
print(cuadrados)

cuadrados2 = list(map(lambda x: x ** 2, numeros))
print(cuadrados2)

aprobados = list(filter(lambda x: x["nota"] >= 5, clase))
print(aprobados)

notas = [10, 2, 3, 4, 5, 6, 7, 8, 9]


def esPar(numero):
    return numero % 2 == 0


pares = []
for nota in notas:
    if esPar(nota):
        pares.append(nota)
print(pares)

pares2 = [nota for nota in notas if esPar(nota)]
print(pares2)

pares3 = list(filter(esPar, notas))
print(pares3)

# Reescribir esto sin usar esPar

pares = []
for nota in notas:
    if nota % 2 == 0:
        pares.append(nota)
print(pares)

pares2 = [nota for nota in notas if nota % 2 == 0]
print(pares2)

pares3 = list(filter(lambda nota: nota % 2 == 0, notas))
print(pares3)

pedidos = [{"producto": "Libro", "precio": 20}, {"producto": "Lápiz", "precio": 2},
           {"producto": "Cuaderno", "precio": 5}, {"producto": "Tablet", "precio": 200},
           {"producto": "Funda", "precio": 15}]

# pedidos de 20 de precio o más
masde20 = []
for pedido in pedidos:
    if pedido["precio"] >= 20:
        masde20.append(pedido)

print(masde20)

masde20b = [pedido for pedido in pedidos if pedido["precio"] >= 20]
print(masde20b)

masde20c = list(filter(lambda pedido: pedido["precio"] >= 20, pedidos))
print(masde20c)
