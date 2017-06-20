#-------------------------------------------------------------------------------
# Name:        mostrar_100_numeros
# Purpose:
#
# Author:      CMartinez
#
# Created:     18-10-2016
# Copyright:   (c) CMartinez 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

for contador in range(1,101):
    print("Numero ",contador)
    if contador == 50:
        pregunta = int(input("Parar? 1:SI o 2:NO"))
        if pregunta == 1:
            print("Paramos!")
            break
        else:
            print("Sigo!")
            pass
        pass
    pass