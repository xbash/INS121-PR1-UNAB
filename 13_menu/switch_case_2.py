print "Menu principal"
print "1) opcion 1"
print "2) opcion 2"
print "3) salir"
opcionMenu = input("Ingresar una opcion: ")

salir = False
while not salir:
	if opcionMenu == 1:
		opcionSub = 0
		while opcionSub != 4:
			print "======================="
			print "\nSub menu principal 1 \n"
			print "======================="
			print "1) opcion 1"
			print "2) opcion 2"
			print "4) salir"
			opcionSub = input("Ingresar una opcion: ")
			if opcionSub == 1:
				print "\nEjecutando opcion 1 de submenu principal 1"
			elif opcionSub == 2:
				print "\nEjecutando opcion 2 de submenu principal 1"
			else:
				print "\nOpcion invalida!!"
		print "Saliendo del submenu principal 2"
	elif opcionMenu ==2 :
		opcionSub = 0
		while opcionSub != 4:
			print "======================="
			print "\nSub menu principal 2 \n"
			print "======================="
			print "1) opcion 1"
			print "2) opcion 2"
			print "4) salir"
			opcionSub = input("Ingresar una opcion: ")
			if opcionSub == 1:
				print "\nEjecutando opcion 1 de submenu principal 2"
			elif opcionSub == 2:
				print "\nEjecutando opcion 2 de submenu principal 2"
			else:
				print "\nOpcion invalida!!"
		print "Saliendo del submenu principal 2"
	elif opcionMenu == 3:
		salir = True
	else:
		print "\nOpcion incorrecta"
print "\nSaliendo del menu principal"