
def menu():
    opcion = 0
    print("Menu Principal")
    print("1).- Opcion 1")
    print("2).- Opcion 2")
    print("3).- Opcion 3")
    print("4).- Salir")
    opcion = input("Ingrese Opcion: ")
    return (opcion)

opcion = 0
while opcion != 4:
	opcion = menu()
	if opcion ==1:
		print("\nEjecutando opcion 1\n")
	elif opcion==2:
		print("\nEjecutando opcion 2\n")
	elif opcion==3:
		print("\nEjecutando opcion 3\n")
print("Saliendo del submenu...")

menu()