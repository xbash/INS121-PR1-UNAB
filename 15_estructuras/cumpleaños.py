# -*- coding: cp1252 -*-
#-------------------------------------------------------------------------------
# Name:        Cumpleaños
#
# Author:      Carlos Chesta
#-------------------------------------------------------------------------------
 
n = {
    'Pepito': (1990, 10, 20),
    'Yayita': (1992, 3, 3),
    'Panchito': (1989, 10, 20),
    'Perica': (1989, 12, 8),
    'Fulanita': (1991, 2, 14),
}
 
def mismo_dia(fecha1,fecha2):
    _,_,dia1 = fecha1
    _,_,dia2 = fecha2
    if dia1 == dia2:
        return True
    else:
        return False
 
def mas_viejo(n):
    viejo = (999999,9999999,999999)
    viejo_nombre = ''
    for nombre,fecha in n.items():
        if fecha < viejo:
            viejo = fecha
            viejo_nombre = nombre
    return viejo_nombre
 
def primer_cumple(n):
    primero = (9999,9999)
    for nombre, fecha in n.items():
        _,mes,dia = fecha
        if (mes,dia) < primero:
            primero = (mes,dia)
            nombre_primero = nombre
    return nombre_primero