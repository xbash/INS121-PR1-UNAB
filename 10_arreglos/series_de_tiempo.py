#-------------------------------------------------------------------------------
# Nombre:      Series de tipo
#
# Autor:       Carlos Chesta
# Mail:        carlos.chesta@alumnos.usm.cl
#-------------------------------------------------------------------------------
 
from numpy import *
 
# 1.-
def medias_moviles(serie, p):
    lista = []
 
    # el arreglo tendra un largo de len(serie) - p + 1 elementos
    for i in range(len(serie) - p + 1):
        p_valores = serie[i : p+i]
        media = sum(p_valores) / p
        lista.append(media)
 
    return array(lista)
 
# 2.-
def diferencias_finitas(serie):
    lista = []
 
    # el arreglo tendra un largo de len(serie) - 1 elementos
    for i in range(len(serie) - 1):
        diferencias = serie[i+1] - serie[i]
        lista.append(diferencias)
 
    return array(lista)