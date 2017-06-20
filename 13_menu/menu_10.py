def opcion1():
	print "\nEjecutando opcion 1\n"
def opcion2():
	print "\nEjecutando opcion 2\n"

def menu():
	salir = False
	while not salir:
		print "1) opcion 1"
		print "2) opcion 2"
		print "0) opcion 0"
		opcion = int(input("Ingresa una opcion: "))
		if opcion == 1:
			opcion1()
		elif opcion == 2:
			opcion2()
		elif opcion == 0:
			salir = True
		else:
			print("\nOpcion incorrecta")
	print "Saliendo"

menu()