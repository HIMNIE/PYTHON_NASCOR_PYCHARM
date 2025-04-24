# 1.- Pedir un número al usuario y mostrar la suma de todos los números hasta ese número
# 5->1+2+3+4+5=15

# 2.- Pedir una cadena al usuario y escribir si tiene o no tiene alguna 'ñ'
# 'Logroño'-> Tiene 'Barceloba'->No tiene

# 3.- Pedir un número al usuario y escribir su tabla de multiplicar

# 4.- Pedir dos números al usuario (mínimo y máximo) y calcular la suma entre los dos
# 2 y 5 ->2+3+4+5=14

# 5.- Pedir una cadena al usuario y escribir una cadena sin la letra 'a'
# 'patata' -> ptt 'ayer se fue' -> 'yer se fue'


#SOLUCION DEL PROF
# 1.- Pedir un número al usuario y mostrar la suma de todos los números hasta ese número
# 5->1+2+3+4+5=15

numero = int(input("Dime un número"))
suma = 0
for i in range(1, numero + 1):
    suma += i
print(suma)

# 2.- Pedir una cadena al usuario y escribir si tiene o no tiene alguna 'ñ'
# 'Logroño'-> Tiene 'Barceloba'->No tiene

cadena = input("Dime una cadena")
tiene = False
for letra in cadena:
    if letra == "ñ":
        tiene = True

if tiene:
    print("Tiene Ñ")
else:
    print("No hay ninguna Ñ")

# 3.- Pedir un número al usuario y escribir su tabla de multiplicar

numero = int(input("Dime el número "))
for i in range(1, 11):
    print(f"{i} x {numero} = {i * numero}")

# 4.- Pedir dos números al usuario (mínimo y máximo) y calcular la suma entre los dos
# 2 y 5 ->2+3+4+5=14
minimo = int(input("Dime el primer número "))
maximo = int(input("Dime el segundo número "))
suma = 0
for i in range(minimo, maximo + 1):
    suma += i
print(suma)

# 5.- Pedir una cadena al usuario y escribir una cadena sin la letra 'a'
# 'patata' -> ptt 'ayer se fue' -> 'yer se fue'
cadena = input("Dime una cadena ")
resultado = ""
for letra in cadena:
    if letra != "a":
        resultado += letra
print(resultado)