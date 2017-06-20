print "diccionario punto\n"
punto = {'x':1, 'y':2, 'z':3}
print punto
print "\ndiccionario dias de la semana"
materias = {}
materias['lunes'] = [222,123]
materias['martes'] = [456]
materias['miercoles'] = [99,100]
materias['jueves'] = []
print materias
print "\nimprimiendo el valor de una clave del diccionario que no existe"
print materias.get('sabado')
print "\nrecorriendo un diccionario con un ciclo"
for dia in materias:
	print dia,":",materias[dia]