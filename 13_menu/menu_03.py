def opcion1():
	print "\nEjecutando opcion 1\n"

def opcion2():
	print "\nEjecutando opcion 1\n"

def opcion3():
	print "\nEjecutando opcion 1\n"

def menu():
	opcion = 0
	while opcion != 4:
		print "1) Opcion 1"
		print "2) Opcion 2"
		print "3) Opcion 3"
		print "4) Salir"
		opcion = int(raw_input("Ingresa una opcion: "))
		if opcion == 1:
			opcion1()
		elif opcion == 2:
			opcion2()
		elif opcion == 3:
			opcion3()
	print "Saliendo gracias!"

##menu principal
menu()