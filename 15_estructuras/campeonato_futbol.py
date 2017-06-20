#-------------------------------------------------------------------------------
# Name:        Campeonato de futbol
#
# Author:      Carlos Chesta
#-------------------------------------------------------------------------------
 
resultados = {
   ('Honduras', 'Chile'):    (0, 1),
   ('Espana',   'Suiza'):    (0, 1),
   ('Suiza',    'Chile'):    (0, 1),
   ('Espana',   'Honduras'): (3, 0),
   ('Suiza',    'Honduras'): (0, 0),
   ('Espana',   'Chile'):    (2, 1),
}
 
def obtener_lista_equipos(resultados):
    lista = []
    for tupla in resultados:
        for pais in tupla:
            if pais not in lista:
                lista.append(pais)
    return lista
 
def calcular_puntos(equipo, resultados):
    puntos = 0
    for tupla,marcador in resultados.items():
        if tupla[0] == equipo:
            if marcador[0] > marcador[1]:
                puntos += 3
            elif marcador [0] == marcador[1]:
                puntos += 1
        elif tupla[1] == equipo:
            if marcador[1] > marcador[0]:
                puntos += 3
            elif marcador [0] == marcador[1]:
                puntos += 1
    return puntos
 
def calcular_diferencia_de_goles(equipo, resultados):
    diferencia = 0
    for tupla,marcador in resultados.items():
        if tupla[0] == equipo:
            diferencia += marcador[0] - marcador[1]
        elif tupla[1] == equipo:
            diferencia += marcador[1] - marcador[0]
    return diferencia
 
def posiciones(resultados):
    paises = obtener_lista_equipos(resultados)
    lista = []
 
    for j in range(len(paises)):
        max_puntos = (-9999,-9999,'pais')
 
        for i in range(len(paises)):
            #(puntos, diferencia, pais)
            tupla = (calcular_puntos(paises[i], resultados), calcular_diferencia_de_goles(paises[i], resultados), paises[i])
            if max_puntos < tupla:
                max_puntos = tupla
        lista.append(max_puntos[2])
        paises.remove(max_puntos[2])
    return lista
 
print posiciones(resultados)