def buscar(lista,elemento):
    posiciones=[]
    try:
       pos=lista.index(elemento)
       while True:
           posiciones.append(pos)
           pos = lista.index(elemento,pos + 1)
    except:
        return posiciones

print(buscar(numeros,6))