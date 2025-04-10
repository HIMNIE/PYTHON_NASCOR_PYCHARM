#suma y resta

a = 10
b = 5
print(a + b)   # 15
print(a - b)   # 5

# Multiplicación y división

print(3 * 4)   # 12
print(10 / 3)  # 3.333...

#División entera y módulo

print(10 // 3)  # 3 (parte entera)
print(10 % 3)   # 1 (resto)

#Potencias
print(2 ** 4)   # 16 (2 elevado a la 4)
print(9 ** 0.5) # 3.0 (raíz cuadrada de 9)

#Ejemplo combinado

x = 8
y = 3

print(f"Suma: {x + y}")
print(f"Resta: {x - y}")
print(f"Multiplicación: {x * y}")
print(f"División: {x / y}")
print(f"División entera: {x // y}")
print(f"Resto: {x % y}")
print(f"Potencia: {x ** y}")


#Errores comunes
#Dividir por 0 lanza un error:
print(5 / 0)  # ZeroDivisionError

#La división / siempre da float aunque los operandos sean enteros:
print(4 / 2)  # 2.0



precio = 80
personas = 7
print(precio / personas)
print(precio // personas)

print(2 ** 4)

# Modulo % Resto de la división
print(17 % 5)

# ¿Cómo saber si un número es par o impar?
# Si el módulo 2 es 0, es par
# si el módulo 2 es 1, es impar

print(8 % 2)  # 0, es par
print(81 % 2)  # 1, es impar

numero = 9
print(numero % 2)

print(numero % 3)
giro = 850
print(giro % 360)



a = 5
b = 10
print(a > 3 and b < 15)   # True (las dos condiciones se cumplen)
print(a > 3 and b < 5)    # False (solo una se cumple)


print(a > 3 or b < 5)     # True (una es verdadera)
print(a < 3 or b < 5)     # False (ninguna es verdadera)


activo = True
print(not activo)         # False
print(not (a < 3))        # True