## Clases 17-05-2016 Diccionarios

#a = input("ingresar: ")

midic = {'Waldo':'dsfdssds', 'Cristian':2, 'Souza':3}
def menu():
    print("****************************")
    print("\tMenu")
    print("****************************")
    opcion = input("ingresar una opcion: ")
    if opcion == 1:
        print("Key Waldo: ",midic['Waldo'])
    if opcion == 2:
        print("Key Cristian: ",midic['Cristian'])
    if opcion == 3:
        print("Key Souza: ",midic['Souza'])
        
# forma para declarar dic
midic = {'Waldo':menu(), 'Cristian':2, 'Souza':3}

# ahora se muestra en pantalla
print("****************************")
print("\tMi diccionario")
print("****************************")
#print midic
        
llaves = midic.keys()
print("Estas son las llaves del diccionario: ",llaves)

# capturar valor}
print(midic.get('Cristian'))
