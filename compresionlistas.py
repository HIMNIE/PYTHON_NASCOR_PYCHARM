# Hemos visto en muchos ejercicios que recorrer y procesar una lista es habitual
# En python tenemos la comprension de listas
# [expresión for elemento in iterable]

cuadrados = [x ** 2 for x in range(1, 10)]
print(cuadrados)

# Hace exactamente lo mismo que esto
cuadrados = []
for x in range(1, 10):
    cuadrados.append(x ** 2)

letrasdobles = [letra * 2 for letra in "hola que tal"]
print(letrasdobles)

notas = [4, 15, 7, 19, 12]
notas10 = [nota / 2 for nota in notas]
print(notas10)

notascopia = [nota for nota in notas]
print(notascopia)

# tabla de multiplicar del 7 (7,14,21,...,70)

tabla7 = [x * 7 for x in range(1, 11)]
print(tabla7)

# Añadir una condición: seleccionar lo elementos del iterable que cumplan una determinada condición
# [expresion for elementi in interable if condicion]

# Buscamos los que sean pares (x%2==0)
pares = [x for x in range(1, 11) if x % 2 == 0]
print(pares)

# Las cadenas de una determinada longitud
cadenas = ["a", "bb", "ccc", "dddd", "eeeeee", "fffffff"]
largas = [cadena for cadena in cadenas if len(cadena) > 4]
print(largas)

# Buscamos las notas aprobadas (>10) y además las transformamos
notas10aprobadas = [nota / 2 for nota in notas if nota >= 10]
print(notas10aprobadas)

# Operador ternario: Igual que un if pero en vez de controlar el flujo
# devuelve un valor dependiendo de la condicion
# valor_si_cierto if condicion else valor_si_falso

numero = 27

espar = "par" if numero % 2 == 0 else "impar"

print(espar)

if numero % 2 == 0:
    espar = "par"
else:
    espar = "impar"

ciudad = "Logroño"
envio = 5 if ciudad == "Barcelona" else 10
print(envio)  # 10


def calculoEnvio(ciudad):
    return 5 if ciudad == "Barcelona" else 10


print(calculoEnvio("Barcelona"))  # 5

# Podemos usar como expresión un operador ternario

notasCorte = ["Aprobada" if nota >= 10 else "Suspendida" for nota in notas]
print(notasCorte)

longitudes = ["corta" if len(cadena) < 4 else "larga" for cadena in cadenas]
print(longitudes)

# Todo junto

numeros = [1, 4, -5, 7, -2, 20]
# A los números positivos si es par lo duplicamos y si es impar lo elevamos al cuadrado

calculo = [numero * 2 if numero % 2 == 0 else numero ** 2 for numero in numeros if numero >= 0]
print(calculo)

# nucleo que es recorer una lista
# for elemento in iterable: for numero in numeros
# Parte derecha yo puedo poner una condición: ejemplo if numero>=0 (los positivos) [1,4,7,20]
# parte izquierda pongo una expresión puede ser numero en cuyo caso no hacemos ninguna transformación
calculo = [numero for numero in numeros if numero >= 0]
print(calculo)
# Una expresión sencilla, por ejemplo, elevar al cubo
calculo = [numero ** 3 for numero in numeros if numero >= 0]
print(calculo)

# Liarme la manta a la cabeza y usar un operador ternario, en este caso
# si es par duplicamos, si es impar elevamos al cubo
# en el operador ternario hacemos lo mismo, empezamos por el núcleo, la condición
# if numero%2==0
# en la parte derecha ponemos lo que devolvemos si NO se cumple la condición numero**2
# en la parte izquierda ponemos lo que devolvemos si SÍ se cumple numero*2
# numero * 2 if numero % 2 == 0 else numero ** 2
# Juntando todo obtengo lo siguiente:
calculo = [numero * 2 if numero % 2 == 0 else numero ** 2 for numero in numeros if numero >= 0]
print(calculo)

frases = ["hola", "que tal", "epanadiplosis", "Bu", "En un lugar de la mancha", "otorrinolaringologo"]

# Vamos a hacer un código que filtre las palabras con una longitud mayor de 4
# Si tienen un espacio dejamos la cadena, si no tienen ningún espacio ponemos "No es frase"
# yo empiezo por el núcleo que siempre es recorrer la lista
filtro = [frase for frase in frases]
# puesto que ni filtro ni pongo expresión lo siguiente me devuelve la propia lista
print(filtro)  # ["hola", "que tal", "epanadiplosis", "Bu", "En un lugar de la mancha", "otorrinolaringologo"]
# Aplico la condición, la longitud debe ser mayor de 4
filtro = [frase for frase in frases if len(frase) > 4]
print(filtro)  # ["que tal", "epanadiplosis",  "En un lugar de la mancha", "otorrinolaringologo"]
# Ahora tengo que construir el operador ternario que, si tiene un espacio me devuelve la frase
# Y si no lo tiene me devuelve "No hay frase2
# Empiezo por el núcleo
# if " " in frase
# Si se cumple: devuelvo frase
# Si no se cumple: devuelvo "No es frase"
# frase if " " in frase else "No es frase"
# Meto el operador ternario en lo que tenía antes
filtro = [frase if " " in frase else "No es frase" for frase in frases if len(frase) > 4]
print(filtro)  # ['que tal', 'No es frase', 'En un lugar de la mancha', 'No es frase']
