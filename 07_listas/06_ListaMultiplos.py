#python3
#Programa de busqueda de multiplos de 2 y 6 en una lista de n numeros naturales

listaMult=[]
numero = int(input("Busqueda de multiplos de 2 y 6. Ingrese el largo del arreglo: "))
for i in range(2,numero+1,1):
    if i % 2 == 0 and i % 6 == 0:
        listaMult.append(i) #agrega el numero al final del arreglo o lista

print("--------")
print("los numeros multiplos de 2 y 6 en el arreglo son: ",listaMult)
