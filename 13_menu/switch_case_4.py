salir = False
while not salir:
	print "="*30
	print "\tMENU PRINCIPAL"
	print "="*30
	print "1) Opcion 1"
	print "2) Opcion 2"
	print "0) Salir"
	opcionMenu = input("Ingresar una opcion: ")

	if opcionMenu == 1:
		opcionSub = 9
		while opcionSub != 0:
			print "="*30
			print "\tSUB MENU 1"
			print "="*30
			print "1) Opcion 1"
			print "2) Opcion 2"
			print "0) Salir"
			opcionSub = input("Ingresar una opcion: ")
			if opcionSub == 1:
				print "\nEjecutando opcion 1 de SUB MENU 1"
			elif opcionSub == 2:
				print "\nEjecutando opcion 2 de SUB MENU 1"
			elif opcionSub == 0:
				break
			else:
				print "\nOpcion invalida!!"
		print "\nSaliendo de SUB MENU 1"
	elif opcionMenu == 2 :
		opcionSub = 9
		while opcionSub != 0:
			print "="*30
			print "\tSUB MENU 2"
			print "="*30
			print "1) Opcion 1"
			print "2) Opcion 2"
			print "0) Salir"
			opcionSub = input("Ingresar una opcion: ")
			if opcionSub == 1:
				print "\nEjecutando opcion 1 de SUB MENU 2"
			elif opcionSub == 2:
				print "\nEjecutando opcion 2 de SUB MENU 2"
			elif opcionSub == 0:
				break
			else:
				print "\nOpcion invalida!!"
		print "\nSaliendo de SUB MENU 2"
	elif opcionMenu == 0:
		salir = True
	else:
		print "\nOpcion invalida!!"
print "\nSaliendo de MENU PRINCIPAL"