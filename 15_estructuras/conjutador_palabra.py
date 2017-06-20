#-------------------------------------------------------------------------------
# Name:        Conjugador de verbos
#
# Author:      Carlos Chesta
#-------------------------------------------------------------------------------
 
pronombres = ['yo', 'tu', 'el', 'nosotros', 'vosotros', 'ellos']
 
conjugacion = {
'ar': ('o', 'as', 'a', 'amos', 'ais', 'an'),
'er': ('o', 'es', 'e', 'emos', 'is', 'en'),
'ir': ('o', 'es', 'e', 'imos', 'is', 'en')}
 
verbo = raw_input("Ingrese verbo: ")
 
comienzo = verbo[:-2]
terminacion = verbo[-2:]
 
for i in range(len(pronombres)):
    print pronombres[i] + " " + comienzo + conjugacion[terminacion][i]