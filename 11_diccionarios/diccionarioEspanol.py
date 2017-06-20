"""
Disene una funcion de nombre DiccionarioEspanol que reciba tres parametros, el primero de
ellos es un diccionario D, el segundo recibira una palabra S y el tercero su signicado sig, a~nadira S
y sig al diccionario D y retornara D con la nueva palabra ingresada. Luego retornara el diccionario.
En un menu indique al usuario si desea a~nadir palabras a su diccionario, o si desea consultar el
signicado de alguna palabra.
"""
def DiccionarioEspanol(Dicc, Palab, Signif):
	Dicc[Palab] = Signif
	return Dicc

Diccionario = dict()
opcion = 0
while opcion != 4: #bucle
	print "Ingrese la opcion que desea ejecutar"
	print "1) Ingresar palabra"
	print "2) Consultar significado"
	print "3) Mostrar palabra"
	print "4) Salir"
	opcion = input("Ingrese opcion: ")
	
	if opcion == 1:
		print "\nOpcion 1 - Ingreso de nueva palabra al diccionario"
		Palabra = raw_input("Ingrese palabra: ")
		Significado = raw_input("Ingrese significado: ")
		Diccionario = DiccionarioEspanol(Diccionario,Palabra,Significado)
	elif opcion == 2:
		print "\nOpcion 2 - Consultar al diccionario una palabra"
		Palabra = raw_input("Ingrese palabra: ")
		print "El significado de",Palabra," es:",Diccionario[Palabra]
	elif opcion == 3:
		#Diccionario = DiccionarioEspanol(Diccionario,Palabra,Significado)
		print "\nOpcion 3 - Mostrar las palabras almacenadas en el diccionario"
		Palabra = Diccionario.keys()
		for i in Palabra:
			print "- ",i
	print ""