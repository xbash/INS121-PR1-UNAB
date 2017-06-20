#python27

#declaracion de diccionario
agenda = {'Juan':123, 'Jose':456, 'Jorge':789, 'Juana':012, 'Joyce':345}

def modificar():
  print '...modificando dato de...'
  print '\n[1] Juan'
  print '\n[2] Jose'
  print '\n[3] Jorge'
  print '\n[4] Juanita'
  print '\n[5] Joyce'
  
  opcion = input('Ingresa la opcion')
  if opcion == 1:
    a = input('Ingresar un nuevo numero telefonico: ')
  if opcion == 2:
    b = input('Ingresar un nuevo numero telefonico: ')
  if opcion == 3:
    c = input('Ingresar un nuevo numero telefonico: ')
  if opcion == 4:
    d = input('Ingresar un nuevo numero telefonico: ')
  if opcion == 5:
    e = input('Ingresar un nuevo numero telefonico: ')
  
  ##el valor de la variable cambia por segun lo modificado
  agenda = {'Juan':a, 'Jose':b,'Jorge':c, 'Juanita':d, 'Joyce':e}

def contacto():
  print '...'
  menu()

def search():
  print '...'
  print '\n[1] Juan'
  print '\n[2] Jose'
  print '\n[3] Jorge'
  print '\n[4] Juanita'
  print '\n[5] Joyce'

def salid():
  print '\n Saliendo....'

def menu():
  print '*'*40
  print '\tMenu'
  print '*'*40
  print '\n[1] Modificar numeros telefonicos'
  print '\n[2] Mostrar numero'
  print '\n[3] Buscar datos de contacto'
  print '\n[4] Salir'
  opcion = input('Ingresar una opcion')
  if opcion == 1:
    modificar()
  if opcion == 2:
    contacto()
  if opcion == 3:
    search()
  if opcion == 4:
    salir()


menu()
