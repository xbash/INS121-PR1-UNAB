
#En un archivo se encuentran los nombres y asistencias de alumnos a un curso de la forma: juan 01111, donde los 1 reprensentan asistencia y los 0 inasistencia
#El programa debe retornar el porcentaje de asistencia al curso de cada alumno

archivo = open("14_AsistenciaAlumnos.txt","r")
for string in archivo:
    datos = string.strip().split(" ")
    asistencia = 0
    dias = len(datos[1])
    atrasos = 0
    inasistencia = 0
    for numero in datos[1]:
        if int(numero) == 1:
            atrasos = atrasos + 1
        elif int(numero) == 2:
            inasistencia = inasistencia + 1
    porcentaje = ((dias - inasistencia - int(atrasos/2)) / dias) * 100
    print(datos[0],porcentaje)
archivo.close()