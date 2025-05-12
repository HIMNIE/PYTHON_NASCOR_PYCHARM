#ejercicio1
# función a la que le pasamos una lista de números y nos devuelve una tupla
# con el número de pares y el número de impares
# contarParidad([1,2,3,4,5])->(2,3) (dos pares y tres impares)


def contarParidad(lista):
    pares = 0
    impares = 0
    for num in lista:
        if num % 2 == 0:
            pares += 1
        else:
            impares += 1
    return (pares, impares)

# Ejemplo de uso
print(contarParidad([1, 2, 3, 4, 5]))  # (2, 3)




#ejercicio2:
# Cread una función que nos devuelva la suma de precios del concesionario

concesionario = [
    {"marca":"Tesla", "tipo":"Electrico", "autonomía":500, "precio":40000},
    {"marca":"Citroen", "tipo":"Gasolina", "autonomía":2500, "precio":10000},
    {"marca":"Ford", "tipo":"Gasolina", "autonomía":3500, "precio":20000},
    {"marca":"Ferrari", "tipo":"Gasolina", "autonomía":5500, "precio":120000},
    {"marca":"Seat", "tipo":"Electrico", "autonomía":700, "precio":10000},
    {"marca":"Skoda", "tipo":"Gasolina", "autonomía":3500, "precio":7000}
]

def sumaPrecios(concesionario):
    total = 0
    for coche in concesionario:
        total += coche["precio"]
    return total

# Ejemplo de uso
print(sumaPrecios(concesionario))  # suma de todos los precios







#ejercicio3
# Cread una función a la que le pasamos una cadena y una longitud y nos devuelve las cadenas
# que superan esa longitud
# masLargas("hola que tal vamos",3)->["hola","vamos"]

def masLargas(cadena, longitud):
    palabras = cadena.split()  # separa la cadena en palabras
    resultado = []
    for palabra in palabras:
        if len(palabra) > longitud:
            resultado.append(palabra)
    return resultado

# Ejemplo de uso
print(masLargas("hola que tal vamos", 3))  # ['hola', 'vamos']
