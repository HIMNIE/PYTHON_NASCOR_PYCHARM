#corregir codigo

def factorial (numero):
    total=1
    while numero>1:
        total*=numero
        numero-=1
    return total

print(factorial(5))  #120


def palabraMasLarga(cadena):
    # Dividimos la cadena en palabras usando espacios como separadores
    palabras = cadena.split()

    # Suponemos que la primera palabra es la más larga inicialmente
    masLarga = palabras[0]

    # Recorremos todas las palabras en la lista
    for palabra in palabras:
        # Si encontramos una palabra más larga que la actual
        if len(palabra) > len(masLarga):
            # Actualizamos 'masLarga' con esta nueva palabra
            masLarga = palabra

    # Devolvemos la palabra más larga encontrada
    return masLarga


# Probamos la función con una frase
print(palabraMasLarga("En un lugar de la mancha de cuyo nombre no quiero acordarme"))



frase = "Hola mundo feliz"
palabras = frase.split()
print(palabras)


#examen:


# corregir código

def factorial(numero):
    total = 1
    while numero > 1:
        total *= numero
        numero -= 1
    return total


print(factorial(5))  # 120 5*4*3*2*1


def palabraMaslarga(cadena):
    palabras = cadena.split(" ")
    masLarga = palabras[0]  # Aquí NO hay un error
    for palabra in palabras:
        if len(palabra) > len(masLarga):  # Aquí hay un error (al revés)
            masLarga = palabra  # Aquí hay un error
    return masLarga


def numeroMayor(lista):
    mayor = lista[0]
    for numero in lista:
        if numero > mayor:  # Aquí hay un error (al revés)
            mayor = numero  # Aquí hay un error
    return mayor


print(palabraMaslarga("En un lugar de la mancha de cuyo nombre no quiero acordarme"))
print(numeroMayor([1, 2, 3, 7, 6, 5, 2]))
print(numeroMayor([-5, -2, -17 - 3]))


# Cread una función porcentajeIva que nos devuelva:
# 0 si el producto es "primera necesidad"
# 4 si es 'libro' o 'revista'
# 10 si es 'pañales'
# 21 en otros casos
def porcentajeIva(producto):
    if producto == "primera necesidad":
        return 0
    elif producto == "libro" or producto == "revista":
        return 4
    elif producto == "pañales":
        return 10
    else:
        return 21


print(porcentajeIva("primera necesidad"))
print(porcentajeIva("libro"))
print(porcentajeIva("revista"))
print(porcentajeIva("pañales"))
print(porcentajeIva("cacahuetes"))


# define una función a la que le pasamos una cadena y nos dice la media de longitud
# de las palabras de la cadena
def mediaLongitud(cadena):
    palabras = cadena.split(" ")
    longitudTotal = 0
    for palabra in palabras:
        longitudTotal += len(palabra)
    return longitudTotal / len(palabras)


def mediaLongitud2(cadena):
    palabras = cadena.split(" ")
    longitudes = [len(palabra) for palabra in palabras]
    return sum(longitudes) / len(palabras)


print(mediaLongitud("aa bbbb ccc"))
print(mediaLongitud2("aa bbbb ccc"))


# Una función números pares a la que le pasamos una lista de números y nos devuelve los pares

def numerosPares(lista):
    resultado = []
    for numero in lista:
        if numero % 2 == 0:
            resultado.append(numero)
    return resultado


def numerosPares2(lista):
    return [numero for numero in lista if numero % 2 == 0]


print(numerosPares([1, 2, 3, 4, 5, 6, 7, 8]))
print(numerosPares2([1, 2, 3, 4, 5, 6, 7, 8]))





clase = [{
    "nombre": "Ana",
    "creditos": 15,
    "curso": "Python"
}, {
    "nombre": "Iu",
    "creditos": 5,
    "curso": "Python"
}, {
    "nombre": "Eva",
    "creditos": 25,
    "curso": "BBDD"
}, {
    "nombre": "Pep",
    "creditos": 7,
    "curso": "BBDD"
}, ]


# Crea una función a la que le pasamos una clase y nos devuelve el total de créditos
def totalCreditos(clase):
    total = 0
    for alumno in clase:
        total += alumno['creditos']
    return total


def totalCreditos2(clase):
    total = sum([alumno['creditos'] for alumno in clase])
    return total


def totalCreditosCurso(clase, curso):
    total = 0
    for alumno in clase:
        if alumno['curso'] == curso:
            total += alumno['creditos']
    return total


def totalCreditosCurso2(clase, curso):
    total = sum([alumno['creditos'] for alumno in clase if alumno['curso'] == curso])
    return total


print(totalCreditos(clase))
print(totalCreditos2(clase))
print(totalCreditosCurso(clase, "BBDD"))
print(totalCreditosCurso2(clase, "BBDD"))


# ordenar los alumnos por crédito

def ordenCredito(clase):
    ordenados = sorted(clase, key=lambda x: x['creditos'])
    return ordenados


def ordenarCredito(clase):
    ordenados = sorted([alumno['creditos'] for alumno in clase])
    return ordenados


def mayorCredito(clase):
    mayor = max(clase, key=lambda x: x['creditos'])
    return mayor


def mayorCredito2(clase):
    mayor = max([alumno['creditos'] for alumno in clase])
    return mayor


print(ordenCredito(clase))
print(ordenarCredito(clase))
print(mayorCredito(clase))
print(mayorCredito2(clase))


# Cread una función a la que le pasamos una cadena y una letra y nos devueve una
# lista con las palabras que tienen esa letra

def palabrasConLetra(cadena, letra):
    palabras = cadena.split(" ")
    resultado = []
    for palabra in palabras:
        if letra in palabra:
            resultado.append(palabra)
    return resultado


def palabrasConLetra2(cadena, letra):
    palabras = cadena.split(" ")
    return [palabra for palabra in palabras if letra in palabra]


print(palabrasConLetra("hola que tal yo mal", "a"))
print(palabrasConLetra2("hola que tal yo mal", "a"))


# Una función a la que le pasamos una cadena y nos devuelve una lista
# con la primera letra de cada palabra

def primeraLetra(cadena):
    palabras = cadena.split(" ")
    resultado = []
    for palabra in palabras:
        resultado.append(palabra[0])
    return resultado


def primeraLetra2(cadena):
    palabras = cadena.split(" ")
    return [palabra[0] for palabra in palabras]


print(primeraLetra("hola que tal yo muy bien"))
print(primeraLetra2("hola que tal yo muy bien"))


# Cread una función a la que le pasamos una cadena y nos devuelve una lista de palabras
# que empiecen y acaben con la misma letra
def inicioFin(cadena):
    palabras = cadena.split(" ")
    resultado = []
    for palabra in palabras:
        if palabra[0] == palabra[-1]:
            resultado.append(palabra)
    return resultado


def inicioFin2(cadena):
    palabras = cadena.split(" ")
    return [palabra for palabra in palabras if palabra[0] == palabra[-1]]


print(inicioFin("hola ana como sales tan pronto"))
print(inicioFin2("hola ana como sales tan pronto"))