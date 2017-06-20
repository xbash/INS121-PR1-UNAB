#-------------------------------------------------------------------------------
# Name:        Ordenamiento
#
# Author:      Carlos Chesta
#-------------------------------------------------------------------------------
 
def menor_a_mayor(palabra):
    return len(palabra)
 
animales = ['conejo', 'ornitorrinco', 'pez', 'hipopotamo', 'tigre']
animales.sort(key=menor_a_mayor)
print animales
print               # Salto de linea
 
# -------------------------------------- #
 
def mayor_a_menor(palabra):
    return -len(palabra)
 
animales = ['conejo', 'ornitorrinco', 'pez', 'hipopotamo', 'tigre']
animales.sort(key=mayor_a_menor)
print animales
print               # Salto de linea
 
# -------------------------------------- #
 
def suma_elementos(lista):
    return sum(lista)
 
a = [[6, 1, 5, 9],
     [0, 0, 4, 0, 1],
     [3, 2, 12, 1],
     [1000],
     [7, 6, 1, 0],
    ]
 
a.sort(key=suma_elementos)
print a
print               # Salto de linea
 
# -------------------------------------- #
 
def pprint(lista):
    print "[" + str(lista[0]) + ","
    for i in range(1, len(lista)):
        if i != len(lista) - 1:
            print str(lista[i]) + ","
        else:
            print str(lista[i]) + "]"
 
# -------------------------------------- #
 
def orden_alfabetico(lista):
    return lista[1]
 
personas = [
    ('John',   'Doe',         (1992, 12, 28)),
    ('Perico', 'Los Palotes', (1992, 10, 8)),
    ('Yayita', 'Vinagre',     (1991,  4, 17)),
    ('Fulano', 'De Tal',      (1992, 10, 4)),
]
 
personas.sort(key=orden_alfabetico)
pprint(personas)
print               # Salto de linea
 
# -------------------------------------- #
 
def orden_fecha_antigua_a_reciente(lista):
    return lista[2]
 
personas.sort(key=orden_fecha_antigua_a_reciente)
 
pprint(personas)
print
 
# -------------------------------------- #
 
def orden_fecha_reciente_antigua(lista):
    fecha = lista[2]
    anio, mes, dia = fecha
    fecha_inv = (-anio, -mes, -dia)
    return fecha_inv
 
personas.sort(key=orden_fecha_reciente_antigua)
 
pprint(personas)
print
 
# -------------------------------------- #
 
def orden_meses(mes):
    dias_meses = {
            "febrero" : 28,
            "abril": 30,
            "agosto": 31,
            "noviembre": 31
        }
    return dias_meses[mes]
 
meses = ['agosto', 'noviembre', 'abril', 'febrero']
 
meses.sort(key=orden_meses)
print meses
print                   # Salto de linea
 
# -------------------------------------- #
 
def impar_izq_par_der(num):
    if num % 2 != 0:
        return -num
    else:
        return num
 
from random import randrange
valores = []
for i in range(12):
    valores.append(randrange(256))
 
print "Normal:", valores
valores.sort(key = impar_izq_par_der)
print "Ordenado:", valores
print                   # Salto de linea
 
# -------------------------------------- #
 
def orden_palindromos(numero):
    if str(numero) == str(numero)[::-1]:
        return numero
    else:
        return -numero
 
a = [12321, 584, 713317, 8990, 44444, 28902]
a.sort(key = orden_palindromos)
print a