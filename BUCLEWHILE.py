# La sintaxis es muy sencilla ejecutar algo mientras se cumple una condición:

# mientras condición sea cierta se ejecuta el código, cuando sea falsa salimos
# while condicion:
# código que se ejecuta

num = 0
while num < 10:
    print(num)
    num = num + 2
# CTRL + ALT + L: formatea el código

# Este código nos pide números y nos los suma, después nos muestra el resultado
#cuente la cantidad de numeros que se han introducido
suma = 0  #sumar cosas
cont=0 #contar cosas
num = -1
while num != 0:
    num = int(input("Dime un número (0 para salir) "))
    suma = suma + num
    cont +=1

    #le resto uno a cont para que no me cuente el 0 como numero
print(f"La suma es {suma} y has introducido {cont-1} numeros")

# Cuenta atrás
inicio = 10
while inicio >= 0:
    print(f"{inicio}...")
    inicio -= 1
print("¡Lanzamiento!")




# Árbol de navidad

arbol = "*"
tamanyo = 6
while tamanyo > 0:
    print(arbol)
    arbol += "*"
    tamanyo -= 1

# En general este es el esquema para repetir algo N veces
veces = 10
while veces > 0:
    # Aquí nuestro código
    veces -= 1


suma = 0
num = 1
while num <= 100:
    suma += num
    num += 1
print(suma)



