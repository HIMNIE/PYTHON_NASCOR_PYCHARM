# Un diccionario es una estructura de datos que almacena un conjunto de pares
# clave, valor
# Es decir, no son valores únicos, sino que se componen de una clave y de un valor
# La clave es inmutable y el valor no

persona = {
    "nombre": "Ana",
    "edad": 30,
    "profesion": "Ingeniera"
}
print(persona)
print(persona["edad"])  # 30
persona["edad"] = 32
print(persona)
persona["sueldo"] = 5000
print(persona)
# print(persona["foo"]) # Da error porque no hay esa clave
print(persona.get("foo"))  # NO da error aunque no hay esa clave
print(persona.get("foo", "Sin valor"))  # NO da error aunque no hay esa clave y le doy un valor por defecto



alumno = {
    "nombre": "him",
    "nota": 10,
    "curso": "bachillerato"
}

print(alumno.keys())
print(alumno.values())
print(alumno.items())

# Un diccionario es una estructura de datos que almacena un conjunto de pares
# clave, valor
# Es decir, no son valores únicos, sino que se componen de una clave y de un valor
# La clave es inmutable y el valor no

persona = {
    "nombre": "Ana",
    "edad": 30,
    "profesion": "Ingeniera"
}
print(persona)
print(persona["edad"])  # 30
persona["edad"] = 32
print(persona)
persona["sueldo"] = 5000
print(persona)
# print(persona["foo"]) # Da error porque no hay esa clave
print(persona.get("foo"))  # NO da error aunque no hay esa clave
print(persona.get("foo", "Sin valor"))  # NO da error aunque no hay esa clave y le doy un valor por defecto

# probad a crear un diccionario para un alumno que tenga nombre, nota y curso

alumno = {
    "nombre": "Ana",
    "nota": 8,
    "curso": "Bachillerato"
}

print(alumno.keys())  # Me devuelve todas las claves
print(alumno.values())  # Me devuelve todos los valores
print(alumno.items())  # Me devuelve todos los pares clave,valor

# recorrer un diccionario
for clave, valor in alumno.items():
    print(f"La clave {clave} tiene el valor {valor}")

for i in alumno.items():
    print(i)

# 1. Crear un diccionario con libros y su cantidad en inventario
inventario = {
    "Cien años de soledad": 4,
    "El Principito": 10,
    "1984": 6
}

# 2. Añadir un nuevo libro
inventario["Don Quijote"] = 3

# 3. Modificar la cantidad de un libro existente
inventario["1984"] = 8

# 4. Eliminar un libro del inventario
del inventario["El Principito"]  # inventario.pop("El Principito")

# 5. Recorrer el diccionario e imprimir el inventario
print("Inventario actual:")
for titulo, cantidad in inventario.items():
    print(f"{titulo}: {cantidad} ejemplares")

# 6. Obtener solo los títulos disponibles
titulos = [titulo for titulo in inventario]
print("\nTítulos disponibles:", titulos)

# 7. Crear una lista de libros con más de 5 ejemplares
populares = [titulo for titulo, cantidad in inventario.items() if cantidad > 5]
print("\nLibros populares (más de 5 ejemplares):", populares)

# 8. Crear un nuevo diccionario con solo los libros escasos (3 o menos)
escasos = {titulo: cantidad for titulo, cantidad in inventario.items() if cantidad <= 3}
print("\nLibros escasos:", escasos)