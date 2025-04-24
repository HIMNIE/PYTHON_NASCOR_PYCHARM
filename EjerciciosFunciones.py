# Cread una función a la que le pasemos un nombre y nos devuelva una cadena con un saludo
# saludo("Ana") -> "Hola Ana"


# Cread una función a la que le pasamos una cadena y una cantidad y nos devuelve la cadena repetida esa cantidad
# repetir("Ana",3)->"AnaAnaAna"


# Cread una función a la que le pasamos un número y nos devuelve True si es par y False si no lo es
# esPar(5)->False  esPar(80)->True



# Función que recibe un nombre y devuelve un saludo personalizado
def saludo(nombre):
    return "Hola " + nombre  # Devuelve la cadena "Hola " seguida del nombre recibido


# Función que recibe una cadena y un número, y devuelve la cadena repetida esa cantidad de veces
def repetir(cadena, cantidad):
    return cadena * cantidad  # Usa la multiplicación de cadenas para repetirla


# Función que recibe un número y devuelve True si es par, False si es impar
def esPar(numero):
    return numero % 2 == 0  # Un número es par si al dividirlo entre 2 el resto es 0


# Ejemplos de uso:
print(saludo("Ana"))         # Salida: Hola Ana
print(repetir("Ana", 3))     # Salida: AnaAnaAna
print(esPar(5))              # Salida: False
print(esPar(80))             # Salida: True



# Función que recibe un nombre y devuelve un saludo personalizado
def saludo(nombre):
    return "Hola " + nombre

# Función que recibe una cadena y un número, y devuelve la cadena repetida esa cantidad de veces
def repetir(cadena, cantidad):
    return cadena * cantidad

# Función que recibe un número y devuelve True si es par, False si es impar
def esPar(numero):
    return numero % 2 == 0

# ------------------- USO INTERACTIVO -------------------

# Pedimos al usuario su nombre y saludamos
nombre_usuario = input("Introduce tu nombre: ")
print(saludo(nombre_usuario))

# Pedimos al usuario una cadena y una cantidad, y mostramos la repetición
cadena_usuario = input("Introduce una palabra para repetir: ")
cantidad_usuario = int(input("¿Cuántas veces quieres repetirla?: "))
print(repetir(cadena_usuario, cantidad_usuario))

# Pedimos un número al usuario y mostramos si es par
numero_usuario = int(input("Introduce un número para saber si es par: "))
if esPar(numero_usuario):
    print("El número es par.")
else:
    print("El número es impar.")
