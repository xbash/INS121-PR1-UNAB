#python27
#Autor: Jorge Sepulveda
#Ejercicio 10: Determinar la suma de los n primeros numeros

suma = 0
print "-------------"
limite = int(raw_input("Ingrese el limite de numeros a sumar : "))

for i in range(0,limite,1):
	suma = suma + i
print "La suma de los",limite," primeros numeros es : ",suma