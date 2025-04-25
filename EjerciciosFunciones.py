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


# Cread una función a la que le pasemos un nombre y nos devuelva una cadena con un saludo
# saludo("Ana") -> "Hola Ana"

def saludo(nombre):
    resultado = "Hola " + nombre
    return resultado





#<---------------------------> Solucion del prof <--------------------------------------->




# Cread una función a la que le pasamos una cadena y una cantidad y nos devuelve la cadena repetida esa cantidad
# repetir("Ana",3)->"AnaAnaAna"

def repetir(cadena, cantidad):
    # código que nos repita una cadena una cantidad de veces
    # Variable que me servirá de 'acumulador'
    resultado = ""
    # Bucle que me recorra una serie de elementos o, como en este caso, que me repita algo un número
    # determinado de veces
    for i in range(0, cantidad):
        # Hago la operación que sea: concatenar, sumar, contar, multiplicar...
        resultado += cadena

    return resultado


def repetir2(cadena, cantidad):
    return cadena * cantidad


def nombreTriple(nombre):
    return (f'{nombre}\n' * 3)  # Lo estamos imprimiendo directamente por la consola IMPURA


nombreTriple('Jenn')


# Cread una función a la que le pasamos un número y nos devuelve True si es par y False si no lo es
# esPar(5)->False  esPar(80)->True

def esPar(numero):
    if numero % 2 == 0:
        resultado = True
    else:
        resultado = False
    return resultado


def esParCompacta(numero):
    # En general siempre que tenemos un if que devuelve true o false podemos devolver directamente la condición del if
    return numero % 2 == 0


repetida = repetir("Hola", 5)
print(repetida)
repetida = repetir2("Hola", 5)
print(repetida)
print("hola" * 5)
print(nombreTriple("Ana"))
nombrerepetido = nombreTriple("Federico")

print(esPar(5))
print(esPar(6))

print(esParCompacta(5))
print(esParCompacta(6))