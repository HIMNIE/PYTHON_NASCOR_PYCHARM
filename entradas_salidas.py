
# Usamos input para pedir datos al usuario (por la consola)
nombre=input("Introduce tu nombre, por favor")
print("Te llamas ",nombre)

# ¡Ojo! Siempre se devuelve una cadena

edad=float(input("Introduce tu edad "))
print(edad+5)

# Pide al usuario su nombre y muestra un saludo como:
# "¡Hola, [nombre]! Bienvenido/a."

nombre = input("¿Cuál es tu nombre? ")
print("¡Hola,", nombre + "!", "Bienvenido/a.")

# Pide al usuario dos números y muestra la suma.
# Usa `int()` para convertir la entrada.
a = int(input("Primer número: "))
b = int(input("Segundo número: "))
print("La suma es:", a + b)