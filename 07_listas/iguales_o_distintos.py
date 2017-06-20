#-------------------------------------------------------------------------------
# Name:        Iguales o distintos
#
# Author:      Carlos Chesta
#-------------------------------------------------------------------------------
 
def todos_iguales(lista):
    primero = lista[0]
    retorno = True
    for i in lista:
        if i != primero:
            retorno = False
    return retorno
 
def todos_distintos(lista):
    aux = []
    retorno = True
    for i in lista:
        if i in aux:
            retorno = False
        else:
            aux.append(i)
    return retorno