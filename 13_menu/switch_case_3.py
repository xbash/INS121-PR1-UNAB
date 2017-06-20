while 1:
	print "======================="
	print "\nMENU PRINCIPAL \n"
	print "======================="
	print "1) opcion 1"
	print "2) opcion 2"
	print "3) salir"
	opcionMenu = input("Ingresar una opcion: ")
	
	if opcionMenu == 1:
		opcionSub = 0
		while opcionSub != 4:
			print "======================="
			print "\nSUB MENU 1 \n"
			print "======================="
			print "1) opcion 1"
			print "2) opcion 2"
			print "4) salir"
			opcionSub = input("Ingresar una opcion: ")
			if opcionSub == 1:
				print "\nEjecutando opcion 1 de submenu 1"
			elif opcionSub == 2:
				print "\nEjecutando opcion 2 de submenu 1"
			else:
				print "\nOpcion invalida!!"
		print "Saliendo de submenu 1"
	elif opcionMenu ==2 :
		opcionSub = 0
		while opcionSub != 4:
			print "======================="
			print "\nSUB MENU 2 \n"
			print "======================="
			print "1) opcion 1"
			print "2) opcion 2"
			print "4) salir"
			opcionSub = input("Ingresar una opcion: ")
			if opcionSub == 1:
				print "\nEjecutando opcion 1 de submenu 2"
			elif opcionSub == 2:
				print "\nEjecutando opcion 2 de submenu 2"
			else:
				print "\nOpcion invalida!!"
		print "Saliendo de submenu 2"
	elif opcionMenu == 3:
		print "\nSaliendo del menu principal"
		break
	else:
		print "\nOpcion incorrecta"