# -*- coding: utf-8 -*-

#Definir una función max() que tome como argumento dos números y devuelva el 
#mayor de ellos. (Es cierto que python tiene una función max() incorporada, 
#pero hacerla nosotros mismos es un muy buen ejercicio.

def max(n1,n2):
    if n1 < n2:
        return n2
    elif n2 < n1:
        return n1
    else:
        print("Son iguales")

print("Funcion maximo")
num1 = int(input("Ingresar el 1er numero: "))
num2 = int(input("Ingresar el 2do numero: "))
print("El numero maximo es: ",max(num1,num2))