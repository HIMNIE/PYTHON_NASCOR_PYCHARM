import random
import datetime

# Cread una función tiradaDado que nos devuelva un número aleatorio del 1 al 6
def tiradaDado():
    return random.randint(1, 6)
print(tiradaDado())



# Cread una función que nos devuelva al azar una provincia de Cataluña
def provinciaCatalunya():
    provincias = ["Barcelona", "Girona", "Lleida", "Tarragona"]
    return random.choice(provincias)


print(provinciaCatalunya())



# Cread una función que nos devuelva el año actual

def anioActual():
    return datetime.date.today().year


print(anioActual())




# Cread una función que nos devuelva True si hoy es viernes y false en caso contrario
def esViernes():
    return datetime.date.today().weekday() == 4  # 0 = lunes, 4 = viernes


print(esViernes())






# Cread una función que nos devuelva la fecha actual en formato día/mes/año
def fechaActual():
    hoy = datetime.date.today()
    return hoy.strftime("%d/%m/%Y")


print(fechaActual())

#solucion del prof
import datetime
import random


# Cread una función tiradaDado que nos devuelva un número aleatorio del 1 al 6

def tiradaDado(limite=6):
    return random.randint(1, limite)


for i in range(10):
    print(tiradaDado())


# Cread una función que nos devuelva al azar una provincia de Barcelona
def provinciaAzar():
    provincias = ["Barcelona", "Tarragona", "Lleida", "Girona"]
    return random.choice(provincias)


for i in range(10):
    print(provinciaAzar())


# Cread una función que nos devuelva el año actual
def anyoActual():
    return datetime.date.today().year


print(anyoActual())


# Cread una función que nos devuelva True si hoy es viernes y false en caso contrario
def esViernes():
    return datetime.date.today().weekday() == 4  # 0 lunes hasta 6 domingo


print(esViernes())


# Cread una función que nos devuelva la fecha actual en formato día/mes/año

def fechaActual():
    return datetime.date.today().strftime("%d/%m/%Y")


print(fechaActual())


# Cread una función que nos devuelva el siguiente día laborable a partir de hoy
def siguienteLaborable():
    fecha = datetime.date.today()
    fecha += datetime.timedelta(days=1)
    while fecha.weekday() > 4:
        fecha += datetime.timedelta(days=1)
    return fecha


def siguienteLaborable2():
    fecha = datetime.date.today()
    fecha += datetime.timedelta(days=1)
    if fecha.weekday() > 4:
        fecha += datetime.timedelta(days=(7 - fecha.weekday()))
    return fecha


print(siguienteLaborable2())
