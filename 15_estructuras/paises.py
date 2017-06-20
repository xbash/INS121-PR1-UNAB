#-------------------------------------------------------------------------------
# Name:        Paises
#
# Author:      Carlos Chesta
#-------------------------------------------------------------------------------
 
paises = {
    'Pepito': {'Chile', 'Argentina'},
    'Yayita': {'Francia', 'Suiza', 'Chile'},
    'John': {'Chile', 'Italia', 'Francia', 'Peru'},
}
 
def cuantos_en_comun(a,b):
    num = len((paises[a] & paises[b]))
    return num