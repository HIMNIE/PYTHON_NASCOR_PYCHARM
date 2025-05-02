# Cread una función a la que le pasamos un cantidad y nos devuelve una lista con
# esa cantidad de la cadena "hola" repetidas
# crearHolas(4)->["Hola","Hola","Hola","Hola"]

def crearHolas(cantidad):
    # devolver una lista con la cadena "Hola" repetida 'cantidad' veces
    resultado = []
    # Tengo añadir la cadena "Hola" a esa lista n veces
    # 1.- Hacer algo n veces for
    # 2.- Añadir una cadena a una lista append
    for i in range(cantidad):
        resultado.append("Hola")

    return resultado


def crearHolas2(cantidad):
    return ["Hola"] * cantidad


print(crearHolas(4))
print(crearHolas2(4))


# tengo la siguiente función que me calcula la media de una lista
def media(lista):
    suma = 0
    for numero in lista:
        suma += numero
    return (suma / len(lista))


# Cread una función mediaAprobados que nos calcule la media pero solo de aquellos números
# que son >=5

def mediaAprobados(lista):
    suma = 0
    cont = 0
    for numero in lista:
        if numero >= 5:
            suma += numero
            cont += 1
    print(suma)
    return (suma / cont)


def mediaAprobados2(lista):
    aprobados = []
    for numero in lista:
        if numero >= 5:
            aprobados.append(numero)
    return media(aprobados)


lista = [1, 8, 3, 4, 5, 6, 2, 8, 9]
calculo = mediaAprobados(lista)
print(calculo)
calculo = mediaAprobados2(lista)
print(calculo)


# Cread una función a la que le pasemos una lista de cadenas y una longitud y nos diga
# cuantas cadenas son mayores de esa longitud
# contarCadenas(["aaa","bbbb","ccccc"],3)->2

def contarCadenas(lista, longitud):
    # una variable donde contar
    cont = 0
    # recorrer la lista de cadenas
    for cadena in lista:
        # Si la cadena tiene una longitud mayor de 'longitud' contarla y si no hago nada
        if len(cadena) > longitud:
            cont += 1
    return cont


print(contarCadenas(["aaa", "bbbb", "ccccc"], 3))
print(contarCadenas(["aaa", "bbbb", "ccccc"], 2))


# Cread una función a la que le pasamos una lista de cadenas y nos devuelve True si
# alguna de las cadenas tiene una 'j'
# tieneJ(["aa","bb"])->False   tieneJ(["aa","bb","ajo"])->True

def tieneJ(lista):
    # recorrer la lista
    for cadena in lista:
        # si la cadena tiene una j devuelvo true si no tiene NO HAGO NADA
        if "j" in cadena:
            return True
    # si al final ninguna ha tenido una j devolvemos false
    return False


print(tieneJ(["aa", "bb"]))
print(tieneJ(["aa", "bb", "ajo"]))


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