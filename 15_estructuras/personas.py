#-------------------------------------------------------------------------------
# Name:        Personas
#
# Author:      Carlos Chesta
#-------------------------------------------------------------------------------
 
from personas import *
 
meses = {
    1: 'enero', 2: 'febrero', 3: 'marzo', 4: 'abril',
    5: 'mayo', 6: 'junio', 7: 'julio', 8: 'agosto',
    9: 'septiembre', 10: 'octubre', 11: 'noviembre',
    12: 'diciembre'}
 
def imprimir_nombres(personas):
    for nombre in personas:
        print(nombre[0])
 
def imprimir_fechas(personas):
    for i in personas:
        _,_,fecha = i
        dia, mes, anio = fecha
        print(str(dia) + " de "+ meses[mes] + " de "+ str(anio))
 
def cuantas_personas(personas):
    return len(personas)
 
def mi_cumple(personas):
    lista = []
    cumple = (21,1,1993)
    for i in personas:
        nombre, apellido, fecha = i
        if fecha == cumple:
            lista.append(nombre + " " + apellido)
    return lista
 
def nombre_mas_comun(personas):
    lista = []
    dicc = {}
    for i in personas:
        nombre, apellido, fecha = i
        lista.append(nombre)
    for i in lista:
        if i not in dicc:
            dicc[i] = lista.count(i)
 
    maximo = -9999
    for nombre, repeticion in dicc.items():
        if repeticion > maximo:
            maximo = repeticion
            nombre_repetido = nombre
    return nombre_repetido