# Cread una función a la que le pasamos dos cadenas y nos devuelve la cadena más larga
# si son iguales nos devuelve la primera
# masLarga("hola","adios")-> "adios"
def masLarga(cadena1, cadena2):
    """
    Devuelve la cadena más larga.
    Si ambas tienen la misma longitud, devuelve la primera.
    """
    if len(cadena1) >= len(cadena2):
        return cadena1
    else:
        return cadena2

# Ejemplo de uso:
print(masLarga("hola", "adios"))  # Output: "adios"


# Cread una función que nos devuelva True si la cadena empieza y acaba por la misma letra, False en caso contrario
# mismoInicioFin("hola")->False mismoInicioFin("ajada")->True
def mismoInicioFin(cadena):
    """
    Devuelve True si la cadena empieza y termina con la misma letra.
    False en caso contrario. Ignora mayúsculas/minúsculas.
    """
    if len(cadena) == 0:
        return False
    return cadena[0].lower() == cadena[-1].lower()

# Ejemplos de uso:
print(mismoInicioFin("hola"))   # False
print(mismoInicioFin("ajada"))  # True


# Cread una función a la que le pasemos una cadena y nos reemplace todas las 'l' por un '1'
# y todas las 'e' por '3' independientemente de si son mayúsculas o minúsculas
# nnumerizar("leche")->"13ch3"

def numerizar(cadena):
    """
    Reemplaza 'l' o 'L' por '1' y 'e' o 'E' por '3' en la cadena dada.
    """
    return cadena.replace('l', '1').replace('L', '1').replace('e', '3').replace('E', '3')

# Ejemplo de uso:
print(numerizar("leche"))        # "13ch3"
print(numerizar("LECHE y Lluvia"))  # "13CH3 y 11uvia"


# Cread una función a la que le pasemos una cadena y nos devuelva la cadena invertida
# alreves("hola")->"aloh"
def alreves(cadena):
    """
    Devuelve la cadena invertida.
    """
    return cadena[::-1]

# Ejemplo de uso:
print(alreves("hola"))  # "aloh"


# Cread una función que nos diga si en una cadena hay letras repetidas consecutivas
# repetidas("hola que tal")-> False  repetidas("sevilla")->True


def repetidas(cadena):
    """
    Devuelve True si hay letras consecutivas iguales en la cadena.
    False en caso contrario.
    """
    for i in range(len(cadena) - 1):
        if cadena[i] == cadena[i + 1]:
            return True
    return False

# Ejemplos de uso:
print(repetidas("hola que tal"))  # False
print(repetidas("sevilla"))       # True

#correcion del prof


# Cread una función a la que le pasamos dos cadenas y nos devuelve la cadena más larga
# si son iguales nos devuelve la primera
# masLarga("hola","adios")-> "adios"

def masLarga(cadena1, cadena2):
    if len(cadena1) >= len(cadena2):
        return cadena1
    else:
        return cadena2


print(masLarga("hola", "adios"))


# Cread una función que nos devuelva True si la cadena empieza y acaba por la misma letra, False en caso contrario
# mismoInicioFin("hola")->False mismoInicioFin("ajada")->True

def mismoInicioFin(cadena):
    return cadena[0] == cadena[-1]  # if cadena[0]==cadena[-1] return True else: return False


def mismoInicioFinOtro(cadena):
    if cadena[0] == cadena[-1]:
        return "Empiezan y acaban por la misma letra"
    else:
        return "Tiene inicio y fin distinto"


print(mismoInicioFin("hola"))
print(mismoInicioFin("ajada"))
print(mismoInicioFinOtro("ajada"))


# Cread una función a la que le pasemos una cadena y nos reemplace todas las 'l' por un '1'
# y todas las 'e' por '3' independientemente de si son mayúsculas o minúsculas
# numerizar("leche")->"13ch3"

def numerizar(cadena):
    cadena = cadena.lower()
    cadena = cadena.replace("l", "1")
    cadena = cadena.replace("e", "3")
    return cadena


def numerizarCompacto(cadena):
    cadena = cadena.lower().replace("l", "1").replace("e", "3")
    return cadena


print(numerizarCompacto("leche"))


# Cread una función a la que le pasemos una cadena y nos devuelva la cadena invertida
# alreves("hola")->"aloh"

def alreves(cadena):
    resultado = ""
    for letra in cadena:
        resultado = letra + resultado
    return resultado


def alrevesNinja(cadena):
    return cadena[::-1]


cadena = "en un lugar de la mancha"

print(cadena[2:5])
print(cadena[:10])
print(cadena[:])

print(cadena[2:5:2])  # el primer número es el inicio. El segundo el final. El tercero el paso
print(cadena[:10:2])  # Si no pongo el primero se entiende que desde el principio
print(cadena[::3])  # Si no pongo tampoco el segundo se entiende que hasta el final

print(cadena[::-1])

print(alreves("hola"))
print(alrevesNinja("hola"))


# Cread una función que nos diga si en una cadena hay letras repetidas consecutivas
# repetidas("hola que tal")-> False  repetidas("sevilla")->True

def repetidas(cadena):
    anterior = ""
    for letra in cadena:
        # si la letra es igual a la anterior devuelvo True[
        if letra == anterior:
            return True
        # Guardo en anterior la letra actual, que será la anterior del siguient paso del bucle
        anterior = letra
    # He recorrido toda la cadena y no he encontrado una letra repetida, devuelvo False
    return False


def repetidasDos(cadena):
    # Ir desde el 1 hasta el final de la cadena
    # Porque antes del 0 no hay letra
    for i in range(1, len(cadena)):
        if cadena[i] == cadena[i - 1]:
            return True
    return False


print(repetidasDos("sevilla"))
print(repetidasDos("hola que tal"))
