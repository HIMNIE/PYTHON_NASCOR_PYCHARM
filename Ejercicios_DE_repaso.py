# Cread una función a la que le pasamos un número y nos lo devuelva multiplicado por 3
# triplicar(5) -> 15

def triplicar(numero):

    return (numero) *3
print(triplicar(5))

# Cread una función a la que le pasamos una cadena y una letra y nos devuelva True si la cadena tiene esa letra
# tieneLetra("hola que tal","t")->true
def tieneLetra(cadena,letra):
    return letra in cadena
print(tieneLetra("hola que tal","t" ))
print(tieneLetra("hola que tal","k" ))




# Cread una función a la que le pasamos una ciudad y un importe y nos devuelve los gastos de envío
# acordes a la siguiente: Barcelona: 0  Tarragona o Girona con importe < 500 5€, resto 0€ Resto de ciudades 6€
# gastosEnvio("Barcelona",50)->0 gastosEnvio("Logroño",50)->6
def gastosEnvio(ciudad,importe):
    if ciudad=="Barcelona" :
        return 0
    elif ciudad=="Girona" or ciudad=="Tarragona" and importe<500:
        return 5
    else :
        return 6
print(gastosEnvio("Barcelona",50))
print(gastosEnvio("Logroño",50))


# cread una función que nos diga si alguien puede subir a una atracción de acuerdo a su edad y su altura
# si tiene más de 18 años o una altura superior a 135 cm puede subir, en caso contrario no
# puedeSubir(20,130)->True puedeSubir(10,140)->True puedeSubir(10,130)->False

def puedeSubir(edad,altura):
    if edad>18 or altura>135:
        return True
    else:
        return False
print(puedeSubir(20,130))
print(puedeSubir(10,140))
print(puedeSubir(10,130))

