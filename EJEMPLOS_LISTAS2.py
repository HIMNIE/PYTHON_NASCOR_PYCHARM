# Crea una función a la que le pasamos una lista de cadenas y me devuelva la más larga
# si hay varias cadenas con la misma longitud, la primera
# masLarga(["aa","eeeee","bbb"])->"eeeee"

# en algún sitio guardaré la cadena más larga
# recorrer la lista
# si la cadena que estoy mirando es más larga que la que ya tengo me quedo con ella

def masLarga(lista):
    larga = ""
    for cadena in lista:
        # Aquí está la magia
        if len(cadena) > len(larga):
            larga = cadena

    return larga


lista = ['a', 'b', 'c', 'a']
print(lista.index('a'))  # 0
print(lista.index('a', 1))  # 3

numeros = [2, 4, 6, 8, 9, 6, 9, 7, 6]
try:
    pos = numeros.index(6)  # 2
    print(pos)
    pos = numeros.index(6, pos + 1)  # 5
    print(pos)
    pos = numeros.index(6, pos + 1)  # 8
    print(pos)
    pos = numeros.index(6, pos + 1)  # Error
    print(pos)
except:
    print("No encontrado")

print(numeros.count(6))

copia_incorrecta = numeros
copia_correcta = numeros.copy()
numeros[0] = 27
print(copia_incorrecta)
print(copia_correcta)
copia_incorrecta[1] = 99
print(numeros)
print(copia_correcta)


# Cuidado con modificar las listas dentro de las funciones, porque la modificación afecta fuera
# Si por lo que sea tenemos que modificar, hagamos una copia
def sumar(lista):
    suma = 0
    for i in range(len(lista)):
        suma += lista.pop()
    return suma


def buscar(lista, elemento):
    posiciones = []
    try:
        pos = lista.index(elemento)
        while True:
            posiciones.append(pos)
            pos = lista.index(elemento, pos + 1)
    except:
        return posiciones


print(buscar(numeros, 6))

numeros = [2, 4, 6, 8, 9, 6, 9, 7, 6]

numeros.sort()
# Modificamos la propia lista, que queda ordenada
print(numeros)

numeros.sort(reverse=True)

print(numeros)

numeros = [2, 4, 6, 8, 9, 6, 9, 7, 6]
# Nos crea una copia ordenada de la lista y la lista original queda como estaba
ordenados = sorted(numeros)

print(numeros)
print(ordenados)

numeros.reverse()
print(numeros)

clase = ["Ana", "Pep", "Rosa", "Iu", "Eva"]
clase.reverse()
print(clase)

clase = ["Ana", "Pep", "Rosa", "Iu", "Eva"]
# Tengo que convertir a lista por cosillas del Python, que no devuelve una lista sino un iterador
clase_vuelta = list(reversed(clase))
print(clase)
print(clase_vuelta)
# Aquí no hace falta convertir a lista porque el in funciona con iteradores
for alumno in reversed(clase):
    print(alumno)

# El key nos permite ordenar por funciones diferentes a las alfabéticas
# En este caso, ordeno por longitud
clase_orden = sorted(clase, key=len)
print(clase_orden)