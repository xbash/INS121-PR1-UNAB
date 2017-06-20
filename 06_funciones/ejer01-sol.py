
# -*- coding: utf-8 -*-

#Ejercicio 1
#Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos. 

def max(n1, n2):
    if n1 < n2:
        print(n2)
    elif n2 < n1:
        print(n1)
    else:
        print("Son iguales")
print("--- Ejercicio 1 ---")
print("El numero mayor entre 14 y 3 es: ", max(14,3))
		
#Ejercicio 2
#Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el mayor de ellos. 

def max_de_tres(n1, n2, n3):
    if n1 > n2 and n1 > n3:
        print(n1)
    elif n2 > n1 and n2 > n3:
        print(n2)
    elif n3 > n1 and n3 > n2:
        print(n3)
    else:
        print("Son iguales")
print("--- Ejercicio 2 ---")
print("El numero mayor entre 9, 8 y 3 es: ", max_de_tres(9,3,8))
		
#Ejercicio 3
#Definir una función que calcule la longitud de una lista o una cadena dada.

def largo_cadena(lista):
    cont = 0
    for i in lista:
        cont += 1
    return cont
print("--- Ejercicio 3 ---")
print("El largo de la palabra es: ",largo_cadena("Me gusta el vino, porque el vino es bueno")

#Ejercicio 4
#Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False.

def es_vocal (x):
    if x == "a" or x == "e" or x == "i" or x == "o" or x == "u":
        return True
    elif x == "A" or x == "E" or x == "I" or x == "O" or x == "U":
        return True
    else:
        return False


#Ejercicio 5

def sum (lista):
    suma = 0
    for i in lista:
        suma += i
    return suma


def multip (lista):
    multiplicacion = 1
    for i in lista:
        multiplicacion *= i
    return multiplicacion

#Ejercicio 6

#! /usr/bin/env python
# -*- coding: utf-8 -*-

def inversa (cadena):
    invertida = ""
    cont = len(cadena)
    indice = -1
    while cont >= 1:
        invertida = invertida + cadena[indice]
        indice = indice + (-1)
        cont = cont - 1
    return invertida

#Bueno reconozco que di muchas vueltas para resolver la palabra invertida. QuizÃ¡ ustedes tengan una soluciÃ³n mas simple para los que reciÃ©n se estÃ¡n iniciando. Cualquier cosa dejan un comentario y explico como funciona.

def es_palindromo (cadena):
    palabra_invertida = inversa (cadena)
    indice = 0
    cont = 0
    for i in range (len(cadena)):
        if palabra_invertida[indice] == cadena[indice]:
            indice += 1
            cont += 1
        else:
            print("No es palindromo")
            break

    if cont == len(cadena): #Si el contador = a la cantidad de letras de la cadena
        print("Es palindromo") # es porque recorriÃ³ todo el ciclo for y todas las
                                            # letras son iguales

#Como dije en el ejercicio anterior yo lo pensÃ© asÃ­, pero deben haber formas mas fÃ¡ciles de resolverlo.Yo utilizo los conocimientos que hasta la fecha tengo sobre python.
#Lo que hago en este ejercicio es utilizar la funciÃ³n del ejercicio anterior (palabra invertida) para poder compararla con la cadena que nosotros deseemos.

#Ejercicio 8

#! /usr/bin/env python
# -*- coding: utf-8 -*-

def superposicion (lista1, lista2):
    for i in lista1:
        for x in lista2:
            if i == x:
                return True
    return False

#En esta funciÃ³n lo que hacemos es comparar dos listas.

#Ejercicio 9

#! /usr/bin/env python
# -*- coding: utf-8 -*-

def generar_n_caracteres (n, caracter):
    print(n * caracter)

#Ejercicio 10

#! /usr/bin/env python
# -*- coding: utf-8 -*-

def procedimiento (lista):
    for i in lista:
        print(i * "x")