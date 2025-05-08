print(f"EJERCICIO Nª1\n")

alumnos = {
    "Ana": [8, 9, 10],
    "Luis": [5, 6, 7],
    "Marta": [9, 8, 9]
}

# 1. Imprimir el promedio de notas de cada alumno
print("Promedio de cada alumno:")

for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: {promedio}")

# 2. Añadir una nota más a cada alumno (por ejemplo, un 10)

for notas in alumnos.values():
    notas.append(10)

# 3. Mostrar el alumno con la nota media más alta
mejor_alumno = ""
mejor_promedio = 0

for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    if promedio > mejor_promedio:
        mejor_promedio = promedio
        mejor_alumno = nombre

print(f"\nEl alumno con la nota media más alta es {mejor_alumno} con un promedio de {mejor_promedio}")



print(f" EJERCICIO Nª2\n")



inventario = {
    "frutas": ["manzana", "pera", "plátano"],
    "verduras": ["zanahoria", "brócoli"],
    "bebidas": ["agua", "zumo"]
}

# 1. Añadir "sandía" a la categoría de frutas
inventario["frutas"].append("sandía")

# 2. Imprimir todos los productos (uno por línea)
print("Productos en el inventario:")
for categoria in inventario:
    for producto in inventario[categoria]:
        print(producto)

# 3. Contar cuántos productos hay en total

total = 0
for productos in inventario.values():
    total += len(productos)


print(f"\nTotal de productos:{total}")



# Método	Qué devuelve
# .keys()	Solo las claves (como "Categoria")
# .values()	Solo los valores (como "productos"])
# .items()	Pares clave-valor


#Solucion del prof


alumnos = {
    "Ana": [8, 6, 10],
    "Luis": [5, 6, 7],
    "Marta": [9, 8, 9],
    "Eva": [9, 8, 9],

}
# Esto no se pedía, pero si queremos añadir notas personalizadas a cada alumno lo podemos hacer así
notasnuevas = [6, 7, 4, 8]
# Para guardar el que tenga la media más alta. Necesitamos la media para saber el valor
# y primerodelaclase para el nombre
mediaprimero = 0
primerodelaclase = ""
# recorrer un diccionario
for alumno, notas in alumnos.items():
    media = sum(notas) / len(notas)
    print(f"El alumno {alumno} tiene una nota media de {media:.2f}")
    if media > mediaprimero:
        mediaprimero = media
        primerodelaclase = alumno
    notas.append(notasnuevas.pop())
print("El primero de la clase es ", primerodelaclase)  #

# No es recomendable. Por varias cosas, una, si añado alumnos ya no funciona
# Si tengo muchos alumnos se me juntan demasiadas líneas
# Y no vale decir 'Así pongo una nota individualizada' ;)
alumnos["Ana"].append(3)
alumnos["Luis"].append(3)
alumnos["Marta"].append(3)

alumnos.keys()  # Las claves "Ana","Luis"...
alumnos.values()  # Los valores [8, 6, 10],...
alumnos.items()  # Los pares clave valor ("Ana",[8, 6, 10])....

alumnos  # python me devuelve alumnos.keys()

inventario = {
    "frutas": ["manzana", "pera", "plátano"],
    "verduras": ["zanahoria", "brócoli"],
    "bebidas": ["agua", "zumo"]
}

# Añade "sandía" a la categoría de frutas.
inventario["frutas"].append("sandía")
print(inventario)
# Imprime todos los productos (uno por línea).
for productos in inventario.values():
    for producto in productos:
        print(producto)

# Cuenta cuántos productos hay en total.
numproductos = 0
for productos in inventario.values():
    numproductos += len(productos)
print(numproductos)

# Diccionario donde cada cliente tiene una lista de pedidos (cada pedido es un dict)
clientes = {
    "Juan": [{"producto": "Libro", "precio": 20}, {"producto": "Lápiz", "precio": 2}],
    "Ana": [{"producto": "Cuaderno", "precio": 5}],
    "Luis": [{"producto": "Tablet", "precio": 200}, {"producto": "Funda", "precio": 15}]
}


def total_gastado(cliente, datos):  # Nos devuelve cuanto ha gastado cada cliente en total
    pedidos = datos[cliente]
    total = 0
    for pedido in pedidos:
        total += pedido["precio"]
    return total


def total_gastado_c(cliente, datos):
    return sum([pedido["precio"] for pedido in datos[cliente]])


def productosPorCliente(
        datos):  # nos devuelve un diccionario donde la clave es el nombre del cliente y el valor es el número de productos
    resultado = {}
    for clave, valor in datos.items():
        resultado[clave] = len(valor)
    return resultado


def productosPorCliente_c(
        datos):  # nos devuelve un diccionario donde la clave es el nombre del cliente y el valor es el número de productos
    return {clave: len(valor) for clave, valor in datos.items()}


# Para saber si un diccionario ya tiene una clave usamos ‘in’ como en las listas

# if "Ana" in clientes:
print(total_gastado("Luis", clientes))
print(total_gastado_c("Luis", clientes))
print(productosPorCliente(clientes))
print(productosPorCliente_c(clientes))