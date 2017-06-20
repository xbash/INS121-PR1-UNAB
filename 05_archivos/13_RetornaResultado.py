#retornar la operacion de los numeros del archivo
#eje 1 + 3 debiera retornar 4
print("Programa que lee numeros y su operacion aritmetica desde un archivo y retorna el resultado")
archivo = open("13_RetornaResultado.txt","r")
for linea in archivo:
    datos = linea.strip().split(" ")
    num1 = int(datos[0])
    num2 = int(datos[2])
    if datos[1] == "+":
        print(num1+num2)
    elif datos[1] == "-":
        print(num2-num1)
    elif datos[1] == "*":
        print(num1*num2)
    elif datos[1] == "/":
        print(num1/num2)

archivo.close()