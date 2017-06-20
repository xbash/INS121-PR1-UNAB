#Lee datos de una matriz contenidos en un archivo y los procesa

archivo = open("21_MultiplicaMatrizArchivo.txt","r")
x = int(input("Ingrese un numero por el cual multiplicar la matriz: "))
for linea in archivo:
    fila = linea.strip().split(" ")
    for n in fila:
        print(x * int(n), end=" ")
archivo.close()