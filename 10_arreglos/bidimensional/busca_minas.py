#------------------------------------------------------------------------------
# Nombre:      Buscaminas
#
# Autor:       Carlos Chesta
# Mail:        carlos.chesta@alumnos.usm.cl
#-------------------------------------------------------------------------------
 
from numpy import *
from numpy.random import *
 
# 1.-
def crear_campo(forma, n):
    fila, columna = forma
    # Se crea un arreglo uniimensional de puros 0
    buscaminas = zeros(fila * columna)
    # Los primeros n elementos tendran el valor -1
    buscaminas[:n] = -1
    # Baraja los elementos al azar
    shuffle(buscaminas)
    # Retorna el arreglo bidimensional segun la forma dada
    return buscaminas.reshape(forma)
 
# 2.-
def descubrir(campo):
    fila, columna = shape(campo)
    # Recorremos a lo largo de las filas y las columnas con estos dos for
    for i in range(fila):
        for j in range(columna):
            # Contador de minas adyacentes al elemento campo[i, j]
            cantidad_minas = 0
 
            # Estos dos for son para recorrer un elemento antrior y posterior de
            # cada eje del elemento campo[i, j]. Es decir, recorre un subcuadrado
            # con elemento central campo[i, j]
            for x in [-1, 0, 1]:
                for y in [-1, 0, 1]:
                    # Fijamos los rangos aceptables de los indices, es decir,
                    # que no tenga un rango menor a 0 o mayor a la medida del arreglo
                    if 0 <= i + x < fila and 0 <= j + y < columna:
 
                        # Contando las minas
                        if campo[i + x, j + y] == -1:
                            cantidad_minas += 1
 
            # A los elementos que no son minas se les asigna la cantidad de minas
            # adyacentes a aquel elemento
            if campo[i,j] != -1:
                campo[i,j] = cantidad_minas
 
    return campo