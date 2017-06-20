#Programa que solicita por pantalla el tamaño de la lista a considerar
#Muestra los numeros primos desde 1 al numero ingresado

num =int(input("Ingrese tamaño de lista: "))
Lista=[]
for rango in range(1,num+1):
    esPrimo=True
    for rango2 in range(2,num):
        if rango % rango2 == 0:
            esPrimo=False
            break
    if esPrimo:
        Lista.append(rango)
        print(Lista)