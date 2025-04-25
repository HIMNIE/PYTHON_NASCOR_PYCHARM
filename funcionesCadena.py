# podemos definir nuestras propias funciones
# pero python tiene muchas funciones predefinidas

cadena = "Hola que tal"

print(len(cadena))

# Funciones de cadena: nos permiten manipular cadenas de texto

# Acceder a un carácter específico de la cadena o a un rango de caracteres

print(cadena[3])  # imprime la letra 'a'

# Con los dos puntos obtenemos una subcadena de la cadena desde el primer carácter hasta el último NO INCLUÍDO
print(cadena[3:7])  # imprime 'a qu' va del 3 al 6 (incluído)

for i in range(0, len(cadena) + 1):
    print(cadena[0:i])

mayusculas = cadena.upper()
print(mayusculas)
minusculas = cadena.lower()
print(minusculas)
print(cadena.title())

# Si una cadena está dentro de otra
print("que" in cadena)
print("pepe" in cadena)

# Nos busca la posición de una cadena dentro de otra
# Si no está nos devuelve -1
posicion = cadena.find("que")
print(posicion)
posicion = cadena.find("pepe")
print(posicion)

# Podemos reemplazar una cadena por otra

print(cadena.replace("que", "ke"))
print(cadena.replace("a", "@"))

print(cadena.replace("a", ""))
# Podemos indicar las veces que queremos reemplazar
cadena = "patatas para ana"
print(cadena.replace("a", "@", 3))

cadena = "   hola que tal   "
# con strip quito espacios del principio y del final

print(cadena.strip().upper())  # encadenamiento y funciona porque las funciones devuelven un valor

sinespacios = cadena.strip()
mayus = sinespacios.upper()
print(mayus)

# en una cadena reemplazar las A por @ independentemiente de mayúsculas o minúsculas

cad = "CADA PATATA tiene carbohidratos"

print(cad.lower().replace("a", "@"))

some_string = 'Hello World'
print('Testing a String')
print('-' * 20)
print('some_string', some_string)
print("some_string.startswith('H')",
      some_string.startswith('H'))
print("some_string.startswith('h')",
      some_string.startswith('h'))
print("some_string.endswith('d')", some_string.endswith('d'))
print('some_string.istitle()', some_string.istitle())
print('some_string.isupper()', some_string.isupper())
print('some_string.islower()', some_string.islower())
print('some_string.isalpha()', some_string.isalpha())
print('String conversions')
print('-' * 20)
print('some_string.upper()', some_string.upper())
print('some_string.lower()', some_string.lower())
print('some_string.title()', some_string.title())
print('some_string.swapcase()', some_string.swapcase())
print('String leading, trailing spaces', " xyz ".strip())
