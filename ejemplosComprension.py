def media(lista):
    suma = 0
    for numero in lista:
        suma += numero
    return (suma / len(lista))


def mediaAprobados2(lista):
    aprobados = []
    for numero in lista:
        if numero >= 5:
            aprobados.append(numero)
    return media(aprobados)


# Filtro la lista con el if >=5, no hago ninguna expresión
def mediaAprobados3(lista):
    aprobados = [nota for nota in lista if nota >= 5]
    return media(aprobados)


def contarCadenas(lista, longitud):
    # una variable donde contar
    cont = 0
    # recorrer la lista de cadenas
    for cadena in lista:
        # Si la cadena tiene una longitud mayor de 'longitud' contarla y si no hago nada
        if len(cadena) > longitud:
            cont += 1
    return cont


# Filtro la lista por las que tengan una longitud mayor que la que me pasan
def contarCadenas2(lista, longitud):
    # Palabras mayores de una longitud
    mayores = [cadena for cadena in lista if len(cadena) > longitud]
    # ¡Ojo! Devuelvo la longitud, porque estoy contando
    return len(mayores)


def minusculas(lista):
    resultado = []
    for elemento in lista:
        resultado.append(elemento.lower())
    return resultado


# No hago ningún filtro, solo transformo a minúsculas
def minusculas2(lista):
    minusculas = [cadena.lower() for cadena in lista]
    return minusculas


def longitudPar(lista):
    resultado = []
    for elemento in lista:
        if len(elemento) % 2 == 0:
            resultado.append(elemento)
    return resultado


# filtro las que tengan longitud par
def longitudPar2(lista):
    resultado = [cadena for cadena in lista if len(cadena) % 2 == 0]
    return resultado