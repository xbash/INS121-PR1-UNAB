Ejercicio 1

#! /usr/bin/env python
# -*- coding: utf-8 -*-

def max (n1, n2):
    if n1 < n2:
        print n2
    elif n2 < n1:
        print n1
    else:
        print "Son iguales"

Aclaro que uso el print para llamar a la función de la manera max(8, 5).
También se puede usar return.

Ejercicio 2

#! /usr/bin/env python
# -*- coding: utf-8 -*-
def max_de_tres (n1, n2, n3):
    if n1 > n2 and n1 > n3:
        print n1
    elif n2 > n1 and n2 > n3:
        print n2
    elif n3 > n1 and n3 > n2:
        print n3
    else:
        print "Son iguales"

Otra vez uso el print en ves del return. Dependiendo para que lo necesitemos se usa uno u el otro. En este caso solo quiero mostrar por pantalla cual es el mayor de los 3 números. 

Ejercicio 3

#! /usr/bin/env python
# -*- coding: utf-8 -*-

def largo_cadena (lista):
    cont = 0
    for i in lista:
        cont += 1
    return cont

En este ejercicio utilizo return en ves de print. Para ver el resultado tendríamos que llamar la función de la manera: print largo_cadena ([1,2,3,4]) o
print largo_cadena ("hola")

Ejercicio 4

#! /usr/bin/env python
# -*- coding: utf-8 -*-

def es_vocal (x):
    if x == "a" or x == "e" or x == "i" or x == "o" or x == "u":
        return True
    elif x == "A" or x == "E" or x == "I" or x == "O" or x == "U":
        return True
    else:
        return False

Ejercicio 5

#! /usr/bin/env python
# -*- coding: utf-8 -*-

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

Ejercicio 6

#! /usr/bin/env python
# -*- coding: utf-8 -*-

def inversa (cadena):
    invertida = ""
    cont = len(cadena)
    indice = -1
    while cont >= 1:
        invertida += cadena[indice]
        indice = indice + (-1)
        cont -= 1
    return invertida

Bueno reconozco que di muchas vueltas para resolver la palabra invertida. Quizá ustedes tengan una solución mas simple para los que recién se están iniciando. Cualquier cosa dejan un comentario y explico como funciona. 

Ejercicio 7

#! /usr/bin/env python
# -*- coding: utf-8 -*-

def inversa (cadena):
    invertida = ""
    cont = len(cadena)
    indice = -1
    while cont >= 1:
        invertida += cadena[indice]
        indice = indice + (-1)
        cont -= 1
    return invertida

 def es_palindromo (cadena):
    palabra_invertida = inversa (cadena)
    indice = 0
    cont = 0
    for i in range (len(cadena)):
        if palabra_invertida[indice] == cadena[indice]:
            indice += 1
            cont += 1
        else:
            print "No es palindromo"
            break

    if cont == len(cadena): #Si el contador = a la cantidad de letras de la cadena
        print "Es palindromo" # es porque recorrió todo el ciclo for y todas las
                                            # letras son iguales

Como dije en el ejercicio anterior yo lo pensé así, pero deben haber formas mas fáciles de resolverlo.Yo utilizo los conocimientos que hasta la fecha tengo sobre python.
Lo que hago en este ejercicio es utilizar la función del ejercicio anterior (palabra invertida) para poder compararla con la cadena que nosotros deseemos. 

Ejercicio 8

#! /usr/bin/env python
# -*- coding: utf-8 -*-

def superposicion (lista1, lista2):
    for i in lista1:
        for x in lista2:
            if i == x:
                return True
    return False

En esta función lo que hacemos es comparar dos listas. 

Ejercicio 9

#! /usr/bin/env python
# -*- coding: utf-8 -*-

def generar_n_caracteres (n, caracter):
    print n * caracter

Ejercicio 10

#! /usr/bin/env python
# -*- coding: utf-8 -*-

def procedimiento (lista):
    for i in lista:
        print i * "x"