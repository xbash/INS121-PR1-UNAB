#Ejercicio 1

#No aclare bien el ejercicio, por lo tanto puede ser que lo resuelvan de esta manera:

#! /usr/bin/env python
# -*- coding: utf-8 -*-

def max_in_list(lista):
    return max (lista) #La funciÃ³n max() ya viene incorporada en python

#Pero la idea es resolver la funciÃ³n por nosotros mismos para saber como es que funciona. AquÃ­ la soluciÃ³n:

#! /usr/bin/env python
# -*- coding: utf-8 -*-
def max_in_list(lista):
    inicio = 0
    for i in lista:
        if i > inicio:
            inicio = i
    return inicio

#Ejercicio 2

#! /usr/bin/env python
# -*- coding: utf-8 -*-
def mas_larga(lista):
    mas_larga = ""
    for i in lista:
        if len(i) > len(mas_larga):
            mas_larga = i
    return mas_larga

#Ejercicio 3

 #! / Usr / bin / env python
# - * - CodificaciÃ³n: utf-8 - *
def filtrar_palabras(lista, n):
    for i in lista:
        if len(i) > n:
            print (i)

#Ejercicio 4

#! / Usr / bin / env python
# - * - CodificaciÃ³n: utf-8 - *

def c_mayusculas (cadena):
    cont = 0
    for i in cadena:
        if i != i.lower(): #Recordar que lower() convierte una cadena en minÃºsculas
            cont += 1
    print ("La cadena tiene", cont, "mayuscula/s")

#Ejercicio 5

#! /usr/bin/env python
# -*- coding: utf-8 -*-
def aDecimal(numeroBin):
    numeroBin = str(numeroBin)
    decimal = 0
    exp = len (numeroBin) -1
    for i in numeroBin:
        decimal += (int(i) * 2**(exp))
        exp = exp - 1
    return decimal

#Ejercicio 6

#! /usr/bin/env python
# -*- coding: utf-8 -*-
def main():
    a_curso = input ("Ingresa el anio en curso: ")
    for i  in range (3):
        nombre = raw_input ("Nombre de la persona: ")
        nacimiento = input ("Anio de nacimiento: ")
        print(nombre, "cumple", (a_curso - nacimiento), "anios en el", a_curso)

#Ejercicio 7

#! /usr/bin/env python
# -*- coding: utf-8 -*-
def mayora20 (tup):
    cont = 0
    for i in tup:
        if i > 20:
            cont += 1
    print ("Hay", cont, "numeros mayores a 20")

#Ejercicio 8

#! /usr/bin/env python
# -*- coding: utf-8 -*-
def main():
    x = input ("Cuantos nombres quieres ingresar?: ")
    lista = []
    for i in range(x):
        a = raw_input ("Ingresa el nombre: ")
        lista.append (a)

    print("")
    comienzo = raw_input ("Con que letra empieza el nombre?: ")
    cont = 0
    for i in lista:
        if i[0] == comienzo.lower() or i[0] == comienzo.upper() :
            cont += 1
    return cont

#Como pueden ver, el ejercicio lo hago interactuando con el usuario. TambiÃ©n decir que uso la funciÃ³n append() que sirve para agregar elementos a una lista, uso la funciÃ³n lower() para convertir cadenas en minÃºsculas y uso la funciÃ³n upper() capara convertir caracteres o cadenas en mayÃºsculas.

#Ejercicio 9

#! /usr/bin/env python
# -*- coding: utf-8 -*-
def contar_vocales(cadena):
    cadena = cadena.lower()
    vocales = "aeiou"

    for x in vocales:
        contador = 0
        for i in cadena:
            if i == x:
                contador += 1
        print("Hay %d %s." % (contador, x))

#Ejercicio 10

#! /usr/bin/env python
# -*- coding: utf-8 -*-
def es_bisiesto():
    print("Comprueba aÃ±os bisiestos")
    a = input ("Escriba un aÃ±os y le dire si es bisiesto: ")
    if a % 4 == 0 and (not(a % 100 == 0)):
        print("El aÃ±o", a, "es un aÃ±o bisiesto porque es multiplo de 4")
    elif a % 400 == 0:
        print("El aÃ±o", a, "es un aÃ±o bisiesto porque es multiplo de 400")
    else:
        print("El aÃ±o", a, "no es bisiesto")