# Programación funcional
# lo que hemos estado haciendo hasta ahora es lineal
# cada instrucción sigue a la siguiente hasta que acabamos
# El primer paso para una programación estructurada es usar funciones
# ¿Qué es una función?
# Bloque de código reutilizable que permite recibir parámetros y devolver un resultado

# sintaxis def nombre_de_la_funcion(parametros):
# Esta función no tiene parámetros pero uso () igual
def saludar():
    # Estas tres líneas se ejecutan cuando se llama a la función
    print("Hola")
    print("¿Qué tal estás")
    print("Yo muy bien")


saludar()
print("------")
saludar()
print("------")


# Incorporamos un parámetro
def saludarNombre(nombre):
    print(f"Hola {nombre}")
    print("¿Qué tal estás")
    print("Yo muy bien")


saludarNombre("Ana")
print("------")
saludarNombre("Juan")


# Añadir devolver un resultado

def suma(a, b):
    return a + b


print(suma(2, 3))
print(suma(8, 10))

resultado = suma(19, 35)
print(resultado)


# Definimos una función llamada contarLetra que recibe dos parámetros:
# cadena: el texto en el que vamos a buscar
# letra: la letra que queremos contar
def contarLetra(cadena, letra):
    contador = 0  # Inicializamos un contador en 0

    # Recorremos cada carácter (c) en la cadena de texto
    for c in cadena:
        # Si el carácter actual es igual a la letra que estamos buscando
        if c == letra:
            contador += 1  # Aumentamos el contador en 1

    # Devolvemos el número total de veces que apareció la letra
    return contador


# Primera llamada a la función: buscamos cuántas veces aparece la letra "a" en la palabra "mancha"
total = contarLetra("mancha", "a")
print(total)  # Imprime 2, porque hay dos letras "a" en "mancha"

# Segunda llamada a la función: buscamos cuántas veces aparece la letra "n" en la frase
total = contarLetra("En un lugar de la mancha", "n")
print(total)  # Imprime 3, porque hay tres letras "n" en la frase
