# Definir una función a la que le pasamos dos números y nos devuelve el mayor

# 1.- QUe parámetros necesitamos
# 2.- Que devolvemos
# 3.- El codigo para obtener ese resultado

# dos números, los podemos llamar a y b
# devolvemos otro número, que es el mayor

def mayor(a, b):
    if a > b:
        return a
    else:
        return b


a = int(input("Dime un número "))
b = int(input("Dime otro número "))
print(f"El mayor de {a} y {b} es {mayor(a, b)}")
