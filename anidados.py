#buvles anidados (y cualquier tipo de anidacion)
#Nosotros podemos poner bucles dentro de bucles igual que poniamos ifs dentro de ifs:


for numero in range(1, 11): #este bucle va del 1 al 10
    print(f"Tabla del {numero}: ")#cuantas veces se imprime esto? 10 veces
    for i in range(1, 11): # este tambien va del 1 al 10
        print(f"{i} x {numero} = {i * numero}")#cuantas veces se imprime esto? 100 veces

colores = ["rojo", "verde", "azul"]
frutas = ["manzana", "plátano", "uva"]

for color in colores:
    for fruta in frutas:
        print(color, fruta)

vocales = "aeiou"
consonantes = "ptd"

for vocal in vocales:
    for consonante in consonantes:
        print(consonante + vocal)

# Reloj

for hora in range(1, 25):
    for minuto in range(1, 60):
        print(f"{hora}:{minuto}")