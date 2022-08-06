import math
from numbers import Number

lista = None
tamano = None
buscado = None
test = None
indice = None
resultado = None
salto = None


# Busqueda de salto
def busquedaSalto(lista, tamano, buscado):
    global test, indice, resultado, salto
    indice = 0
    salto = math.floor(math.sqrt(tamano))
    while lista[int(((min([salto, tamano]) - 1) + 1) - 1)] < buscado:
        indice = salto
        salto = (salto if isinstance(salto, Number) else 0) + math.floor(
            math.sqrt(tamano))
        if indice >= tamano:
            return -1
    while lista[int((indice + 1) - 1)] < buscado:
        indice = (indice if isinstance(indice, Number) else 0) + 1
        if indice == min([salto, tamano]):
            return -1
    if lista[int((indice + 1) - 1)] == buscado:
        return indice
    return -1


test = [0, 1, 2, 3, 5, 10, 23, 44, 78, 100]
resultado = busquedaSalto(test, len(test), 10)
# Empieza desde 0
if resultado >= 0:
    print('El numero se encuentra en la posición: ' + str(resultado))
else:
    print('No se encontró el numero.')
