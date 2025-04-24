# Ejercicios While
# 1.- Pedir un número al usuario y hacer una cuenta regresiva desde ese número
from ctypes.macholib.dyld import DEFAULT_LIBRARY_FALLBACK

num1=0
num=float(input("Ingresar un numero"))
while num1 < num :
    print(num)
    num-=1


# 2.- Sumar todos los números pares del 1 al 100 (incluidos)
num2=1
suma=0
while num2<=100 :
    if num2%2==0 :
        #suma+=num2
        suma=suma+num2
    #num2+=1
    num2=num2+1
print(f"la suma de los  numero pares del 1 al 100 es : {suma}")




# 3.- Mostrar la tabla de multiplicar del 7
num3=7
num4=1
while  num4<=10 :

    num5=num3*num4
    print(f"{num3}*{num4}={num5}")
    num4+=1

# 4.- Pedir números al usuario hasta que introduzca un 0. Mostrar el número mayor

# mayor= num6
# num6=int(input("ingresar numeros"))
# while num6 != 0:
#     if num6>mayor:
#         mayor=num6
#
#     print(f"el numero mayor ingresado fue {mayor}")

#
# 5.- Escribir un programa que pida nombres y salga cuando escribamos la palabra ‘salir’
palabra = input("Ingresar nombres: ")

while palabra != "salir":
    print(palabra)
    palabra = input("Ingresar otros nombres: ")

print("Ya saliste.")



#
# 6.- Modificar el programa anterior para que salga cuando repitamos el nombre

nombre = input("Ingresar nombres: ")
anterior = None

while nombre != anterior:
    anterior=nombre
    nombre = input("Ingresar otros nombres: ")

print("Ya saliste.")

#
# 7.- Escribir un programa que calcule la suma de todos los múltiplos de 5 menores de 100

num33=5
num44=1
sumar=0
while  num33*num44<=100 :

    num55=num33*num44
    print(f"{num33}*{num44}={num55}")
    sumar=suma+num55
    num44+=1
print(f"la suma de los numeros {sumar}")
#
# 8.- Pedir un número y calcular el factorial (factorial de 5. 5*4*3*2*1)
#
# Pedir un número al usuario
numero = int(input("Ingresar un número para calcular su factorial: "))

# Inicializar las variables
factorial = 1
contador = 1

# Usar un bucle while para calcular el factorial
while contador <= numero:
    factorial *= contador  # Multiplica el valor de factorial por el contador
    contador += 1  # Incrementa el contador

# Mostrar el resultado
print(f"El factorial de {numero} es: {factorial}")


# 9.- Mostrar los cuadrados de los números del 1 al 10

# Inicializar el contador
i = 1

# Usar un bucle while para recorrer del 1 al 10
while i <= 10:
    cuadrado = i ** 2  # Calcula el cuadrado del número
    print(f"El cuadrado de {i} es {cuadrado}")
    i += 1  # Incrementar el contador



    #================================SOLUCION DEL PROFESOR=========================================

# 1.- Pedir un número al usuario y hacer una cuenta regresiva desde ese número

# Pedir un número
numero = int(input("Dame un número entero"))

# Contar desde el número hasta el cero
while numero >= 0:
    # Imprimir esa 'cuenta' para ver la regresión
    print(numero)
    numero = numero - 1  # numero-=1

# Sumar todos los números pares del 1 al 100 (incluidos)

# ¿Se averiguar todos los números pares del 1 al 100?
# ¿Se mostrar todos los número del 1 al 100?
# ¿Se cuando un número es par o impar?
# ¿Se sumar en una variable?
numero = 1
suma = 0
while numero <= 100:
    if numero % 2 == 0:
        suma += numero
    numero += 1
print(suma)

numero = 0
suma = 0
while numero <= 100:
    suma += numero
    numero += 2
print(suma)

# Mostrar la tabla de multiplicar del 7
# 1x7=7 2x7=14 3x7=21....10x7=70
# Esto SI es un bucle
# Con qué numero empieza el bucle y con cual acaba
# Del 1 al 10
numero = 1
while numero <= 10:
    print(f"{numero} x 7 = {numero * 7}")
    numero += 1

# Pedir números al usuario hasta que introduzca un 0. Mostrar el número mayor
# Pedir un número al usuario (lo sabemos)
# Saber un bucle hasta que un valor sea 0
# Saber cual es el mayor de una serie de números

# Pido un número al usuario
numero = int(input("Dame un número entero"))
# De momento me lo quedo. Lo que es correcto es el mayor
mayor = numero
# Mientras el usuario no me introduzca un 0, voy pidiendo números
while numero != 0:
    numero = int(input("Dame un número entero"))
    # Si el número que me ha dado el usuario es mayor que el que ya tenía, pues me quedo con él
    if numero > mayor:
        mayor = numero
print(mayor)

# Escribir un programa que pida nombres y salga cuando escribamos la palabra ‘salir’
# Pido un nombre
# bucle hasta que digan salir

nombre = ""

while nombre != "salir":
    nombre = input("Dime un nombre")

nombre = ""
lista = ""
while nombre != "salir":
    nombre = input("Dime un nombre")
    lista += nombre + " "
print(lista)

# Modificar el programa anterior para que salga cuando repitamos el nombre
# cuando el nombre que me introducen es igual al anterior

nombre = ""
anterior = "#"
while nombre != anterior:
    anterior = nombre
    nombre = input("Dime un nombre")

# Escribir un programa que calcule la suma de todos los múltiplos de 5 menores de 100

numero = 0
suma = 0
while numero <= 100:
    suma += numero
    numero += 5
print(suma)

# Pedir un número y calcular el factorial (factorial de 5. 5*4*3*2*1)
# Pido un número
# Hago un bucle desde donde hasta donde?
# Empiezo en el número y acabo en el 1

numero = int(input("Dime un número"))
factorial = 1
while numero >= 1:
    factorial = factorial * numero
    numero -= 1

print(factorial)

# Mostrar los cuadrados de los números del 1 al 10
# bucle del 1 al 10
numero = 1
while numero <= 10:
    print(numero ** 2)
    numero += 1
