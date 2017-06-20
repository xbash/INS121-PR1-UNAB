### Agenda
a = 111
b = 222
c = 333
d = 444
agenda = {'Waldo':a, 'Crisitan':b, 'Madeleine':c, "Colombo":d}


def modificar():
    print "...Cambiar dato de..."
    print "\n[1] Waldo"
    print "\n[2] Cristian"
    print "\n[3] Madeleine"
    print "\n[4] Colombo"
    opcion = input("Ingresar la opcion: ")
    if opcion == 1:
        a = input("Ingresar nuevo numero de telefono: ")
    if opcion == 2:
        b = input("Ingresar nuevo numero de telefono: ")
    if opcion == 3:
        c = input("Ingresar nuevo numero de telefono: ")
    if opcion == 4:
        d = input("Ingresar nuevo numero de telefono: ")
        
    ## el valor de la variable cambia segun lo modificado...
    agenda = {'Waldo':a, 'Crisitan':b, 'Madeleine':c, "Colombo":d}

    ## llamo a menu...
    menu()
    
def contacto():
    print "..."
    menu()
    
def seach():
    print "..."
    print "\n[1] Waldo"
    print "\n[2] Cristian"
    print "\n[3] Madeleine"
    print "\n[4] Colombo"
    opcion = input("Ingresar la opcion: ")
    if opcion == 1:

    if opcion == 2:

    if opcion == 3:

    if opcion == 4:

    menu()
    
def chaofeo():
    print "..."


def menu():
    print "****************************"
    print "\tMenu"
    print "****************************"
    print "\n[1] Modificar Numero telefonico"
    print "\n[2] Mostrar Contactos"
    print "\n[3] Buscar dato de Contacto"
    print "\n[4] Salir"
    opcion = input("Igresar una opcion: ")
    if opcion == 1:
        modificar()
    if opcion == 2:
        contacto()
    if opcion == 3:
        seach()
    if opcion == 4:
        chaofeo()

menu()
