#-------------------------------------------------------------------------------
# Name:        Signo zodiacal
#
# Author:      Carlos Chesta
#-------------------------------------------------------------------------------
 
def determinar_signo(fecha_de_nacimiento):
    _,mes,dia = fecha_de_nacimiento
    fecha = (mes,dia)
    if (12,22) <= fecha or fecha <= (1,20):
            return 'capricornio'
    for i,j in signos.items():
        inicio,termino = j
        tupla_zodiacal =(inicio,termino)
 
        if inicio <= fecha and fecha <= termino:
            return i
 
signos = {
   'aries':       (( 3, 21), ( 4, 20)),
   'tauro':       (( 4, 21), ( 5, 21)),
   'geminis':     (( 5, 22), ( 6, 21)),
   'cancer':      (( 6, 22), ( 7, 23)),
   'leo':         (( 7, 24), ( 8, 23)),
   'virgo':       (( 8, 24), ( 9, 23)),
   'libra':       (( 9, 24), (10, 23)),
   'escorpio':    ((10, 24), (11, 22)),
   'sagitario':   ((11, 23), (12, 21)),
   'capricornio': ((12, 22), ( 1, 20)),
   'acuario':     (( 1, 21), ( 2, 19)),
   'piscis':      (( 2, 20), ( 3, 20)),
}