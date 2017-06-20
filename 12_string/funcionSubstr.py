#-------------------------------------------------------------------------------
# Name:        funcionSubstr
# Purpose:
#
# Author:      CMartinez
#
# Created:     18-10-2016
# Copyright:   (c) CMartinez 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#Funcion que retorna la parte del string que inicia en el indice start y de largo length

def Substr(String,Start,Length):
    if Length == 0 or Start > len(String)-1:
        return none
    if Start < 0:
        Start = 0
    if Length > len(String)-Start:
        Length=len(String)-Start
    aux = ""
    for i in range(Start,Start+Length):
        aux = aux + String[i]
    return aux

palabra = "abcdfgh"
print(Substr(palabra,2,2))


