import json
from pprint import pprint
from random import randint

with open('strings.json') as data_file:    
    data = json.load(data_file)

# este codigo crea el arreglo de diccionarios    
largo = len(data["contribuyentes_activos"])
contribuyentes = [] # diccionario
for i in data["contribuyentes_activos"]:
    contribuyente = {}
    contribuyente["razon_social"] = i["razon_social"]
    contribuyente["emitidos"] =  i["emitidos"]
    if data["contribuyentes_activos"][i]["emitidos"] is None: # esto es porque algunos emitidos decian none
        contribuyente["emitidos"] = 0
    contribuyentes.append(contribuyente)

pprint(contribuyentes) # imprimir normal

salir = 1
size = len(contribuyentes)
print(size)
while salir != 0:
    salir = 0
    for i in range(0,(size-1)):
        uno = contribuyentes[i]["emitidos"]
        dos = contribuyentes[i+1]["emitidos"]
        if uno < dos: # si el siguiente es mayor intercambio
            aux = contribuyentes[i]
            contribuyentes[i] = contribuyentes[i+1]
            contribuyentes[i+1] = aux
            salir = salir + 1
    
        
pprint(contribuyentes) # imprimir ordenados
