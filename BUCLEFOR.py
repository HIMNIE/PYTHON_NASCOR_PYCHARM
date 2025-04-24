# bucle for se utiliza para recorrer secuencias
# sintaxis:
# for elemento in secuencia:

# Bucle for para recorrer una serie numérica
# Elemento: i
# Secuencia: range(1,6) range nos genera un rango de números desde el primero hasta el último menos uno
# range(1,4)->[1,2,3]
# range(10,21)->[10,11,12,13,14,15,16,17,18,19,20]
for i in range(1, 6):
    print(i)

# El ejercicio de los cuadrados: mostrar los cuadrados del 1 al 10
for i in range(1, 11):
    print(i ** 2)

for letra in "En un lugar de la mancha":
    print(letra, end=" ")

palabras = 1
for letra in "En un lugar de la mancha":
    if letra == " ":
        palabras += 1
print(palabras)
# Suma de todos los números del 1 al 100 con bucle for
suma = 0
for i in range(1, 101):
    suma += i
print(suma)

# Esto en python es una lista
frutas = ["manzana", "banana", "cereza"]
for fruta in frutas:
    print(fruta)

# range(max): Un iterable de números enteros consecutivos que empieza en 0 y acaba en max - 1
for i in range(10):
    print(i)  # del 0 al 9
# range(min, max): Un iterable de números enteros consecutivos que empieza en min y acaba en max - 1
for i in range(1, 11):
    print(i)  # del 1 al 10
# range(min, max, step): Un iterable de números enteros consecutivos que empieza en min
# acaba en max - 1 y los valores se van incrementando de step en step.
# Este último caso simula el bucle for con variable de control.

for i in range(1, 100, 5):
    print(i)  # del 1 al 100 en pasos de 5

# Nos permite poner pasos negativos

for i in range(10, -1, -1):
    print(i)

# Sumar todos los números pares del 1 al 100 (incluidos)
suma = 0
for i in range(1, 101):
    if i % 2 == 0:
        suma += i
print(suma)

suma = 0
for i in range(0, 101, 2):
    suma += i
print(suma)

# Mostrar la tabla de multiplicar del 7
# 1x7=7 2x7=14 3x7=21....10x7=70
for i in range(1, 11):
    print(f"{i} x 7 = {i * 7}")

# Pedir una cadena al usuario y decirle cuantas letras 'a' tiene
# hola->1  patata->3
# Pedir una cadena al usuario: sabemos
# Un bucle para recorrer las letras (lo hemos visto en la teoría)
# Dentro de ese bucle vamos a mirar si la letra es la 'a'
contador = 0
cadena = input("Dime una cadena y te diré cuantas aes tiene ")
for letra in cadena:
    if letra == "a":
        contador += 1
print("El número de aes en '", cadena, "' es ", contador)

