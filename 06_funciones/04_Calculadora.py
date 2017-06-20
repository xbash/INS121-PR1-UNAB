#//////////////////////////////////////////////
#////   UNAB - Facultad Ingenieria         ////
#////   07-05-2016 Santiago, Chile         ////
#////   Autor: Isui Rojas M.               ////
#////   Ing. en Computacion e Informatica  ////
#//////////////////////////////////////////////

# Funcion que recibe 2 variables para retornar resultado
def sumar(a,b):
	return a+b
# Funcion que recibe 2 variables para retornar resultado
def restar(a,b):
	return a-b
# Funcion que recibe 2 variables para retornar resultado
def dividir(a,b):
        if b == 0:
                print "No se puede dividir por 0"                
        else:
                return a/b
# Funcion que recibe 2 variables para retornar resultado
def multiplicar(a,b):
	return a*b

# Funcion que recibe variable para ejecutar alguna condicion
def operacion(o):
	# Condicion para salir del programa y retorna texto antes de salida
	if o == 5:
		print "Termino del Programa"
		# Retorna x para romper el ciclo de menu
		return 'x'
	# En caso de no salir ejecuta lo siguiente
	elif o == 1 or o == 2 or o == 3 or o == 4:
		i = float(input("Ingresar un numero: "))
		j = float(input("Ingresar otro numero: "))
		if o == 1:
			return sumar(i,j)
		if o == 2:
			return restar(i,j)
		if o == 3:
			return dividir(i,j)
		if o == 4:
			return multiplicar(i,j)


# Funcion que muestra un menu y retorna valor solicitado
def menu():
	print "*****************************"
	print "\n[1] Sumar"
	print "\n[2] Restar"
	print "\n[3] Dividir"
	print "\n[4] Multiplicar"
	print "\n[5] Exit"
	s = input("\nIngresar opcion: ")
	m = operacion(s)
	return m

m = 1
# Ciclo para menu, cuando m == x este terminara
while m != 'x':
	m = menu()
	if m != 'x':
		print m
		print "*****************************"
