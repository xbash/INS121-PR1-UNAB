#Se agregan datos a la lista, se copia a 2da lista y se imprime el
#contenido en 2 formas

milista=[]
milista.append(1)
milista.append(2)
milista.append(3)

print(milista[0]) #imprime 1
print(milista[1]) #imprime 2
print(milista[2]) #imprime 3

#imprime el contenido completo de la lista forma 1
print("---------")
for i in milista:
  print(i)

#Copio el contenido de milista a milista2
#imprime el contenido de la lista forma 2
milista2 = milista[:]
print("Lista 2: ",milista2)