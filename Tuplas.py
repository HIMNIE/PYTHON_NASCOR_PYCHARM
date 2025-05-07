# las tuplas son como las listas, pero inmutables
# No se pueden modificar
# Si las listas se definen con corchetes, las tuplas se definen con paréntesis

mitupla = (1, 2, 3, 4)
otratupla = ("Ana", "Pep", "Eva")

for numero in mitupla:
    print(numero)

print(mitupla[1])
print(mitupla[-1])
print(mitupla[1:3])


def extremos(lista):
    ordenada = sorted(lista)  # [1,2,3,4,5,8]
    return (ordenada[0], ordenada[-1])


print(extremos([2, 4, 1, 8, 5, 3]))
# desempaquetar tupla
menor, mayor = extremos([2, 4, 1, 8, 5, 3])
print((menor))
print((mayor))

i, j = extremos([2, 4, 1, 8, 5, 3])
print((i))
print((j))

# desempaqueto 4 valores
a, b, c, d = mitupla  # a=1,b=2,c=3,d=4
print(c)

tupla = (2, 4, 8)

a, b, c = tupla  # a=2, b=4, c=8


def foo():
    return ("Sí", "No", "Quizás")


def tablairpf():
    return (5, 10, 12, 18)


s, n, q = foo()  # s="Sí", n="No", q="Quizás"

print(q)

bajo, medio, alto, superior = tablairpf()

# desempaquetar múltiples valores
b, *m, s = tablairpf()

print(b)  # 5
print(m)  # [10,12]
print(s)  # 18

b, m, *s = tablairpf()

print(b)  # 5
print(m)  # 10
print(s)  # [12, 18]

*_, m, s = tablairpf()

print(b)  # [5, 10]
print(m)  # 12
print(s)  # 18


def suma(*numeros):
    suma = 0
    for numero in numeros:
        suma += numero
    return suma


print(suma(1, 2))
print(suma(1, 2, 4, 5, 7))
print(suma(1, 2, 4, 5, 7, 8, 9, 10))

s, n, _ = foo()  # s="Sí", n="No", _ se ignora