sueldo = 2500

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