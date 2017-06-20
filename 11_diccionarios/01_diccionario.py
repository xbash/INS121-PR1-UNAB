#-------------------------------------------------------------------------------
# Name:        01_diccionario
# Purpose:
#
# Author:      jsepulveda
#
# Created:     18-10-2016
# Copyright:   (c) jsepulveda 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

alumnos = [{
"nombre":"Juan",
"fecha_nac":(1992,7,2),
"familia":{"papa":"Pedro","mama":"Luisa"},
"cursos":[
		{"sigla":"ING133","notas":[7,6,5.2]},
		{"sigla":"FIS120","notas":[6,4,3]}]
},{
"nombre":"Jorge",
"fecha_nac":(1983,7,2),
"familia":{"papa":"Mario","mama":"Maria"},
"cursos":[
		{"sigla":"INF320","notas":[7,6,5.2]},
		{"sigla":"MAT120","notas":[6,4,3]}]
}]
print(alumnos[0]["cursos"][1]["notas"][1])
for alumno in alumnos:
    print("")
    print("Notas de "+alumno["nombre"])
    for curso in alumno["cursos"]:
        suma = 0
        for nota in curso["notas"]:
            suma += nota
            promedio = round(suma/len(curso["notas"]),1)
            print("curso "+curso["sigla"]+": "+str(promedio))