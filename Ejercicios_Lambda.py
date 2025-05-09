print(f"---------- LIBROS ----------\n")
biblioteca = [
    {"titulo": "El Quijote", "autor": "Cervantes", "precio": 20},
    {"titulo": "Las olas", "autor": "Virginia Woolf", "precio": 17},
    {"titulo": "Los detectives salvajes", "autor": "Roberto Bolaño", "precio": 23},
    {"titulo": "Tom va a la escuela", "autor": "Rick Sánchez", "precio": 10}
]

print(f" \n1. Sumar todos los precios de los libros\n")


suma_precios = 0
for libro in biblioteca:
    suma_precios += libro["precio"]
print("Suma precios libros:", suma_precios)


print(f"\n2. Encontrar el libro con el precio más alto\n")


libro_mas_caro = biblioteca[0]  # Inicializamos con el primer libro
for libro in biblioteca[1:]:  # Empezamos el bucle desde el segundo elemento
    if libro["precio"] > libro_mas_caro["precio"]:
        libro_mas_caro = libro  # Actualizamos si encontramos uno más caro
print("Libro más caro es :", libro_mas_caro)


print(f"\n3. Ordenar la lista de libros por título (alfabéticamente)\n")


ordenados_por_titulo = sorted(biblioteca, key=lambda libro: libro["titulo"])
print("Libros ordenados por título:", ordenados_por_titulo)


print(f"\n---------- PROYECTOS ----------\n")


proyecto = [

    {"nombre": "Análisis", "horas": 10, "precio": 60},
    {"nombre": "Desarrollo", "horas": 50, "precio": 50},
    {"nombre": "Implementación", "horas": 5, "precio": 70},
    {"nombre": "Pruebas", "horas": 15, "precio": 40},
]

print(f"\n1. Calcular el coste total de todos los proyectos\n")


coste_total = 0
for p in proyecto:
    coste_total += p["horas"] * p["precio"]
print(f"Coste total proyectos:{coste_total}")

print(f"\n2. Proyecto con mayor coste (horas * precio)\n")

proyecto_mas_caro = proyecto[0]  # Inicializamos con el primer proyecto
for p in proyecto[1:]:  # Empezamos el bucle desde el segundo proyecto
    if p["horas"] * p["precio"] > proyecto_mas_caro["horas"] * proyecto_mas_caro["precio"]:
        proyecto_mas_caro = p  # Actualizamos si encontramos un proyecto más caro
print("Proyecto más caro:", proyecto_mas_caro)


print(f"\n3. Ordenar los proyectos por número de horas (de menor a mayor)\n")

ordenados_por_horas = sorted(proyecto, key=lambda p: p["horas"])
print("Proyectos ordenados por horas:", ordenados_por_horas)

print(f"\n4. Filtrar los proyectos que cuesten más de 1000 €\n")

proyectos_caros = []
for p in proyecto:
    if p["horas"] * p["precio"] > 1000:
        proyectos_caros.append(p)
print("Proyectos con coste > 1000€:", proyectos_caros)

#solucion del prof


biblioteca = [
    {"titulo": "El Quijote", "autor": "Cervantes", "precio": 20},
    {"titulo": "Las olas", "autor": "Virginia Woolf", "precio": 17},
    {"titulo": "Los detectives salvajes", "autor": "Roberto Bolaño", "precio": 23},
    {"titulo": "Tom va a la escuela", "autor": "Rick Sánchez", "precio": 10}
]

# Para resolver los siguientes ejercicios podéis usar cualquier método de los vistos en clase

# Calcular la suma de todos los precios

# obtener precio
# Haciendo el bucle de toda la vida y sumando los precios
suma = 0
for libro in biblioteca:
    suma += libro["precio"]
print(suma)
# Comprension de listas obteniendo solo el precio, entonces ya puedo usar 'sum'
precios = [libro["precio"] for libro in biblioteca]
print(sum(precios))
# Obteniendo los precios mediante el 'map' y una función lambda, después puedo usar 'sum'
precios = list(map(lambda x: x["precio"], biblioteca))
print(sum(precios))

# Queremos obtener el libro con el precio más alto
# Método tradicional con un for nos guardamos el más caro 'de momento'
libroCaro = None
precio = 0
for libro in biblioteca:
    # Si encontramos uno más caro nos lo quedamos
    if libro["precio"] > precio:
        precio = libro["precio"]
        libroCaro = libro
print(libroCaro)

# Usar max junto con lambda para que busque el máximo de la propiedad 'precio'
libroCaro = max(biblioteca, key=lambda x: x["precio"])
print(libroCaro)

# queremos ordenarlos por título

# Ordenamos mediante título usando una lambda
librosPorTitulo = sorted(biblioteca, key=lambda x: x["titulo"])
print(librosPorTitulo)

proyectos = [
    {"nombre": "Análisis", "horas": 10, "precio": 60},
    {"nombre": "Desarrollo", "horas": 50, "precio": 50},
    {"nombre": "Implementación", "horas": 5, "precio": 70},
    {"nombre": "Pruebas", "horas": 15, "precio": 40},
]

# Queremos calcular el coste total de todos los proyectos (horas*precio)

total = 0
for proyecto in proyectos:
    total += proyecto["horas"] * proyecto["precio"]
print(total)

importes = [proyecto["horas"] * proyecto["precio"] for proyecto in proyectos]
print(sum(importes))
importes = list(map(lambda x: x["precio"] * x["horas"], proyectos))
print(sum(importes))

# El proyecto con mayor coste (horas*precio)
mayorCoste = max(proyectos, key=lambda proyecto: proyecto["precio"] * proyecto["horas"])
print(mayorCoste)
# ordenar por número de horas
porHoras = sorted(proyectos, key=lambda x: x["horas"])
print(porHoras)
# Filtrar los que cuesten más 1000 €

caros = [proyecto for proyecto in proyectos if proyecto["horas"] * proyecto["precio"] > 1000]
print(caros)
caros = list(filter(lambda x: x["horas"] * x["precio"] > 1000, proyectos))
print(caros)



