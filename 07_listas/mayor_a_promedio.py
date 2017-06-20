#-------------------------------------------------------------------------------
# Nombre:      Mayores que el promedio
#
# Autor:       Carlos Chesta
# Mail:        carlos.chesta@alumnos.usm.cl
#-------------------------------------------------------------------------------
 
n = int(raw_input("Cuantos datos ingresara? "))
 
lista = []
 
for i in range(1, n + 1):
    dato = float(raw_input("Dato " + str(i) + ": "))
    lista.append(dato)
 
promedio = sum(lista) / len(lista)
contador = 0
 
for i in lista:
    if i > promedio:
        contador += 1
 
print contador, "datos son mayores que el promedio"