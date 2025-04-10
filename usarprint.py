print("hola")

pi = 3.1415926535
print(f"Pi con 2 decimales: {pi:.2f}")           # → Pi con 2 decimales: 3.14
print("Pi con 4 decimales: {:.4f}".format(pi))   # → Pi con 4 decimales: 3.1416

edad=20
print(edad)
print("hola",edad)

print("tu edad es ",edad)
#la f, lo que quiere decir es 'cadena formateada'
#nos permite poner valores entre llaves
print(f" tu edad es {edad} enhorabuena ")
print(f" Dentro de 10 años tendras {edad+10}")

#aqui se convierte
print(f" Dentro de 10 años tendras {float(edad)+10}")


print('se llama "wifi" y es un medio de conexion')

#la barra (slash) se llama caracter de escape
#el caracter siguiente es especial
print("se llama\"Wifi\" y es un medio de conexion ")

# \n es salto de linea
print("se llama \n y es un medio de conexion")

#\t es un tabulador
print("se llama \t y es un medio de conexion")

#\\ es un barra
print("se llama \\ y es un medio de conexion")
print("para imprimir barra \\")

#opciones del print
print("hola", edad,"pepe",14)

#especifico cual quiero que sea el separador
print("hola", edad,"pepe",14, sep="  --  ")

#especificar el final de linea
print("hola")
print("juan")
print("hola", end=",")
print("hola")

with open("salida.txt", "w") as f:
    print("Esto va al archivo", file=f)


a=.1
b=.2
print(a+b)
print(f"a+b con 2 decimales: {(a+b):.2f}")

