import datetime

ahora = datetime.datetime.now()

anio_actual = ahora.year
anio_actual = 2025
anio_nacimiento = int(input("Dime tu año de nacimiento"))

print(f"Este año tendrás {anio_actual - anio_nacimiento} años")

# Calcular el área de un triángulo
base = float(input("Dime la base"))
altura = float(input("Dime la altura"))
area = base * altura / 2
print("El área es ", area)
# saber hacer esto es importante porque puede ser que queramos
# almacenar el valor, no imprimirlo
print("El área es " + str(area))
print(f"El área es {area}")

# Pido el número
numero = int(input("Dime un numero del 10 al 99"))
decenas = numero // 10
unidades = numero % 10
suma = decenas + unidades
print("La suma es ", suma)

# Pido los minutos
total_minutos = int(input("Dime cuantos minutos"))

# calculo horas y minutos
horas = total_minutos // 60
minutos = total_minutos % 60

# muestro
print(f"{horas} horas y {minutos} minutos")