#-------------------------------------------------------------------------------
# Name:        Desviacion estandar
#
# Author:      Carlos Chesta
#-------------------------------------------------------------------------------
 
def promedio(valores):
    suma = 0
    for i in valores:
        suma += i
    return suma/float(len(valores))
 
def desviacion_estandar(valores):
    prom = promedio(valores)
    numerador = 0
    for i in valores:
        numerador += (i - prom)**2
    return (numerador/(len(valores)-1))**0.5

