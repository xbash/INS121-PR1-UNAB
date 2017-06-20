#-------------------------------------------------------------------------------
# Name:        Mapear y filtrar
#
# Author:      Carlos Chesta
#-------------------------------------------------------------------------------
 
def cuadrado(x):
    return x**2
 
def mapear(f,valores):
    lista=[]
    for i in valores:
        lista.append(f(i))
    return lista
 
def es_larga(palabra):
    return len(palabra)>4
 
def filtrar(f,valores):
    lista= []
    for i in valores:
        if f(i):
            lista.append(i)
    return lista