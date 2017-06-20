#python 3.4
#Autor: @kokesepulveda
#Este programa solicita por pantalla el ingreso de numeros para luego
#insertarlos en la lista
lista=[]
lista_suma=[]
suma=0

for i in range(5):
    elem=int(input("Inserte numero: "))
    lista.append(elem)
print(lista)

for j in lista:
    suma=int(j)
    lista_suma.append(suma)

print(lista_suma)
