#python27
#Autor: Jorge Sepulveda S.
#Ejercicio: Determinar el numero menor entre 2 numeros

num1=int(raw_input("Ingrese un 1er numero entero: "))
num2=int(raw_input("Ingrese un 1do numero entero: "))

if num1<num2:
	print "El numero menor es ",num1
elif num2<num1:
	print "El numero menor es ",num2
else:
	print "Los numeros son iguales"
