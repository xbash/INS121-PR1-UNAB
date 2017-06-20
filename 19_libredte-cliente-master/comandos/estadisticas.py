# -*- coding: utf-8 -*-

"""
LibreDTE
Copyright (C) SASCO SpA (https://sasco.cl)
Este programa es software libre: usted puede redistribuirlo y/o modificarlo bajo
los términos de la Licencia Pública General Affero de GNU publicada por la
Fundación para el Software Libre, ya sea la versión 3 de la Licencia, o (a su
elección) cualquier versión posterior de la misma.
Este programa se distribuye con la esperanza de que sea útil, pero SIN GARANTÍA
ALGUNA; ni siquiera la garantía implícita MERCANTIL o de APTITUD PARA UN
PROPÓSITO DETERMINADO. Consulte los detalles de la Licencia Pública General
Affero de GNU para obtener una información más detallada.
Debería haber recibido una copia de la Licencia Pública General Affero de GNU
junto a este programa.
En caso contrario, consulte <http://www.gnu.org/licenses/agpl.html>.
"""

"""
Comando para consultar las estadísticas de la aplicación web de LibreDTE
@author Esteban De La Fuente Rubio, DeLaF (esteban[at]sasco.cl)
@version 2016-11-22
"""

# opciones en formato corto
options = ''

# opciones en formato largo
long_options = ['certificacion', 'csv=', 'cantidad=']

# función principal del comando
def main (Cliente, args) :
    certificacion, csv, cantidad = parseArgs(args)
    if certificacion :
        ambiente = 'certificacion'
    else :
        ambiente = 'produccion'
    respuesta = Cliente.get('/estadisticas/'+ambiente)
    if respuesta.status_code!=200 :
        print('Error al obtener los datos para la estadística: '+respuesta.json())
        return respuesta.status_code
    datos = respuesta.json()
    if csv :
        csvContribuyentesActivos(datos['contribuyentes_activos'], csv)
    else :
        statsContribuyentesActivos(datos['contribuyentes_activos'], cantidad)
    return 0

# función que procesa los argumentos del comando
def parseArgs(args) :
    certificacion = 0
    csv = 0
    cantidad = 5
    for var, val in args:
        if var == '--certificacion' :
            certificacion = 1
        if var == '--csv' :
            csv = val
        if var == '--cantidad' :
            cantidad = val
    return certificacion, csv, cantidad

# función que genera la estadísticas de los contribuyentes activos
def statsContribuyentesActivos(datos, cantidad) :
    print()
    print('Estadística de LibreDTE')
    print('=======================')
    print()
    total = len(datos)
    # 1-4: promedio, desviación estándar, máximo y mínimo
    print('Total de empresas: '+str(total))
    print('Máximo de documentos totales: '+str(maximoDocumentosTotales(datos)))
    print('Mínimo documentos totales: '+str(minimoDocumentosTotales(datos)))
    print('Promedio de documentos totales: '+str(promedioDocumentosTotales(datos)))
    print('Desviación estándar de documentos totales: '+str(desviacionEstandarDocumentosTotales(datos)))
    print()
    # 5: contribuyentes que más emiten
    print('Contribuyentes que más documentos emiten:')
    contribuyentes = contribuyentesConMasEmision(datos, cantidad)
    for e in contribuyentes :
        print('  - '+e['razon_social']+' ('+str(e['emitidos'])+')')
    print()
    # 6: contribuyentes que más reciben
    print('Contribuyentes que más documentos reciben:')
    contribuyentes = contribuyentesConMasRecepcion(datos, cantidad)
    for e in contribuyentes :
        print('  - '+e['razon_social']+' ('+str(e['recibidos'])+')')
    print()
    # 7: contribuyentes que más emiten y reciben (total)
    print('Contribuyentes que más documentos emiten y reciben (total):')
    contribuyentes = contribuyentesConMasEmisionRecepcion(datos, cantidad)
    for e in contribuyentes :
        print('  - '+e['razon_social']+' ('+str(e['total'])+')')
    print()
    # 8: contribuyentes que están sobre la cuota
    print('Contribuyentes que están sobre la cuota:')
    contribuyentes = contribuyentesSobreCuota(datos)
    for e in contribuyentes :
        print('  - '+e['razon_social']+' ('+str(e['sobre_cuota'])+')')
    print()
    # 9: usuarios con más de un contribuyente registrado
    print('Usuarios con más de un contribuyente registrado')
    usuarios = usuariosConRegistroContribuyentesSuperiorA(datos, 2)
    for u in usuarios :
        print('  - '+u['usuario']+' ('+str(u['contribuyentes'])+')')
    print()
    # 10: usuarios que pertenecen a ciertos grupos
    print('Usuarios que pertenecen a los siguientes grupos:')
    grupos = ['dte_plus', 'lce_plus', 'rrhh_plus', 'inventario_plus']
    for g in grupos :
        n = usuariosEnGrupo(datos, g)
        print('  - '+g+': '+str(n)+' de '+str(total)+' ('+str(round((n/total)*100,2))+'%)')
    print()

# función que genera un archivo CSV con los datos de los contribuyentes activos
# Va un contribuyente por línea con las columnas de datos ordenados de la siguiente forma:
#   rut, razón social, usuario, grupos, nombre, emitidos, recibidos, total, sobre la cuota
def csvContribuyentesActivos(datos, archivo, sep = ';'):
	print('Generando archivo '+archivo)
	csvArchivo = open(archivo,'w')
	csvArchivo.write('rut'+sep+'razon_social'+sep+'usuario'+sep+'grupos'+sep+'nombre'+sep+'emitidos'+sep+'recibidos'+sep+'total'+sep+'sobre_cuota'+sep+'\n')
	for contribuyente in datos:
		csvArchivo.write(str(contribuyente['rut'])+sep+contribuyente['razon_social']+sep+str(contribuyente['usuario'])+sep+' '.join(contribuyente['grupos']) +sep+contribuyente['nombre']+sep+str(contribuyente['emitidos'])+sep+ str(contribuyente['recibidos'])+sep+ str(contribuyente['total'])+sep+str(contribuyente['sobre_cuota'])+sep+'\n')
	csvArchivo.close()

# función que entrega el máximo de los totales de documentos (emitidos y recibidos)
# retorna un número entero
def maximoDocumentosTotales(datos):
	maximo = None
	listaMax=[]
	for contribuyente in datos:
		listaMax.append(contribuyente['total'])
	return max(listaMax)

# función que entrega el mínimo de los totales de documentos (emitidos y recibidos)
# retorna un número entero
def minimoDocumentosTotales(datos):
	listaMin=[]
	minimo = None
	for contribuyente in datos:
		listaMin.append(contribuyente['total'])
	return min(listaMin)

# función que entrega el promedio (o media) de los totales de documentos (emitidos y recibidos)
# retorna un número entero
def promedioDocumentosTotales(datos):
	total = len(datos)
	suma = 0
	for contribuyente in datos:
		suma += contribuyente['total']
		promedio = int(suma / total)
	return promedio

# función que entrega la desviación estándar de los totales de documentos (emitidos y recibidos)
# retorna un número entero
def desviacionEstandarDocumentosTotales(datos):
	desviacion = None
	total = len(datos)
	sumaNumero = 0
	for contribuyente in datos:
		sumaNumero += (contribuyente['total'] - promedioDocumentosTotales(datos))**2
		desviacion = int((sumaNumero / total)**0.5)
	return desviacion

# función que entrega un arreglo con las contribuyentes que más documentos emiten
# retorna un arreglo de diccionarios con índices: razon_social y emitidos
# ordenados de mayor a menor emitidos. ejemplo:
# [{'razon_social': 'empresa 1', 'emitidos': 10}]
def contribuyentesConMasEmision(datos, cantidad):
	contribuyentes=[]
	listaEmitidos=[]
	listaRazonSocial=[]
	listaFinal=[]
	for contribuyente in datos:
		listaEmitidos.append(contribuyente['emitidos'])
		listaRazonSocial.append(contribuyente['razon_social'])
	for razonSocial in listaEmitidos:
		if razonSocial == None:
			listaFinal.append(0)
		else:
			listaFinal.append(razonSocial)
	for cantContribuyente in range(0,cantidad):
		maximo = listaFinal[0]
		for dato in (range(len(listaFinal))):
			if listaFinal[dato] >= maximo:
				maximo = listaFinal[dato]
				indice = dato
		final = {"razon_social":listaRazonSocial[indice],"emitidos":listaFinal[indice]}
		contribuyentes.append(final)
		listaRazonSocial.pop(indice)
		listaFinal.pop(indice)
	return contribuyentes

# función que entrega un arreglo con las contribuyentes que más documentos reciben
# retorna un arreglo de diccionarios con índices: razon_social y recibidos
# ordenados de mayor a menor recibidos. ejemplo:
# [{'razon_social': 'empresa 1', 'recibidos': 10}]
def contribuyentesConMasRecepcion(datos, cantidad):
	contribuyentes = []
	listaRecibidos=[]
	listaRazonSocial=[]
	listaFinal=[]
	for contribuyente in datos:
		listaRecibidos.append(contribuyente['recibidos'])
		listaRazonSocial.append(contribuyente['razon_social'])
	for razonSocial in listaRecibidos:
		if razonSocial == None:
			listaFinal.append(0)
		else:
			listaFinal.append(razonSocial)
	for cantContribuyente in range(0,cantidad):
		maximo = listaFinal[0]
		for dato in (range(len(listaFinal))):
			if listaFinal[dato] >= maximo:
				maximo = listaFinal[dato]
				indice = dato
		final = {"razon_social":listaRazonSocial[indice],"recibidos":listaFinal[indice]}
		contribuyentes.append(final)
		listaRazonSocial.pop(indice)
		listaFinal.pop(indice)
	return contribuyentes

# función que entrega un arreglo con las contribuyentes que más documentos emiten
# y reciben (total)
# retorna un arreglo de diccionarios con índices: razon_social y total
# ordenados de mayor a menor totales. ejemplo:
# [{'razon_social': 'empresa 1', 'total': 10}]
def contribuyentesConMasEmisionRecepcion(datos, cantidad):
	contribuyentes = []
	listaTotales=[]
	listaRazonSocial=[]
	listaFinal=[]
	for contribuyente in datos:
		listaTotales.append(contribuyente['total'])
		listaRazonSocial.append(contribuyente['razon_social'])
	for razonSocial in listaTotales:
		if razonSocial == None:
			listaFinal.append(0)
		else:
			listaFinal.append(razonSocial)
	for cantContribuyente in range(0,cantidad):
		maximo = listaFinal[0]
		for dato in (range(len(listaFinal))):
			if listaFinal[dato] >= maximo:
				maximo = listaFinal[dato]
				indice = dato
		final = {"razon_social":listaRazonSocial[indice],"total":listaFinal[indice]}
		contribuyentes.append(final)
		listaRazonSocial.pop(indice)
		listaFinal.pop(indice)
	return contribuyentes

# función que entrega un arreglo con las contribuyentes que están sobre la cuota
# retorna un arreglo de diccionarios con índices: razon_social y sobre_cuota
# ordenados de mayor a menor sobre la cuota. ejemplo:
# [{'razon_social': 'empresa 1', 'sobre_cuota': 10}]
def contribuyentesSobreCuota(datos):
	contribuyentes = []
	for contribuyente in datos:
		if contribuyente['sobre_cuota'] :
			contribuyentes.append(contribuyente)
	return contribuyentes

# función que entrega un arreglo con los usuarios que tienen una cantidad igual
# o superior de contribuyentes registrados a la indicada
# retorna una arreglo de diccionarios con índices: usuario y contribuyentes
# ordenados de mayor a menor contribuyentes. ejemplo:
# [{'usuario': 'delaf', 'contribuyentes': 4}]
def usuariosConRegistroContribuyentesSuperiorA(datos, cantidad):
	usuarios = []
	contribuyentes = {}
	listaUsuarios = []
	listaContribuyentes = []
	posicion = 0
	for contribuyente in datos:
		usuario = contribuyente['usuario']
		if usuario in contribuyentes:
			contribuyentes[usuario]+=1
		else:
			contribuyentes[usuario]=1
	for usuario in contribuyentes:
		listaUsuarios.append(usuario)
		listaContribuyentes.append(contribuyentes[usuario])
	for cantidadUsuario in range(len(listaUsuarios)):
		if listaContribuyentes[cantidadUsuario] >= cantidad:
			posicion = cantidadUsuario
			dato_grabar = {"usuario":listaUsuarios[posicion],"contribuyentes":listaContribuyentes[posicion]}
			usuarios.append(dato_grabar)
	return usuarios

# función que cuenta la cantidad de usuarios que están en cierto grupo
# se cuenta al usuario tantas veces como contribuyentes existan
# retorna un número entero con la cantidad de coincidencias
def usuariosEnGrupo(datos, grupo):
	cantidad = 0
	for contribuyente in datos:
		for idUsuario in contribuyente['grupos']:
			if idUsuario in grupo:
				cantidad += +1
	return cantidad