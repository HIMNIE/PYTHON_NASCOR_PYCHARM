# Ejercicios comprension
# Nivel fácil
# Crea una lista con los cuadrados de los números del 1 al 10.
# Obtén una lista con los números del 0 al 20 que sean múltiplos de 3.
# Dada la lista ["Ana", "Luis", "Pedro"], obtén una lista con sus longitudes.
# 🔧 Nivel intermedio
# Crear una función fueraNegativos a la que le pasamos una lista y nos devuelve solo los positivos fueraNegativos ([3, -1, -7, 5, 0])->[3,5,0]
# Crea una función a la que se le pasa un límite y un número y nos devuelve una lista con todos los números hasta ese límite que son múltiplos de ese número listaMultiplos(10,4)->[4,8]
# Crea una función a la que le pasamos un número y nos devuelve una lista con la tabla de multiplicar de ese número tablaMultiplicar(7)->[7,14,21,…70]
# 🔬 Nivel avanzado
# Crea una función a la que le pasamos una lista de palabras y nos devuelve solo las que tengan vocales conVocales([“hola”,”qwfr”,”que”])->[“hola”,”que”]


# Crea una lista con los cuadrados de los números del 1 al 10.

cuadrados = [numero ** 2 for numero in range(1, 11)]
print(cuadrados)
lista = [1.4, 5.6, 9.35]
cuadrados = [numero ** 2 for numero in lista]
print(cuadrados)
# Obtén una lista con los números del 0 al 20 que sean múltiplos de 3.
multiplos3 = [numero for numero in range(0, 21) if numero % 3 == 0]
print(multiplos3)
# Dada la lista ["Ana", "Luis", "Pedro"], obtén una lista con sus longitudes.
lista = ["Ana", "Luis", "Pedro"]
longitudes = [len(cadena) for cadena in lista]
print(longitudes)


# Crear una función fueraNegativos a la que le pasamos una lista y nos devuelve
# solo los positivos fueraNegativos ([3, -1, -7, 5, 0])->[3,5,0]
def fueraNegativos(lista):
    resultado = [numero for numero in lista if numero >= 0]
    return resultado


print(fueraNegativos([3, -1, -7, 5, 0]))


# Crea una función a la que se le pasa un límite y un número y nos devuelve una
# lista con todos los números hasta ese límite que son múltiplos de ese número
# listaMultiplos(10,4)->[4,8]
def listaMultiplos(limite, multiplo):
    resultado = [numero for numero in range(1, limite + 1) if numero % multiplo == 0]
    return resultado


print(listaMultiplos(10, 4))  # [4,8]
print(listaMultiplos(20, 3))  # [3,6,9,12,15,18]


# Crea una función a la que le pasamos un número y nos devuelve una lista
# con la tabla de multiplicar de ese número tablaMultiplicar(7)->[7,14,21,…70]
def tablaMultiplicar(numero):
    resultado = [numero * n for n in range(1, 11)]
    return resultado


def tablaMultiplicar2(numero):
    resultado = [n for n in range(1, numero * 10 + 1) if n % numero == 0]
    return resultado


print(tablaMultiplicar(7))  # [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]
print(tablaMultiplicar2(7))  # [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]


# Crea una función a la que le pasamos una lista de palabras y nos devuelve solo
# las que tengan vocales conVocales([“hola”,”qwfr”,”que”])->[“hola”,”que”]

def tieneVocal(cadena):
    cadena = cadena.lower()
    vocales = "aeiouáéíóúàèìòùü"
    for vocal in vocales:
        if vocal in cadena:
            return True
    return False


print(tieneVocal("hola"))  # True
print(tieneVocal("gjhgjh"))  # False


def conVocales(lista):
    resultado = [cadena for cadena in lista if tieneVocal(cadena)]
    return resultado


print(conVocales(["asasa", "jkhkjhk", "pepe", "sÍ", "üà"]))  # ['asasa', 'pepe']


# Crea una función a la que le pasamos un límite y nos dice los números primos
# hasta ese límite
def esPrimo(numero):
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True


def primosHasta(limite):
    resultado = [numero for numero in range(1, limite + 1) if esPrimo(numero)]
    return resultado


print(primosHasta(100))