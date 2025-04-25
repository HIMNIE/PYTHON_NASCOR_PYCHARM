def esVocal(letra):
    vocales = "aeiouáéíóúü"
    return letra.lower() in vocales


print(esVocal("A"))
print(esVocal("i"))
print(esVocal("ó"))
print(esVocal("j"))
print(esVocal("f"))


def contarLetra(cadena, letra):
    # creo un acumulador
    contador = 0
    for c in cadena:
        if c == letra:
            contador += 1
    return contador


def contarLetra2(cadena, letra):
    cadena2 = cadena.replace(letra, "")
    return len(cadena) - len(cadena2)


print(contarLetra("hola que tal", "a"))
print(contarLetra2("hola que tal", "a"))
