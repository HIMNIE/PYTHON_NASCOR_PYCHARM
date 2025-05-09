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
