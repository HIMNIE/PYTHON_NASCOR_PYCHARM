# Variables

# Caja donde almacenar valores
edad = 90
nombre = "Ana"
sueldo = 5000
iva = .21
tieneSaldo = True

# Podemos hacer operaciones

edad += 1
sueldoneto = sueldo * .85
nombre = nombre + " Pi"

# Tema de los nombres, mayúsculas y minúsculas cuentan
# no es lo mismo 'nombre' que 'Nombre' que 'NOMBRE'
# empezamos con minuscula y si hay palabra nueva a) Usamos mayusculas b) usamos guión bajo

sueldoBruto = sueldo * 1.1

sueldo_bruto = sueldo * 1.1

sb = sueldo * 1.1

# Los operadores 'extraños' son el módulo %, la división entera // y la exponenciación

resto = 7 % 3  # El resto de divivir 7 entre 3, es decir 1

entero = 7 // 3  # división entera luego 2

potencia = 2 ** 10  # 2 elevado a la décima potencia, es decir 1024

cont = 0

# sumar 1
cont = cont + 1
cont += 1

# concatenar cadena
alumno = "Ana"
alumno = alumno + " Pi"
alumno += " Pi"


# >,>=,<,<= pero ojo igual es '==' y diferente es '!='

# Operadores booleanos, que nos dan cierto o falso
# and cierto si los dos son ciertos or cierto si alguno es cierto y not cierto si es falso y viceversa

# funciones
# trozo de código reutilizable al que le pasamos parámetros y frecuentemente devolvemos un resultado
# sintaxis
# def nombre_funcion(parametros):
#     codigo
#     return resultado

# IMPORTANTE: Una función debe ser 'pura', es decir, solo depende de los parámetros que le pasamos
# devuelve un resultado que a igual parámetro igual resultado
# NO modifica el entorno, si yo le paso na variable fuera de la función debe tener el mismo valor
# con los tipos simples no hay problema, pero con las listas hay que tener cuidado
# si modificamos la lista dentro de la función también la modificamos fuera

def saludo():
    return "Hola que tal"


# Tengo la función, después la tengo que llamar

hola = saludo()
print(saludo())


def saludo2(nombre):
    return f"Hola {nombre} que tal estás"


print(saludo2("Ana"))

nombre = "Federido I de Prusia"

print(saludo2(nombre))


def saludos(cantidad=2):
    resultado = ""
    for i in range(cantidad):
        resultado += saludo() + "\n"  # resultado=resultado+saludo()+"\n"
    return resultado


print(saludos(5))
print(saludos())


# Condicional. Nos permite dirigir el flujo del código dependiendo de condiciones
# if condicion:
#   codigo si se cumple
# else:
#   codigo si no se cumple
# La condición puede ser compleja utilizando and, or y not

def mayor(a, b):
    if a > b:
        return a
    else:
        return b


print(mayor(6, 9))  # 9


def login(usuario, password):
    if usuario == "admin" and password == "1234":
        return True
    else:
        return False


print(login("Ana", "11212"))  # False
print(login("admin", "1234"))  # True

usuario = input("Dime tu usuario")
password = input("Dime la contraseña")
if login(usuario, password):
    print("Puedes entrar")
else:
    print("No puedes entrar")


def irpf(sueldo):
    if sueldo < 1000:
        return .02
    elif sueldo < 3000:
        return .05
    elif sueldo < 5000:
        return .1
    else:
        return .2


def sueldoNeto(sueldo):
    return sueldo - sueldo * irpf(sueldo)


print(irpf(2500))  # 0.05
print(sueldoNeto(2500))
miSueldo = sueldoNeto(2500)

totalAnyo = miSueldo * 12

print(f"Este año voy a ganar neto {totalAnyo}")


# bucles
# while y el for
# while es un bucle que se ejecuta mientras se cumpla una condición
def geometrica(inicio, razon, limite):
    while inicio < limite:
        inicio *= razon
    return inicio


print(geometrica(1, 2, 500))


# cogemos cualquier número, si es par dividimos entre 2 si impar *3+1

def serieAl1(numero):
    lista = [numero]
    while numero != 1:
        if numero % 2 == 0:
            numero = numero / 2
        else:
            numero = numero * 3 + 1
        lista.append(numero)
    return lista


print(serieAl1(4500))

# for nos permite recorrer 'iterables' ¿QUé es un iterable?
# Elementos de python que se pueden recorrer
# Una cadena se puede recorrer letra a letra
for letra in "hola":
    print(letra)

# Una lista se puede recorrer elemento a elemento
for elemento in [4, 2, 7, 9, 6]:
    print(elemento)

# Puedo crear rangos de números consecutivos con 'range'

for i in range(8):  # 0..7
    print(i)

for i in range(2, 8):  # 2..7
    print(i)

for i in range(2, 8, 2):  # 2,4,6
    print(i)

for i in range(7, 0, -1):  # 7,6,5,4,3,2,1
    print(i)

# Con esto de los rangos consecutivos también puedo hacer el repetir una acción
# un número determinado de veces

# Imprime "hola" 5 veces. En este caso no nos importa el valor de i, simplemente hacer algo 5 veces
for i in range(5):
    print("hola")


# Las cadenas tienen una serie de funciones para saber si tienen una subcadena, pasar mayúsculas/minúsculas
# obtener subcadenas con el 'slicing', etcétera

def fragmentos(cadena):
    resultado = []
    for i in range(len(cadena)):
        resultado.append(cadena[0:i])
    return resultado


print(fragmentos("anastasia"))

# Listas: colecciones de elementos de cualquier tipo
lista = [1, 2, 5, 2, "hola", True]


# Se pueden recorrer con un for como hemos visto antes y tienen una serie de funciones
# para insertar, añadir, repetir, etcétera

def crearConsecutiva(veces):
    lista = []
    for i in range(veces):
        lista.append(i)
    return lista


print(crearConsecutiva(10))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]