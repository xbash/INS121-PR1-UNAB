#python 3.4

i = int(input("Cuantos numeros vas a procesar?: "))
for j in range(0,i):
	x = int(input("Ingrese un numero: "))
	if (x > 0):
		print ("Numero positivo")
	elif (x == 0):
		print ("Igual a 0")
	else:
		print ("Numero negativo")