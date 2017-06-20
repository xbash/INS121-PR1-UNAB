#main menu
opcionMenu = 0
print "Menu principal"
print "1) Submenu 1"
print "2) Submenu 2"
print "3) Retornar"
opcionMenu = input("Opcion: ")

if opcionMenu == 1:
	print "\nSubmenu 1"
	print "1) Opcion 1 submenu 1"
	print "2) Opcion 2 submenu 1"
	print "3) Volver a menu principal"
	opcionSubMenu = input("Opcion submenu 1: ")
	if opcionSubMenu=="1":
		print "Ejecutando opcion 1 del submenu 1"
	elif opcionSubMenu=="2":
		print "Ejecutando opcion 2 del submenu 1"
	else:
		print "Ejecutando opcion 3 del submenu 1"
elif opcionMenu == 2:
	print "\nSubmenu 2"
	print "1) Opcion 1 submenu 2"
	print "2) Opcion 2 submenu 2"
	print "3) Volver a menu principal"
	opcionSubMenu = input("Opcion submenu 2: ")
	if opcionSubMenu=="1":
		print "Ejecutando opcion 1 del submenu 2"
	elif opcionSubMenu=="2":
		print "Ejecutando opcion 2 del submenu 2"
	else:
		print "Ejecutando opcion 3 del submenu 2"
elif opcionMenu=="3":
    print "Volviendo al menu principal"
	#break
#main menu loop: no matter what is selected, player is directed back to main menu until option 3 (end turn) is selected:

while opcionMenu=="1" or opcionMenu=="2":
	opcionMenu=raw_input("Opcion: ")
	continue