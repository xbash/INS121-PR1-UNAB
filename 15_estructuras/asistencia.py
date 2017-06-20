#-------------------------------------------------------------------------------
# Name:        Asistencia
#
# Author:      Carlos Chesta
#-------------------------------------------------------------------------------
 
alumnos = ['Pepito', 'Yayita', 'Fulanita', 'Panchito']
asistencia = [
[True, True, True, False, False, False, False],
[True, True, True, False, True,  False, True ],
[True, True, True, True,  True,  True,  True ],
[True, True, True, False, True,  True,  True ]]
 
def total_por_alumno(asistencia):
    contador = 0
    lista = []
    for i in asistencia:
        for j in i:
            if j:
                contador += 1
        lista.append(contador)
        contador = 0
    return lista
 
def alumno_estrella(asistencia):
    maximo = max(total_por_alumno(asistencia))
    for i in range(len(alumnos)):
        if total_por_alumno(asistencia)[i] == maximo:
            return alumnos[i]