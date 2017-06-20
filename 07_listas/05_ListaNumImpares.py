#python27
#programa que cuenta numeros impares de un arreglo o lista

listaNum = []
numero = 0
cantidad = 0
contador = 0
cantidad = int(input("Ingresa la cantidad de elementos de la lista: "))
for i in range(0,cantidad,1):
  print(i+1,)
  numero = int(input(".- Ingresa un numero: "))
  listaNum.append(numero)
print("-----------")
print("La lista contiene: ",listaNum)

print("-----------")
for i in range(0,cantidad,1):
  if listaNum[i] % 2 == 1:
    print("El numero ingresado",listaNum[i],"es impar")
    contador = contador + 1
print("La cantidad de numeros impares en la lista es: ",contador)
