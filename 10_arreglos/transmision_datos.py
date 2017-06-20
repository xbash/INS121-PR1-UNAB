#-------------------------------------------------------------------------------
# Nombre:      Transmision de datos
#
# Autor:       Carlos Chesta
# Mail:        carlos.chesta@alumnos.usm.cl
#-------------------------------------------------------------------------------
 
from numpy import *
 
# No hay diferencia entre trabajar con arreglos y listas EN ESTE EJERCICIO
 
def numero_decimal(datos):
    decimal = 0
    exponente = len(datos) - 1
 
    for binario in datos:
        decimal += binario * 2**exponente
        exponente -= 1
 
    return decimal
 
def bloque_valido(datos):
    return len(datos) % 4 == 0
 
# Importamos el la funcion 'ceil' que retorna el entero mayor mas cercano de un numero flotante.
# Ej: ceil(4.3) -> 5.0; ceil(2.7) -> 3-0
from math import ceil
def decodificar_bloques(datos):
    cantidad_bloques = int(ceil(len(datos) / 4.0))
    # Creamos una lista para agregar los numeros decimales. Esto porque en los
    # arreglos no se pueden agregar elementos una vez creados
    lista_bloques_decodificados = []
 
    for i in range(cantidad_bloques):
        # Rebanamos 4 en 4 los datos
        bloque = datos[4*i : 4*(i + 1)]
 
        if bloque_valido(bloque):
            decimal = numero_decimal(bloque)
            lista_bloques_decodificados.append(decimal)
 
        else:
            lista_bloques_decodificados.append(-1)
 
    # Retornamos la conversion de lista a arreglo
    return array(lista_bloques_decodificados)
