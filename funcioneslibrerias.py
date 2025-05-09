# librerías externas
# Conjunto de funciones que nos permiten ampliar las capacidades de python
import random

# Por ejemplo la librería random para obtener numeros aleatorios

# función random me devuelve un número aleatorio entre 0 y 1 sin llegar al 1
numero_aleatorio = random.random()
print(numero_aleatorio)  # Por ejemplo, 0.5738124566

numero_aleatorio = random.randint(1, 6)  # Un número aleatorio entre 1 y 6 (incluidos).
print(numero_aleatorio)  # Por ejemplo, 4

colores = ["rojo", "verde", "azul", "amarillo"]
color_aleatorio = random.choice(colores)
print(color_aleatorio)  # Por ejemplo, "verde"

cartas = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
random.shuffle(cartas)
print(cartas)  # La lista 'cartas' ahora estará en un orden aleatorio.

def tiradaMoneda():
    opciones=['cara','cruz']
    return random.choice(opciones)

for i in range(10):
    print(tiradaMoneda())

import math

print(math.pi)
print(math.e)
print(math.sqrt(1024))
print(math.factorial(6))
print(math.log2(1024))
# Importar el módulo datetime
import datetime

# Obtener la fecha y hora actual
ahora = datetime.datetime.now()
print("Fecha y hora actual:", ahora)

# Obtener la fecha actual
fecha_actual = datetime.date.today()
print("Fecha actual:", fecha_actual)

# Obtener el año, mes y día de una fecha
print("Año:", fecha_actual.year)
print("Mes:", fecha_actual.month)
print("Día:", fecha_actual.day)

# Crear una fecha específica
fecha_personalizada = datetime.date(2023, 10, 3)
print("Fecha personalizada:", fecha_personalizada)

# Crear una fecha y hora específicas
fecha_hora_personalizada = datetime.datetime(2023, 10, 3, 14, 30)
print("Fecha y hora personalizada:", fecha_hora_personalizada)

# Formatear una fecha como una cadena de texto
fecha_formateada = fecha_actual.strftime("%d/%m/%Y")
print("Fecha formateada:", fecha_formateada)

# Crear una fecha a partir de una cadena de texto formateada
fecha_desde_cadena = datetime.datetime.strptime("03/10/2023", "%d/%m/%Y")
print("Fecha desde cadena:", fecha_desde_cadena)

# Realizar operaciones con fechas
diferencia_dias = fecha_personalizada - fecha_actual
print("Diferencia en días:", diferencia_dias.days)

# Obtener la fecha y hora en el futuro o pasado
dias_adelante = datetime.timedelta(days=7)
fecha_futura = fecha_actual + dias_adelante
print("Fecha en una semana:", fecha_futura)

# Obtener el día de la semana (0=Lunes, 6=Domingo)
print("Día de la semana:", fecha_actual.weekday())

# Crear un intervalo de tiempo específico
intervalo_tiempo = datetime.timedelta(hours=2, minutes=30)
print("Intervalo de tiempo:", intervalo_tiempo)

# Obtener la hora actual
hora_actual = datetime.datetime.now().time()
print("Hora actual:", hora_actual)

# Crear una hora específica
hora_personalizada = datetime.time(14, 30)
print("Hora personalizada:", hora_personalizada)

# Combinar una fecha y una hora
fecha_hora_combinada = datetime.datetime.combine(fecha_actual, hora_personalizada)
print("Fecha y hora combinadas:", fecha_hora_combinada)

# x**2 + 3x +1
def miFuncion(num):
    return num ** 2 + 3 * num + 1


print(math.sin(math.pi * 1.5))
print(math.sin(0))
