# listas: colección de variables

nota = 7  # Una variable en la que guardo un valor
notas = [5, 8, 6, 4]  # Una lista es una colección de variables

vacia = []
foo = ["hola"]
varios = ["a", "b", "c"]

mixta = [1, 4, "cadena", False, 3.56, "otra cadena", 28]  # Los elementos pueden ser de cualquier tipo

print(mixta[2])  # cadena
print(mixta[-1])  # 28 (el último)

for elemento in mixta:
    print(elemento)

print(mixta[2:4])
print(mixta[2:5])
print(mixta[2:3])

clase = ["Ana", "Pep", "Eva", "Iu"]

# la variable alumno va a ir tomando los valores de la lista 'clase'
# es decir, primero Ana, después Pep, luego Eva y por último Iu
for alumno in clase:
    print(alumno)

# Mutables: que se pueden cambiar

clase[1] = "Juan"
print(clase)

# Métodos de las listas

# append añade un elemento al final de la lista
clase.append("Rosa")
print(clase)

# extend nos añade una lista al final de otra lista
otraclase = ["John", "Mary"]
clase.extend(otraclase)

print(clase)

# también podemos hacerlo simplemente sumando
otraclasemas = ["Luis", "María"]
clase += otraclasemas
print(clase)

# el append también se puede hacer sumando pero ¡ojo! entre corchetes
clase += ["Fernando"]
print(clase)

# Podemos insertar un elemento en cualquier posición con insert

clase.insert(2, "Florencia")

# ¡Ojo! No es lo mismo insertar que cambiar. Añado Florencia y el resto se desplaza
print(clase)

# Eliminamos la primera ocurrencia de Florencia
clase.remove("Florencia")
print(clase)

# Extraer elementos

# Estoy extrayendo el último elemento y lo estoy guardando en último
ultimo = clase.pop()
print(ultimo)
print(clase)

# Puedo hacer pop sin guardar, simplemente elimino el último elemento
clase.pop()
print(clase)

# pop puede tener como parámetro una posición

al = clase.pop(3)  # extraigo el elemento 3 (Iu)
print(al)
print(clase)

for i in range(len(clase)):
    clase.pop()

print(clase)