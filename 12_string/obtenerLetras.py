#-------------------------------------------------------------------------------
# Name:        obtenerLetras
# Purpose:
#
# Author:      CMartinez
#
# Created:     18-10-2016
# Copyright:   (c) CMartinez 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------


#Dada una palabra retornar las que estan en posicion par
def obtenerLetras(palabra, par=True):
    aux = ""
    for i in range(len(palabra)):
        if (par and i%2 == 1) or (not par and i%2 == 0):
            aux = aux + palabra[i]
    return aux

print(obtenerLetras("Hola Mundo"))
print(obtenerLetras("Hola Mundo", True))
print(obtenerLetras("Hola Mundo", False))