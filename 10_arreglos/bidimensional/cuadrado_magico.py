#-------------------------------------------------------------------------------
# Nombre:      Cuadrado magico
#
# Autor:       Carlos Chesta
# Mail:        carlos.chesta@alumnos.usm.cl
#-------------------------------------------------------------------------------
 
from numpy import *
 
# 1.-
def consecutivos(arreglo):
    n = len(arreglo)
 
    for i in range(1, n**2 + 1):
        if i not in arreglo:
            return False
 
    return True
 
# 2.-
def es_magico(arreglo):
    n = len(arreglo)
 
    for i in range(n):
        fila_i = arreglo[i, ::]
        columna_i = arreglo[::, i]
 
        # Negamos la condicion necesaria para que sea cuadrado magico
        if sum(fila_i) != sum(columna_i) or sum(fila_i) != sum(diag(arreglo)):
            return False
 
    return True