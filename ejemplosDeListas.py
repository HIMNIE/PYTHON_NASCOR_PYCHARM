# Lista de notas de los estudiantes
notas = [10, 6, 3, 5, 8, 9, 2, 7]

# -------------------------------
# CALCULAR LA MEDIA (PROMEDIO)
# -------------------------------

# Inicializamos una variable para acumular la suma de todas las notas
suma = 0

# Recorremos cada nota en la lista
for nota in notas:
    suma += nota  # Vamos sumando cada nota a la variable 'suma'

# Calculamos la media dividiendo la suma entre el número de notas
print(suma / len(notas))  # Mostramos el resultado de la media

# -------------------------------
# CONTAR CUÁNTOS HAN APROBADO
# -------------------------------

# Inicializamos un contador de aprobados
aprobados = 0

# Recorremos cada nota
for nota in notas:
    if nota >= 5:  # Si la nota es mayor o igual a 5, es un aprobado
        aprobados += 1  # Sumamos 1 al contador de aprobados

print(aprobados)  # Mostramos cuántos estudiantes han aprobado

# -------------------------------
# CREAR UNA LISTA DE SUSPENDIDOS
# -------------------------------

# Creamos una lista vacía para guardar las notas suspendidas (< 5)
suspendidos = []

# Recorremos cada nota
for nota in notas:
    if nota < 5:  # Si la nota es menor que 5, es un suspenso
        suspendidos.append(nota)  # Añadimos esa nota a la lista de suspendidos

print(suspendidos)  # Mostramos la lista de notas suspendidas
