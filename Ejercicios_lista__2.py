# Definir el algoritmo
# Los pasos que vamos a implementar para resolver el problema
# La 'receta'
# Divide y vencerás: un problema grande se compone de otros más pequeños
# Lo primero es pensar ¿Cömo voy a resolver este problema?

# Cread una función a la que le pasamos una lista de números y nos devuelva una lista
# con el menor y el mayor
# menorMayor([3,1,8,5])->[1,8]

# Función que recibe una lista de números y devuelve una lista con el menor y el mayor
def menorMayor(lista):
    lista_ordenada = sorted(lista)       # Ordenamos la lista de menor a mayor
    menor = lista_ordenada[0]            # El primer elemento es el menor
    mayor = lista_ordenada[-1]           # El último elemento es el mayor
    return [menor, mayor]                # Devolvemos la lista con menor y mayor

# Ejemplo de uso
print(menorMayor([3, 1, 8, 5]))  # Resultado: [1, 8]



# Cread una función a la que le pasamos una lista de nombres y nos devuelve una lista
# con todos los nombres en minúsculas
# minusculas(["Ana","Pep","Iu"])->["ana","pep","iu"]

# Función que convierte todos los nombres de una lista a minúsculas
def minusculas(lista):
    resultado = []  # Lista donde guardamos los nombres en minúsculas
    for nombre in lista:  # Recorremos cada nombre de la lista
        resultado.append(nombre.lower())  # Convertimos a minúsculas y lo añadimos a la nueva lista
    return resultado  # Devolvemos la lista con todos los nombres en minúsculas

# Ejemplo de uso
print(minusculas(["Ana", "Pep", "Iu"]))  # Resultado: ['ana', 'pep', 'iu']


# Cread una función a la que le pasamos una lista de cadenas y nos devuelve una lista
# con las que tengan una longitud par
# longitudPar(["aa","bbb","cccc","ddddd"])->["aa","cccc"]

# Función que devuelve solo las cadenas que tienen una longitud par
def longitudPar(lista):
    resultado = []  # Lista para guardar las cadenas con longitud par
    for cadena in lista:  # Recorremos cada cadena de la lista
        if len(cadena) % 2 == 0:  # Si la longitud es par (divisible por 2)
            resultado.append(cadena)  # Añadimos la cadena a la nueva lista
    return resultado  # Devolvemos solo las cadenas con longitud par

# Ejemplo de uso
print(longitudPar(["aa", "bbb", "cccc", "ddddd"]))  # Resultado: ['aa', 'cccc']



#SOLUCION_DEL_PROF


# Definir el algoritmo
# Los pasos que vamos a implementar para resolver el problema
# La 'receta'
# Divide y vencerás: un problema grande se compone de otros más pequeños
# Lo primero es pensar ¿Cömo voy a resolver este problema?

# Cread una función a la que le pasamos una lista de números y nos devuelva una lista
# con el menor y el mayor
# menorMayor([3,1,8,5])->[1,8]

# Cual es el mayor y cual es el menor

# Esta solución es más fácil
def menorMayor(lista):
    ordenada = sorted(lista)
    return [ordenada[0], ordenada[-1]]


# Esta solución es más eficiente, porque ordenar es algo muy costoso
def menorMayor2(lista):
    menor = lista[0]
    mayor = lista[0]
    for numero in lista:
        if numero < menor:
            menor = numero
        if numero > mayor:
            mayor = numero
    return [menor, mayor]


# Esto de aquí hay que evitarlo: No se modifican los parámetros que pasamos
def menorMayor3(lista):
    lista.sort()
    menor = lista.pop(0)
    mayor = lista.pop(-1)
    return [menor, mayor]


print(menorMayor([3, 1, 8, 5]))
print(menorMayor2([3, 1, 8, 5]))

milista = [2, 1, 6, 8, 33, 4, 12, 25]
print(menorMayor3(milista))
print(milista)


# Cread una función a la que le pasamos una lista de nombres y nos devuelve una lista
# con todos los nombres en minúsculas
# minusculas(["Ana","Pep","Iu"])->["ana","pep","iu"]

# Tener un sitio donde guardar el resultado
# recorrer la lista
# como pasar una cadena a minúsculas
def minusculas(lista):
    resultado = []
    for elemento in lista:
        resultado.append(elemento.lower())
    return resultado


print(minusculas(["Ana", "Pep", "Iu"]))


# Cread una función a la que le pasamos una lista de cadenas y nos devuelve una lista
# con las que tengan una longitud par
# longitudPar(["aa","bbb","cccc","ddddd"])->["aa","cccc"]

# Tener un sitio donde guardar el resultado
# recorrer la lista
# Si la longitud es par, lo añado a la lista
def longitudPar(lista):
    resultado = []
    for elemento in lista:
        if len(elemento) % 2 == 0:
            resultado.append(elemento)
    return resultado


print(longitudPar(["aa", "bbb", "cccc", "ddddd"]))










def definirlafuncion(parametro1, parametros):
# Codigo que hace cosas
# 90% de las veces es:
# Defino una o varias variables para almacenar resultados
# recorro la lista
# dentro de ese recorrido aplico la lógica que me soluciona el problema


# devuelvo el resultado



