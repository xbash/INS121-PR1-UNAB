#-------------------------------------------------------------------------------
# Name:        numeros_primos
# Purpose:
#
# Author:      CMartinez
#
# Created:     18-10-2016
# Copyright:   (c) CMartinez 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#Indicar los numeros primos desde el 1 al 20
es_primo = 1
for contador in range(2,20):
    for contador_dos in range(2,contador):
        if contador%contador_dos == 0:
            es_primo = 0
            break
            pass
        pass
    if es_primo == 0:
        print("No es primo", contador)
    else:
        print("Es primo", contador)
        pass
    es_primo = 1
    pass