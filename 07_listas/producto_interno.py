#-------------------------------------------------------------------------------
# Name:        Producto interno
#
# Author:      Carlos Chesta
#-------------------------------------------------------------------------------
 
def producto_interno(a,b):
    suma = 0
    for i in range(len(a)):
        suma += a[i]*b[i]
    return suma
 
a = [7, 1, 4, 9, 8]
b = range(5)
 
def son_ortogonales(a,b):
    if producto_interno(a,b) == 0:
        return True
    else:
        return False