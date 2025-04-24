# Ejercicio 1: Acceso a una fiesta
# Un usuario puede entrar a una fiesta si es mayor de 18 años y tiene entrada VIP o es invitado.

# Completa el código para imprimir “Acceso permitido” o “Acceso denegado”:

edad = 20
vip = False
invitado = True

# Tu condición va aquí:
if edad >= 18 and (vip or invitado):
    print("Acceso permitido")
else:
    print("Acceso denegado")





#🧪 Ejercicio 2: Validación de login
#Un sistema da acceso si el usuario es "admin" y la clave es "1234", pero no está bloqueado.

usuario = "admin"
clave = "1234"
bloqueado = False

# Tu condición:
if usuario == "admin" and clave=="1234" and not bloqueado:
    print("Login exitoso")
else:
    print("Acceso denegado")
#🧪 Ejercicio 3: Acceso a descuentos
#Un cliente tiene descuento si es mayor de 65 años o si tiene carnet de estudiante válido y es mayor de 18.

edad = 19
tiene_carnet = True

# Tu condición:
if  edad > 65 or (tiene_carnet and edad >18):
    print("Tiene descuento")
else:
    print("No tiene descuento")
##🧪 Ejercicio 4: Evaluación académica
#Un estudiante aprueba si su nota es mayor o igual a 6 y no está inhabilitado por asistencia.

nota = 6.5
asistencia_suficiente = True

# Tu condición:
if nota>=6 and asistencia_suficiente:
    print("Aprobado")
else:
    print("Reprobado")
#🧪 Ejercicio 5: Uso del operador not
#Muestra un mensaje si el usuario no ha aceptado los términos:

acepta_terminos = False

if  not acepta_terminos:
    print("Debes aceptar los términos para continuar")



#Ejercicios IF

# Escribe un programa que solicite al usuario su edad y determine si es menor o
# igual a 18 años. Si es menor o igual a 18 años, muestra el mensaje “Eres menor de edad”,
# de lo contrario, muestra “Eres mayor de edad”.

edad=int(input("cual es tu edad "))
if edad<=18:
    print("Eres menor de edad")
else:
    print("Eres mayor de edad")


# Crea un programa que pida al usuario dos números y determine
# cuál es el mayor de los dos números. Si son iguales,
# muestra un mensaje que indique que los números son iguales.

PrimerNumero=float(input("ingresar el primer numero"))
SegundoNumero=float(input("ingresar el segundo numero"))

if PrimerNumero > SegundoNumero:
    print("El primer número es mayor.")
elif SegundoNumero > PrimerNumero:
    print("El segundo número es mayor.")
else:
    print("Los dos números son iguales.")


# Desarrolla un programa que pida al usuario un número entero y
# determine si es par o impar. Si es par, muestra
# “Es un número par”, si es impar, muestra “Es un número impar”.


Numero=int(input("ingresar un numero"))
if Numero%2 == 0:
    print("es un numero Par")
else:
    print("es un numer impar")


# Escribe un programa que solicite al usuario su calificación en un examen
# y determine si ha aprobado o reprobado. Si la calificación es igual o superior a 60,
# muestra “Aprobado”, de lo contrario, muestra “Reprobado”.


Calificacion=float(input("cual es tu calificacion en tu examen"))

if Calificacion >= 60:
    print("Aprobado")
else:
    print("reprobado")

#SOLUCION DEL PROF :

# Escribe un programa que solicite al usuario su edad y determine si es menor o
# igual a 18 años. Si es menor o igual a 18 años, muestra el mensaje
# “Eres menor de edad”, de lo contrario, muestra “Eres mayor de edad”.

edad = int(input("Introduce tu edad"))

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

# Crea un programa que pida al usuario dos números y determine cuál es el mayor
# de los dos números. Si son iguales, muestra un mensaje que indique que los números
# son iguales.

num1 = float(input("Dime el primer número"))
num2 = float(input("Dime el segundo número"))

if num1 > num2:
    print(f"El mayor es {num1}")
    print("El mayor es", num1)
    print("El mayor es" + str(num1))
elif num2 > num1:
    print(f"El mayor es {num2}")
else:
    print("Son iguales")

# Desarrolla un programa que pida al usuario un número entero y determine si es par
# o impar. Si es par, muestra “Es un número par”, si es impar, muestra
# “Es un número impar”.

num = float(input("Dime un número"))
if num % 2 == 0:
    print(f"El numero {num} es par")
else:
    print(f"El numero {num} es impar")

# Escribe un programa que solicite al usuario su calificación en un examen y
# determine si ha aprobado o reprobado. Si la calificación es igual o superior
# a 60, muestra “Aprobado”, de lo contrario, muestra “Reprobado”.

nota = float(input("Dime tu calificación"))
if nota >= 60:
    print(f"Estás aprobado")
else:
    print(f"Estás suspendido")

# Un usuario puede entrar a una fiesta si es mayor de 18 años y tiene entrada VIP o es invitado.

edad = 20
vip = False
invitado = True

# Tu condición va aquí:
if edad >= 18 and (vip or invitado):
    print("Acceso permitido")
else:
    print("Acceso denegado")

# Un sistema da acceso si el usuario es "admin" y la clave es "1234",
# pero no está bloqueado.

usuario = "admin"
clave = "1234"
bloqueado = False

# Tu condición:
if usuario == "admin" and clave == "1234" and not bloqueado:  # bloqueado==False
    print("Login exitoso")
else:
    print("Acceso denegado")

# Un cliente tiene descuento si es mayor de 65 años o si tiene
# carnet de estudiante válido y es mayor de 18.

edad = 19
tiene_carnet = True

# Tu condición:
if edad > 65 or (tiene_carnet and edad > 18):
    print("Tiene descuento")
else:
    print("No tiene descuento")

# Un cliente tiene descuento :
# su edad está entre 60 y 80: edad>=60 and edad<=80
# tiene carnet y más de 18 años: tiene_carnet and edad>=18
# no tiene carnet y es menor de 10 años: not tiene_carnet and edad<10
# las tres condiciones estarán unidas con un or
edad = 19
tiene_carnet = True

# Tu condición:
# if edad>=60 and edad<=80 or tiene_carnet and edad>=18 or not tiene_carnet and edad<10:
if (edad >= 60 and edad <= 80) or (tiene_carnet and edad >= 18) or (not tiene_carnet and edad < 10):
    print("Tiene descuento")
else:
    print("No tiene descuento")

# Un estudiante aprueba si su nota es mayor o igual a 6 y
# no está inhabilitado por asistencia.

nota = 6.5
asistencia_suficiente = True

# Tu condición:
if nota >= 6 and asistencia_suficiente:
    print("Aprobado")
else:
    print("Reprobado")

# Muestra un mensaje si el usuario no ha aceptado los términos:

acepta_terminos = False

if not acepta_terminos:
    print("Debes aceptar los términos para continuar")

