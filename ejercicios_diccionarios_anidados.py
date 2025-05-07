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