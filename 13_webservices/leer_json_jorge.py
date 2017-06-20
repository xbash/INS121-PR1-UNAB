import json, math
from pprint import pprint

#Se indica la ruta del archivo json local
with open('produccion.json') as data_file:    
    #decoded
	data = json.load(data_file)

totalContribuyentes = len(data["contribuyentes_activos"])
print("Total de contribuyentes activos: ",totalContribuyentes)
print("-"*30)

#mayorContribuyente
mayorContribuyente = -1
for contribuyente in data["contribuyentes_activos"]:
	if contribuyente["total"] >= mayorContribuyente:
		mayorContribuyente = contribuyente["total"]
print("Maximo de documentos totales: ",mayorContribuyente)

#menorContribuyente
menorContribuyente = 999999
for contribuyente in data["contribuyentes_activos"]:
	if contribuyente["total"] <= menorContribuyente:
		menorContribuyente = contribuyente["total"]
print("Minimo documentos totales: ",menorContribuyente)

#promedioContribuyente
for contribuyente in data["contribuyentes_activos"]:
	suma = 0
	suma += contribuyente["total"]
	promedio = (suma / totalContribuyentes)
print("El promedio de documentos totales es: ",promedio)

#desviacionEstandar
for contribuyente in data["contribuyentes_activos"]:
	sumaNumero = 0
	sumaNumero += (contribuyente["total"] - promedio)**2
	desviacion = ((sumaNumero / totalContribuyentes))**0.5
print("La desviacion estandar es: ",desviacion)

#Contribuyentes que mas emiten documentos
listaContribuyentes=[]
for contribuyente in data["contribuyentes_activos"]:	
	#listaContribuyentes.append(contribuyente["razon_social"]+","+str(contribuyente["emitidos"]))
	#alternativa
	listaContribuyentes.append(str('EMPRESA:')+','+contribuyente['razon_social']+','+str('EMITIDOS:')+','+str(contribuyente['emitidos']))
print(listaContribuyentes)


