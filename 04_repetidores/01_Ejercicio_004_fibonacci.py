a , b = 0 , 1
print "Ingresar cantidad de terminos a mostrar: "
n = input()
cont = 0

print "Los valores son los siguientes: "
while cont < n:
	print a
	a , b = b , a+b
	cont= cont + 1
