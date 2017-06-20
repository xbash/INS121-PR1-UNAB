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
@version 2016-11-10
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
        print('  - '+g+': '+str(n)+' de '+str(total)+' ('+str(round((n/100)*100,2))+'%)')
    print()

# función que genera un archivo CSV con los datos de los contribuyentes activos
# Va un contribuyente por línea con las columnas de datos ordenados de la siguiente forma:
#   rut, razón social, usuario, grupos, nombre, emitidos, recibidos, total, sobre la cuota
def csvContribuyentesActivos(datos, archivo, sep = ';') :
    print('Generando archivo '+archivo)

    file = open(archivo, "w")
    file.write("rut"+sep+ "razon_social"+sep+"usuario"+sep+"grupos" +sep+ "nombre" +sep+"emitidos"+sep+ "recibidos"+sep+"total"+sep+"sobre_cuota"+sep+"\n")    
    for n in datos:
        
        file.write(str(n["rut"])+sep+ n["razon_social"]+sep+str(n["usuario"])+sep+" ".join(n["grupos"]) +sep+ n["nombre"] +sep+str(n["emitidos"])+sep+ str(n["recibidos"])+sep+ str(n["total"])+sep+str(n["sobre_cuota"])+sep+"\n")    
    file.close()         

    

# función que entrega el máximo de los totales de documentos (emitidos y recibidos)
# retorna un número entero
def maximoDocumentosTotales(datos) :
    maximo = None
    n=[]
    for x in datos:
        n.append(x["total"])
    return max(n)

# función que entrega el mínimo de los totales de documentos (emitidos y recibidos)
# retorna un número entero
def minimoDocumentosTotales(datos) :
    minimo = None
    n=[]
    for x in datos:
        n.append(x["total"])
    return min(n)


# función que entrega el promedio (o media) de los totales de documentos (emitidos y recibidos)
# retorna un número entero
def promedioDocumentosTotales(datos) :
    promedio = None
    suma=0
    cont=0
    for x in datos:
        suma+=int(x["total"])
        cont+=1
    promedio=int(suma/cont)
    
    return (promedio)

# función que entrega la desviación estándar de los totales de documentos (emitidos y recibidos)
# retorna un número entero
def desviacionEstandarDocumentosTotales(datos) :
    desviacion = None
    n=int(promedioDocumentosTotales(datos))
    total=0
    cont=0
    for x in (datos):
        cont+=1
        total+=(int(x["total"])-n)**2
    desviacion=int((total/(cont-1))**0.5)
    
    return (desviacion)
# función que entrega un arreglo con las contribuyentes que más documentos emiten
# retorna un arreglo de diccionarios con índices: razon_social y emitidos
# ordenados de mayor a menor emitidos. ejemplo:
# [{'razon_social': 'empresa 1', 'emitidos': 10}]
def contribuyentesConMasEmision(datos, cantidad) :
    contribuyentes = []
    n=[]
    lista=[]
    lista2=[]
    for m in datos:
        n.append(m["emitidos"])
        lista.append(m["razon_social"])
    for r in n:
        if r == None:
            lista2.append(0)
        else:
            lista2.append(r)
    
    for cant in range(0,cantidad):
        maximo=lista2[0]
        for dato in (range(len(lista2))):
            if lista2[dato] >= maximo:
                maximo=lista2[dato]
                indice=dato
        e={"razon_social":lista[indice],"emitidos":lista2[indice]}
        contribuyentes.append(e)
        lista.pop(indice)
        lista2.pop(indice)
    
    return (contribuyentes)
# función que entrega un arreglo con las contribuyentes que más documentos reciben
# retorna un arreglo de diccionarios con índices: razon_social y recibidos
# ordenados de mayor a menor recibidos. ejemplo:
# [{'razon_social': 'empresa 1', 'recibidos': 10}]
def contribuyentesConMasRecepcion(datos, cantidad) :
    contribuyentes2 = []
    n=[]
    lista=[]
    lista2=[]
    for m in datos:
        n.append(m["recibidos"])
        lista.append(m["razon_social"])
    for r in n:
        if r == None:
            lista2.append(0)
        else:
            lista2.append(r)
    
    for cant in range(0,cantidad):
        maximo=lista2[0]
        for dato in (range(len(lista2))):
            if lista2[dato] >= maximo:
                maximo=lista2[dato]
                indice=dato
        e={"razon_social":lista[indice],"recibidos":lista2[indice]}
        contribuyentes2.append(e)
        lista.pop(indice)
        lista2.pop(indice)
        
    return contribuyentes2

# función que entrega un arreglo con las contribuyentes que más documentos emiten
# y reciben (total)
# retorna un arreglo de diccionarios con índices: razon_social y total
# ordenados de mayor a menor totales. ejemplo:
# [{'razon_social': 'empresa 1', 'total': 10}]
def contribuyentesConMasEmisionRecepcion(datos, cantidad) :
    contribuyentes3 = []
    n=[]
    lista=[]
    lista2=[]
    for m in datos:
        n.append(m["total"])
        lista.append(m["razon_social"])
    for r in n:
        if r == None:
            lista2.append(0)
        else:
            lista2.append(r)
    
    for cant in range(0,cantidad):
        maximo=lista2[0]
        for dato in (range(len(lista2))):
            if lista2[dato] >= maximo:
                maximo=lista2[dato]
                indice=dato
        e={"razon_social":lista[indice],"total":lista2[indice]}
        contribuyentes3.append(e)
        lista.pop(indice)
        lista2.pop(indice)
        
    return contribuyentes3

# función que entrega un arreglo con las contribuyentes que están sobre la cuota
# retorna un arreglo de diccionarios con índices: razon_social y sobre_cuota
# ordenados de mayor a menor sobre la cuota. ejemplo:
# [{'razon_social': 'empresa 1', 'sobre_cuota': 10}]
def contribuyentesSobreCuota(datos) :
    contribuyentes4 = []
    # TODO"sobre_cuota"
    n=[]
    lista=[]
    lista2=[]
    indice=0
    for m in datos:
        n.append(m["sobre_cuota"])
        lista.append(m["razon_social"])
    for r in n:
        sc = r if r else 0
        lista2.append(sc)
    
    for cant in (range(len(lista2))):
        if lista2[cant] >= 1:
            indice=cant
            e={"razon_social":lista[indice],"sobre_cuota":lista2[indice]}
            contribuyentes4.append(e)       
        
        else:
            pass
        
        
    return  contribuyentes4

# función que entrega un arreglo con los usuarios que tienen una cantidad igual
# o superior de contribuyentes registrados a la indicada
# retorna una arreglo de diccionarios con índices: usuario y contribuyentes
# ordenados de mayor a menorcontribuyentes. ejemplo:
# [{'usuario': 'delaf', 'contribuyentes': 4}]
def usuariosConRegistroContribuyentesSuperiorA(datos, cantidad) :
    contribuyentes5=[]
    c={}
    lista=[]
    lista2=[]
    indice=0
    for d in datos:
        x=d["usuario"]
        if x in c:
            c[x]+=1
        else:
            c[x]=1
    for u in c:
        lista.append(u)
        lista2.append(c[u])
    for cant in range(len(lista)):
        if lista2[cant] >= cantidad:
            indice=cant
            e={"usuario":lista[indice],"contribuyentes":lista2[indice]}
            contribuyentes5.append(e)
    return contribuyentes5

# función que cuenta la cantidad de usuarios que están en cierto grupo
# se cuenta al usuario tantas veces como contribuyentes existan
# retorna un número entero con la cantidad de coincidencias
def usuariosEnGrupo(datos, grupo) :
    cantidad = 0
    for d in datos:
        for g in d["grupos"]:
            if g in grupo:
                cantidad+=1
        
    return cantidad
