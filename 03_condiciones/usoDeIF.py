#python 3.4
#Autor: @kokesepulveda

edad= int(input("Cuantos años tienes? "))
if edad >=1 and edad<=100:
    if edad>=1 and edad <=18:
        print("Es usted un menor de edad")
    elif edad >=18 and edad <=38:
        print("Es usted un LOLO en este Pais")
    elif edad >=39 and edad <=59:
        print("Es usted un adulto pero joven!!")
    elif edad >=60 and edad <=100:
        print("Venga ya!!, que aun es un adulto y servible!!")
    else:
        print("Lo siento, la edad podría sonar a increible pero eso no puede ser cierto!")
else:
    print("Lo siento, la edad podría sonar a increible pero eso no puede ser cierto!")
print("¡Hasta la proxima!")
