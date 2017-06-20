def opcion1 () :
	print ("Ejecutando opcion 1")

def opcion2 () :
	print ("Ejecutando opcion 2")

def menu () :
	salir = False
	while not salir :
		print ("1. Opcion 1")
		print ("2. Opcion 2")
		print ("0. Salir")
		opcion = int (input("Ingrese su opcion: "))
		if opcion == 1 :
			opcion1()
		elif opcion == 2 :
			opcion2()
		elif opcion == 0 :
			salir = True
		else :
			print ("Opcion incorrecta")
	print ("Saliendo")

menu ()
