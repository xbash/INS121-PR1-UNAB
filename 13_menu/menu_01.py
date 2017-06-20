def submenu1():
    opcionSubMenu=0
    print "\nSubmenu 1"
	print "1) Opcion 1 submenu 1"
    print "2) Opcion 2 submenu 1"
    print "4).- Salir"
    opcionSubMenu= int(raw_input ("Ingrese Opcion: "))
    return (opc)
	opcionSubMenu=0
	while opcionSubMenu!=4:
		opcionSubMenu = menu()
		if opcionSubMenu ==1:
			print "\nEjecutando opcion 1\n"
		elif opcionSubMenu==2:
			print "\nEjecutando opcion 2\n"
		elif opcionSubMenu==3:
			print "\nEjecutando opcion 3\n"

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