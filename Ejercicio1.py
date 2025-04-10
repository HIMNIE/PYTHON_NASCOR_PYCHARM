#Ejercicio 1: Cuantos años cumples este año

#Escribe un programa que solicite al usuario su año de nacimiento y calcule la edad que tendrá a finales de este año

fechaNacimiento=input("tu fecha de nacimiento?")
print(f"tu fecha nacimiento {int(fechaNacimiento)}")
fechaActual=2025
print(f"Tu edad {int(fechaActual)-int(fechaNacimiento)}")

#Escribe un programa que solicite al usuario una cantidad en dólares y
# la convierta a euros utilizando una tasa de cambio fija (1 dolar=0,93 €).

cantidadEuro=input("Ingresa la cantidad que quieres cambiar")
a=0.93
print(f"la cantidad total a recibir {float(cantidadEuro)*a:.2f}")


#Ejercicio 3: Cálculo del Índice de Masa Corporal (IMC)

#El Índice de Masa Corporal (IMC) se calcula utilizando la siguiente fórmula:

#[IMC = \frac{peso(kg)}{altura(m)^2}]
#IMC =peso / altura**2

#Escribe un programa en Python que solicite al usuario su peso en kilogramos y su altura en metros, luego calcule y muestre su IMC.

#Paso 1: Solicitar peso y altura al usuario.
#Paso 2: Calcular el IMC usando la fórmula.
#Paso 3: Mostrar el resultado.

#Aquí tienes un ejemplo de cómo podrías estructurar el código:
# Solicitar datos al usuario
peso =float( input("tu peso?"))
altura =float(input("tu altura?"))


# Calcular el IMC
imc=peso/altura**2

# Mostrar el resultado
print(f" tu IMC {imc:.2f}")



#Ejercicio 4: Conversión de Temperatura

#Escribe un programa que convierta una temperatura en grados Celsius a grados Fahrenheit utilizando la siguiente fórmula:

#[Fahrenheit = (Celsius * 9/5) + 32]

#Paso 1: Solicitar la temperatura en grados Celsius al usuario.
#Paso 2: Calcular la temperatura equivalente en grados Fahrenheit.
#Paso 3: Mostrar el resultado.

#Aquí tienes un ejemplo de cómo podrías estructurar el código:

# Solicitar la temperatura en grados Celsius
Celsius = float(input("ingresa la temperatura en grados Celsius"))

# Calcular la temperatura en grados Fahrenheit
fahrenheit = (Celsius * 9/5) + 32

# Mostrar el resultado
print(f"la temperatura en fahrenheit{fahrenheit:2f}")


#Ejercicio 5: Calcular el área de un triángulo

#Enunciado:
#Escribe un programa que pida la base y la altura de un triángulo y calcule su área.

#Esquema de solución:

#Pedir al usuario la base (base) y la altura (altura).
#Usar la fórmula del área: area = (base * altura) / 2.
#Mostrar el resultado.

base=float(input("ingresa la base de triangulo"))
altura=float(input("ingresa la altura de triangulo"))
area=(base*altura)/2
print(f"el resultado es {area:2f}")



#Ejercicio 6: Suma de dígitos de un número de 2 cifras

#Enunciado:
#Pide al usuario un número de dos cifras y muestra la suma de sus dígitos.

#Esquema de solución:

#Obtener un número entero entre 10 y 99.
#Separar las cifras usando división entera y módulo:
#decena = num // 10, unidad = num % 10.
#Sumar ambas cifras.

NumeroEntero=int(input("ingresar un numero entero entre 10 y 99"))
decena=NumeroEntero//10
unidad=NumeroEntero%10

print(f" la suma de las cifras es : {decena+unidad}")

#Ejercicio 7: Conversión de minutos a horas y minutos

#Enunciado:
#Dado un número de minutos, convierte ese valor a horas y minutos.

#Esquema de solución:

#Pedir al usuario los minutos (total_minutos).
#Calcular las horas con horas = total_minutos // 60.
#Calcular los minutos restantes con minutos = total_minutos % 60.

