
#Programa de busqueda de multiplos en los n numeros naturales
#Multiplos de 3 o 7

print("Busqueda de numeros multiplos de 3 o 7 de una lista\n")
numero = input("Ingresa la cantidad de elementos de la lista: ")
multi=[] #declaracion de lista
largo = 0
for i in range(3,numero+1,1):
  if i % 3 == 0 or i % 7 == 0:
    multi.append(i) #agrega el numero al final del arreglo o lista
print(multi)

print("-----------")
print("Los numeros multiplos de 3 o 7 en el arreglo son: ")
largo = len(multi)
for i in range(0,largo,1):
  print("el elemento",i,"es =",multi[i])


