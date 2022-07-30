import math

izq = None
der = None
buscado = None
lista = None
test = None
mid2 = None
resultado = None
mid1 = None

# Busqueda Ternaria
def busquedaTernaria(izq, der, buscado, lista):
  global test, mid2, resultado, mid1
  if der >= izq:
    mid1 = izq + math.floor((der - izq) / 3)
    mid2 = der - math.floor((der - izq) / 3)
    print(''.join([str(x) for x in ['Rango: ', mid1, ', ', mid2]]))
    if lista[int((mid1 + 1) - 1)] == buscado:
      return mid1
    if lista[int((mid2 + 1) - 1)] == buscado:
      return mid2
    if buscado < lista[int((mid1 + 1) - 1)]:
      resultado = busquedaTernaria(izq, mid1 - 1, buscado, lista)
    elif buscado > lista[int((mid2 + 1) - 1)]:
      resultado = busquedaTernaria(mid2 + 1, der, buscado, lista)
    else:
      resultado = busquedaTernaria(mid1 + 1, mid2 - 1, buscado, lista)
  else:
    resultado = -1
  return resultado

# Valores para la busqueda ternaria
def busquedaTernariaValores(lista, buscado):
  global izq, der, test, mid2, resultado, mid1
  resultado = busquedaTernaria(0, len(lista) - 1, buscado, lista)
  return resultado

test = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultado = busquedaTernariaValores(test, 6)
if resultado != -1:
  print('El numero 6 esta en la posición: ' + str(resultado))
else:
  print('No se encontró.')
