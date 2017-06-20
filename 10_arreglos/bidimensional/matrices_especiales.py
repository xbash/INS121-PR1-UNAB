#-------------------------------------------------------------------------------
# Nombre:      Matrices especiales
#
# Autor:       Carlos Chesta
# Mail:        carlos.chesta@alumnos.usm.cl
#-------------------------------------------------------------------------------
 
from numpy import *
 
# 1.-
def es_simetrica(a):
    fila, columna = shape(a)
 
    # En el caso de que la matriz no sea cuadrada (por def. la matriz simetrica
    # tiene que ser cuadrada)
    if fila != columna:
        return False
 
    for i in range(fila):
        for j in range(columna):
            if a[i, j] != a[j, i]:
                return False
 
    return True
 
# 2.-
# Obs: asumire que las matrices son cuadradas para ahorrar un par de lineas
def es_antisimetrica(a):
    fila, columna = shape(a)
 
    for i in range(fila):
        for j in range(columna):
            if a[i, j] != -a[j, i]:
                return False
 
    return True
 
# 3.-
def es_diagonal(a):
    fila, columna = shape(a)
    for i in range(fila):
        for j in range(columna):
            if i != j and a[i][j] != 0:
                return False
    return True
 
# 4.-
def es_triangular_superior(a):
    fila, columna = shape(a)
    for i in range(fila):
        for j in range(columna):
            if i > j and a[i][j] != 0:
                return False
    return True
 
# 5.-
def es_triangular_inferior(a):
    return es_triangular_superior(a.transpose())
 
# 6.-
def es_idempotente(a):
    return all(dot(a, a) == a)
 
# 7.-
def conmutan(a, b):
    fila_a, columna_a = shape(a)
    fila_b, columna_b = shape(b)
 
    # En el caso de que no se pueda hacer el producto matricial en las matrices
    # por tener tamanios incompatibles.
    # Obs: la matriz A (n x m) se puede hacer producto matricial con la matriz B (r x s)
    # si y solo si: m == r, y el resultado sera una matriz de n x s
    if columna_a == fila_b:
        return all(dot(a, b) == dot(b, a))
    else:
        return False