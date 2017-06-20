"""
Escribir una funcion que reciba un diccionario, donde la llave sea el nombre de una
persona y el valor sea el genero (hombre o mujer), y para cada nombre imprima el
mensaje Estimado <nombre>, vote por mi, en caso de ser hombre, y Estimada
<nombre>, vote por mi en caso de ser mujer.
"""

Diccionario = {'Luisa':'mujer','Rosa':'mujer','Maria':'mujer','Luis':'hombre','Jorge':'hombre'}
for i in Diccionario:
	if Diccionario[i] == "mujer":
		print "Estimada",i,"vote por mi"
	elif Diccionario[i] == "hombre":
		print "Estimado",i,"vote por mi"
