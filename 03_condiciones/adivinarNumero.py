c = 0
encontro = False
num = int(input("Ingresa un numero: "))
while (not encontro):
    c = c + 1
    numero = int(input("Ingresa un numero: "))
    if(numero>num):
        if(numero - num < 5):
            print("Casi")
        elif(numero - num < 10):
            print("Cerca")
        else:
            print("Lejos")
    elif(numero < num):
        if(num - numero < 5):
            print("Casi")
        elif(num - numero < 10):
            print("Cerca")
        else:
            print("Lejos")
    else:
        encontro = True
print("La persona realizo "+str(c)+" intentos")
