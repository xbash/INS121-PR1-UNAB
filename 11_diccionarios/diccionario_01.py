#Python27
#Autor Jorge

#forma para declarar un diccionario
diccionario = {'Chile':13, 'Argentina':14, 'Culombia':16}

#Mostrar por pantalla un diccionario
print diccionario['Chile']

#operacion
def menu():
  print 'Menu'
  opcion = input('Ingresa la opcion: ')
  if opcion == 1:
    print 'Llave Chile: ',diccionario['Chile']
  if opcion == 2:
    print 'Llave Argentina: ',diccionario['Argentina']
  if opcion == 3:
    print 'Llave Culombia: ',diccionario['Culombia']

#
diccionario = {'Chile':menu(), 'Argentina':14, 'Culombia':16}

llaves = diccionario.keys()
print 'Estas son las llaves del diccionario: ',llaves
