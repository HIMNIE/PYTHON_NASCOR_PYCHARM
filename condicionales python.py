# Estructura de control: Nos permite definir el flujo del programa
# if : comprobar una condición y si se cumple se ejecuta un código
# y, opcionalmente, si no se cumple, se ejecuta otro

edad = int(input("Dime tu edad"))

if edad >= 18:
    print("Bienvenido a la web")
    print("Eres bienvenido/a")
    print("Disfruta del contenido")
else:
    print("Eres menor de edad")
    print("Introduce un codigo de autorización si quieres acceder")
    codigo = input("Dime el codigo")
    if codigo == "1234":
        print("Bienvenido")
    else:
        print("Código incorrecto")

print("Esto está fuera del if y se ejecuta tanto si se cumple la condición como si no")

# Comparaciones
# >, >=, <, <= , ==, !=

# La igualdad se utilizan dos signos =
if edad == 18:
    print("Bienvenido a la mayoría de edad")

# Para diferente exclamación e igual !=
if edad != 18:
    print("No tienes 18 años")

# Recordad que vimos los operadores booleanos
# and, or, not

if edad >= 18 and edad <= 25:
    print("Tienes descuento de carnet joven (entre 18 y 25)")

if edad < 18 or edad > 65:
    print("Tienes descuento de niño o jubilado (menor de 18 o mayor de 65")

# recordad la precedencia de los operadores, el and va primero

if edad < 18 or edad > 20 and edad < 30:
    print("Esto se cumple si la edad es menor de 18")
    print("O la edad está entre 20 y 30")

# Recordad que si dudamos podemos usar paréntesis, que son gratis:
if edad < 18 or (edad > 20 and edad < 30):
    print("Esto se cumple si la edad es menor de 18")
    print("O la edad está entre 20 y 30")

if not edad >= 18:
    print("Eres menor")
if edad < 18:
    print("Es lo mismo")

# Mini ejercicio planteado
# Vamos a hacer un if que nos de un descuento si la edad es 40 o 50
