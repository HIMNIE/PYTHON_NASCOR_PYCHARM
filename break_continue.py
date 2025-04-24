for i in range(1, 100):
    print(i)
    if i == 16:
        break

cadena = input("Dime una cadena")
tiene = False
for letra in cadena:
    if letra == "ñ":
        tiene = True
        break

if tiene:
    print("Tiene Ñ")
else:
    print("No hay ninguna Ñ")

numero = int(input("Dime un número"))
esPrimo = True
for i in range(2, numero):
    if numero % i == 0:
        esPrimo = False
        break
if esPrimo:
    print(f"{numero} es primo")
else:
    print(f"{numero} no es primo")

# continue Se salta las instrucciones que hay a continuación y sigue con el bucle

numero = 100
suma = 0
for i in range(1, numero + 1):
    if i % 2 == 0:
        continue
    print(i)
    suma += i

cadena = input("Dime una cadena ")
resultado = ""
for letra in cadena:
    if letra == "a":
        continue
    resultado += letra
print(resultado)