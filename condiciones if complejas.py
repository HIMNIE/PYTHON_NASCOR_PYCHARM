sueldo = 500

irpf = 15

# Tenemos esta tabla: hasta 2000 10%, hasta 3000 12% hasta 5000 15%  resto 25%

if sueldo < 2000:
    irpf = 10
else:
    if sueldo < 3000:
        irpf = 12
    else:
        if sueldo < 5000:
            irpf = 15
        else:
            irpf = 25

print(irpf)

# Lo de arriba se puede reescribir usando la estructura elif
if sueldo < 2000:
    irpf = 10
elif sueldo < 3000:
    irpf = 12
elif sueldo < 5000:
    irpf = 15
else:
    irpf = 25

print(irpf)

# Sintaxis básica: si se cumple la condición se ejecuta lo que está dentro del if

if sueldo < 1000:
    print("El sueldo no puede ser menos que el SMI")

    # esto está dentro del if
    print("Se viene inspección")

# esto está fuera del if
print(sueldo)

# sintaxis con else: si se cumple se ejecuta lo del if y si no, lo del else

if sueldo > 3000:
    print("Sueldazo")
else:
    print("Sueldo común")

# sintaxis con elif
# cada elif plantea una nueva condición que se evalua, como si fuera un if
# pero queda más claro

if sueldo < 1000:  # Los sueldos menores de 1000
    print("Inspeccion")
elif sueldo < 2000:  # Los menores de 2000
    print("Sueldo bajo")
elif sueldo < 4000:  # De 4000
    print("Buen sueldo")
else:  # Los mayores de 4000 (else del último if)
    print("Sueldazo")

# Las condiciones pueden ser complejas y combinar operadores

if sueldo < 1000 or sueldo > 9000:  # Aquí combino dos condiciones con un or
    print("Sueldo incorrecto")

# Pueden ser lo complejas que hagan falta
if (sueldo < 1000 or sueldo > 9000) and sueldo % 10 == 0:
    print("Sueldo incorrecto que acaba en cero")

# Puedo tener if dentro de otros ifs (ifs anidados)
# Puede ser  lo complicado que haga falta
if sueldo > 5000:
    if sueldo % 10 == 0:
        print("Sueldo mayor de 5000 que acaba en 0")
    else:
        print("Sueldo mayor de 5000 que NO acaba en 0")
else:
    print("Sueldo menor de 5000")

# Veamos un ejemplo de esto
# Calcular el precio de envío de un paquete
# Tenemos lo siguiente:
# Barcelona: 5€ da lo mismo el peso
# Girona o Tarragona 5€ si pesa menos de 10 kilos y 10€ si pesa más
# Resto de ciudades: hasta 10k 5€, hasta 20k 10€, hasta 30k 15 € resto 30€

ciudad = "Logroño"
peso = 12

precio = 0

if ciudad == "Barcelona":
    precio = 5
else:
    if ciudad == "Girona" or ciudad == "Tarragona":
        # calculo los precios
        if peso < 10:
            precio = 5
        else:
            precio = 10
    else:
        if peso < 10:
            precio = 5
        elif peso < 20:
            precio = 10
        elif peso < 30:
            precio = 15
        else:
            precio = 30

print(precio)