#podemos tener parametros por defecto o con valores predeterminados

def espar(numero):
    if numero %2 ==0:
        return True
    else:
        return False

suma=0

for i in range(0,101):
    if espar(i):
        suma+=i
print(suma)


# Podemos tener parámetros por defecto o con valores predeterminados

def saludo(nombre="Anónimo"):
    return "Hola " + nombre


ana = saludo("Ana")

anonim = saludo()  # Como no paso un valor a 'nombre' pone por defecto 'Anónimo'

print(ana, anonim)


def potencia(numero, exponente=2):
    return numero ** exponente  # En python para elevar un número a otro se usa ** numero^exponente


# suma 1+1+1+1+1  5*1 (multiplicación)
# multiplicación 5*5*5*5 5^4 (potencia)


print(potencia(2, 4))
print(potencia(8))  # Como no le pongo valor a 'exponente' le pone por defecto 2


# En la siguiente función vamos a hacer que la cantidad por defecto sea '2'
# Si yo pongo repetir("Ana")-> "AnaAna"

def repetir2(cadena, cantidad):
    return cadena * cantidad


# Que las funciones pueden llamar a otras funciones

def esPar(numero):
    # En general siempre que tenemos un if que devuelve true o false podemos devolver directamente la condición del if
    return numero % 2 == 0


def sumaPares(numero):
    suma = 0
    for i in range(0, numero + 1):
        if esPar(i):
            suma += i
    return suma


print(sumaPares(100))


def esVocal(letra):
    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
        return True
    else:
        return False


def contarVocales(cadena):
    # variable que acumula: en este caso lo que hago es contar
    contador = 0
    # Bucle para recorrer, en este caso recorro todas letras de la cadena
    for letra in cadena:
        # En letra tenemos todas las letras de la cadena
        # Llamamos a la función esVocal para saber si es vocal o no

        if esVocal(letra):
            # Si sí que es vocal, contamos uno
            contador += 1
    # devolvemos el resultado
    return contador


print(esVocal("a"))
print(esVocal("j"))

print(contarVocales("hola que tal"))  # 5


def esPrimo(numero):
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True


def mostrarPrimos(numero):
    resultado = "1"
    for i in range(2, numero + 1):
        if esPrimo(i):
            resultado += f",{i}"
    return resultado


print(esPrimo(100))
print(esPrimo(17))

print(mostrarPrimos(50))