from math import sqrt
a=1
while a!=0:
    opcion = int(input("Ingrese la opcion: "))
    if opcion == 1:
        #sqrt
        numero = int(input("Ingrese el numero: "))
        print (math.sqrt(numero))  
    elif opcion == 2:
        numero = int(input("Ingrese el numero: "))
        print (numero**2)
    elif opcion == 3:
        numero = int(input("Ingrese el numero 1: "))
        numero2 = int(input("Ingrese el numero 2: "))
        print ("El numero es: "+str(numero**numero2))
    else:
        print ("No entendi la opcion")
        a = 0
