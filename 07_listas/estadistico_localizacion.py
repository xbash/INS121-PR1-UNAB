#-------------------------------------------------------------------------------
# Nombre:      Estadisticos de localizacion
#
# Autor:       Carlos Chesta
# Mail:        carlos.chesta@alumnos.usm.cl
#-------------------------------------------------------------------------------
 
def media_aritmetica(datos):
    suma = 0.0
    for numero in datos:
        suma += numero
    return suma / len(datos)
 
def media_armonica(datos):
    suma_denominador = 0.0
    for numero in datos:
        suma_denominador += 1.0/numero
    return len(datos) / suma_denominador
 
def mediana(datos):
    ordenada = sorted(datos)
    if len(ordenada) % 2 != 0:
        dato_medio = ordenada[len(ordenada)/2]
    else:
        dato_medio = (ordenada[len(ordenada)/2] + ordenada[len(ordenada)/2 - 1]) / 2
    return dato_medio
 
def modas(datos):
    lista = []
    mayor = -9999
    for numero in datos:
        if datos.count(numero) >= mayor:
            mayor = datos.count(numero)
    for numero in datos:
        if datos.count(numero) == mayor and numero not in lista:
            lista.append(numero)
 
    return sorted(lista)
 
 
datos = []
n = int(raw_input("Cuantos datos ingresara? "))
for i in range(n):
    dato = float(raw_input("Ingrese dato: "))
    datos.append(dato)
 
if 0 not in datos:
    print "Media aritmetica", media_aritmetica(datos)
    print "Media armonica", media_armonica(datos)
    print "Mediana", mediana(datos)
    print "Moda", modas(datos)
 
else:
    print "Media aritmetica", media_aritmetica(datos)
    print "Mediana", mediana(datos)
    print "Moda", modas(datos)