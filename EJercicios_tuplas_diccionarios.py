# Cread una función provincias() que nos devuelva una tupla con las provincias de Catalunya
# utilizad desempaquetamiento para asignarlo a cuatro variables a,b,c,d
# Recorred la tupla con un for

def provincias():
    return ("Barcelona", "Tarragona", "Lleida", "Girona")

# Desempaquetamiento
a, b, c, d = provincias()

# Recorrido con for
for provincia in provincias():
    print(provincia)

# Cread una función descuentos que nos devuelva una tupla con descuentos de 5,10 y 20
# utilizad desempaquetamiento para:
# obtener los 3 descuentos
# obtener el primer descuento e ignorar los otros dos


def descuentos():
    return (5, 10, 20)

# Desempaquetamiento completo
d1, d2, d3 = descuentos()

# Desempaquetamiento parcial (solo el primero, ignorar los demás)
d1, *_ = descuentos()

print(d1)



# Cread una función estadística a la que le pasamos una lista de números y nos devuelve una tupla
# con la cantidad de números, la suma, y la media
# estadistica([1,2,3,4])->(4,10,2.5)


# Cread un diccionario para almacenar los datos de un cliente que son nombre Eva, email eva@eva.com
# telefono 666777666 y credito 5000
cliente = {
    "nombre": "Eva",
    "email": "eva@eva.com",
    "telefono": "666777666",
    "credito": 5000
}


# Cread una función a la que le pasamos un diccionario como el de los libros y nos devuelve el
# título del libro que tenga más ejemplares



#solucion del prof:


# Cread una función provincias() que nos devuelva una tupla con las provincias de Catalunya
# utilizad desempaquetamiento para asignarlo a cuatro variables a,b,c,d
# Recorred la tupla con un for

def provincias():
    return ("Barcelona", "Girona", "Lleida", "Tarragona")


a, b, c, d = provincias()
print(c)  # Lleida

for provincia in provincias():
    print(provincia)


# Cread una función descuentos que nos devuelva una tupla con descuentos de 5,10 y 20
# utilizad desempaquetamiento para:
# obtener los 3 descuentos
# obtener el primer descuento e ignorar los otros dos
def descuentos():
    return (5, 10, 20)


d1, d2, d3 = descuentos()
print(d1, d2, d3)
d1, *_ = descuentos()
d1, _, _ = descuentos()
print(d1)
print(descuentos())


# Cread una función estadística a la que le pasamos una lista de números y nos devuelve una tupla
# con la cantidad de números, la suma, y la media
# estadistica([1,2,3,4])->(4,10,2.5)

# Tuplas
def estadistica(lista):
    return (len(lista), sum(lista), sum(lista) / len(lista))


print(estadistica([1, 2, 3, 4]))
# Ejemplos de desempaquetado
# solo quiero la media
*_, media = estadistica([1, 2, 3, 4])
print(media)
# solo quiero la suma
_, suma, _ = estadistica([1, 2, 3, 4])
print(suma)
# Si quiero recuperar todo hago esto
longitud, suma, media = estadistica([1, 2, 3, 4])


# vs Listas
def estadistica(lista):
    return [len(lista), sum(lista), sum(lista) / len(lista)]


# quiero saber la media
media = estadistica([2, 4, 91, 7])[2]
# quiero todos
longitud = estadistica([2, 4, 91, 7])[0]
suma = estadistica([2, 4, 91, 7])[1]
media = estadistica([2, 4, 91, 7])[2]
# Cread un diccionario para almacenar los datos de un cliente que son nombre Eva, email eva@eva.com
# telefono 666777666 y credito 5000
cliente = {
    "nombre": "Eva",
    "email": "eva@eva.com",
    "telefono": "666777666",
    "credito": 5000
}


# Cread una función a la que le pasamos un diccionario como el de los libros y nos devuelve el
# título del libro que tenga más ejemplares
def masEjemplares(libros):
    titulo = ""
    ejemplares = 0
    for clave, valor in libros.items():
        if valor > ejemplares:
            ejemplares = valor
            titulo = clave

    return titulo


inventario = {
    "Cien años de soledad": 400,
    "El Principito": 10,
    "1984": 6,
    "Tierra yerma": 400
}
inventario["El Quijote"] = 90
print(masEjemplares(inventario))

print(list(inventario.keys())[1:3])
# list, tuple y dict podemos convertir a lista, tupla o diccionario
print(list(inventario))  # todas las claves
print(list(inventario.values()))  # todos los valores
print(max(inventario.values()))


def masEjemplares2(libros):
    maximo = max(libros.values())
    titulo = [libro for libro, ejemplares in libros.items() if ejemplares == maximo]
    return titulo


print(masEjemplares2(inventario))