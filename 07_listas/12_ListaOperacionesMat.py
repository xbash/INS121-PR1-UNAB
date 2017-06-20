from random import *
#para utilizar la funcion de numeros aleatorios entre [a,b]
lista=[]
for i in range(10):
	lista.append(randint(1,100)) #inserta elementos
	print(lista[i])

print("-"*10)
print("Lista: ",lista)
max = max(lista) #minimo
min = min(lista) #maximo
largo = len(lista) #largo lista
sum = sum(lista) #suma total
del(lista[5]) #elimina 6to elemento
print("maximo:",max,"\nminimo:",min,"\nlargo:",largo,"\nsuma: ",sum)
