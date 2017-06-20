#-------------------------------------------------------------------------------
# Nombre:      Rotar matrices
#
# Autor:       Carlos Chesta
# Mail:        carlos.chesta@alumnos.usm.cl
#-------------------------------------------------------------------------------
 
from numpy import *
 
# 1.-
# Ciclico
def rotar90(a):
    columnas = a.shape[1]
    lista = []
 
    for i in range(1, columnas + 1):
        lista.append(a[:, -i])
 
    return array(lista)
 
# Operaciones de arreglos
def rotar90(a):
    return a.transpose()[::-1]
 
# 2a.-
# Ciclico
def rotar180(a):
    arreglo_rotado = a      # Defino inicialmente esta variable. Obviamente
                            # no esta rotado cuando la defino
 
    for ciclo in range(0, 180, 90): # Va a iterar dos veces
        columnas = arreglo_rotado.shape[1]
        lista = []
 
        for i in range(1, columnas + 1):
            lista.append(arreglo_rotado[:, -i])
 
        arreglo_rotado = array(lista)
 
    return arreglo_rotado
 
# Operacion de arreglos
def rotar180(a):
    return a.transpose()[::-1].transpose()[::-1]
 
# Astuta
def rotar180(a):
    return rotar90(rotar90(a))
 
# 2b.-
# Ciclico
 
def rotar270(a):
    arreglo_rotado = a      # Defino inicialmente esta variable. Obviamente
                            # no esta rotado cuando la defino
 
    for ciclo in range(0, 270, 90):     # Va a iterar 3 veces
        columnas = arreglo_rotado.shape[1]
        lista = []
 
        for i in range(1, columnas + 1):
            lista.append(arreglo_rotado[:, -i])
 
        arreglo_rotado = array(lista)
 
    return arreglo_rotado
 
# Operacion de arreglos
def rotar270(a):
    return a.transpose()[::-1].transpose()[::-1].transpose()[::-1]
 
# Astuta
def rotar270(a):
    return rotar180(rotar90(a))