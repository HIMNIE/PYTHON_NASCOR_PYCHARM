# Listas: conjunto de elementos sobre el que podemos realizar diferentes operaciones
# Tuplas: como las listas pero se pueden desempaquetar
# Diccionarios: Conjunto de pares clave, valor

notas = [1, 2, 3, 4]
tupla = (1, 2, 3)
diccionario = {
    "nombre": "Ana",
    "nota": 6
}

# En python todo esto se puede combinar

# Quiero guardar los datos de un alumno
alumno = {
    "nombre": "ana",
    "email": "ana@ana.es",
    "curso": "Python"
}
# Quiero guardar también las asignaturas, que son varias
alumno = {
    "nombre": "ana",
    "email": "ana@ana.es",
    "curso": "Python",
    "asignaturas": ["Programación", "Bases de datos"]
}

# Para cada asignatura, quiero guardar su nota y su profesor
alumno = {
    "nombre": "ana",
    "email": "ana@ana.es",
    "curso": "Python",
    "asignaturas": [{"nombre": "Programación", "nota": 7, "profesor": "JP"},
                    {"nombre": "Bases de datos", "nota": 8, "profesor": "Iu"}]
}
# Para cada asignatura, tiene 3 notas
alumno = {
    "nombre": "ana",
    "email": "ana@ana.es",
    "curso": "Python",
    "asignaturas": [{"nombre": "Programación", "nota": [7, 8, 6], "profesor": "JP"},
                    {"nombre": "Bases de datos", "nota": [8, 9, 9], "profesor": "Iu"}]
}
# Guardar la información de toda la clase que son varios alumnos
clase = [{
    "nombre": "ana",
    "email": "ana@ana.es",
    "curso": "Python",
    "asignaturas": [{"nombre": "Programación", "nota": [7, 8, 6], "profesor": "JP"},
                    {"nombre": "Bases de datos", "nota": [8, 9, 9], "profesor": "Iu"}]
},
    {
        "nombre": "iu",
        "email": "iu@iu.es",
        "curso": "Python",
        "asignaturas": [{"nombre": "Programación", "nota": [4, 2, 3], "profesor": "JP"},
                        {"nombre": "Bases de datos", "nota": [8, 9, 9], "profesor": "Iu"}]
    }
    ,
    {
        "nombre": "Eva",
        "email": "eva@eva.es",
        "curso": "Bases de datos",
        "asignaturas": [{"nombre": "sistema", "nota": [5, 7, 6], "profesor": "Pep"},
                        {"nombre": "Bases de datos", "nota": [7, 6, 9], "profesor": "Iu"}]
    }
]

for alumno in clase:
    print(alumno)  # Recorro los alumnos que, recordemos, son diccionarios

# Quiero un listado de todos los alumnos
for alumno in clase:
    print(alumno["nombre"])

nombres = [alumno['nombre'] for alumno in clase]
print(nombres)

# Para cada alumno ver las asignaturas que tiene
# Primero me recorro los alumnos
for alumno in clase:
    print(f"El alumno {alumno['nombre']} tiene las asignaturas:")
    for asignatura in alumno["asignaturas"]:
        print(asignatura["nombre"])

# Para cada alumno ver los profesores que tiene
for alumno in clase:
    print(f"El alumno {alumno['nombre']} tiene los profesores:")
    for asignatura in alumno["asignaturas"]:
        print(asignatura["profesor"])
        print(f"Que le ha puesto las siguienes notas")
        for nota in asignatura["nota"]:
            print(nota)

votaciones = [
    {
        "votante": "Juan",
        "votos": [
            {"participante": "Ana", "puntos": 5},
            {"participante": "Pedro", "puntos": 3}
        ]
    },
    {
        "votante": "Marta",
        "votos": [
            {"participante": "Ana", "puntos": 4},
            {"participante": "Luis", "puntos": 2}
        ]
    },
    {
        "votante": "Pedro",
        "votos": [
            {"participante": "Ana", "puntos": 3},
            {"participante": "Luis", "puntos": 5}
        ]
    }
]

# Nombre de los votantes
for votante in votaciones:
    print(f"El votante {votante["votante"]} ha hecho los siguientes votos")
    for voto in votante["votos"]:
        print(f"{voto["puntos"]} al participante {voto["participante"]}")


# Cuantos puntos tiene un participante
def puntosParticipante(votaciones, participante):
    puntos = 0
    for votante in votaciones:
        for voto in votante["votos"]:
            if voto["participante"] == participante:
                puntos += voto["puntos"]
    return puntos


print(puntosParticipante(votaciones, "Ana"))