#-------------------------------------------------------------------------------
# Name: Contar letras y palabras
#
# Author: Carlos Chesta
#-------------------------------------------------------------------------------
 
def contar_letras(oracion):
dicc = {}
for i in oracion.lower():
   if i != ' ':
      if letra in d:
         dicc[letra] += 1
      else:
         dicc[letra] = 1
 
return dicc
 
def contar_vocales(oracion):
    aux = oracion.lower()
    dicc = {}
    a = oracion.count('a')
    e = oracion.count('e')
    i = oracion.count('i')
    o = oracion.count('o')
    u = oracion.count('u')
 
    dicc['a']=a
    dicc['e']=e
    dicc['i']=i
    dicc['o']=o
    dicc['u']=u
    return dicc
 
 
def contar_iniciales(oracion):
    d = {}
    oracion2 = oracion.lower()
    d[oracion2[0]] = 1
 
    for i in range(len(oracion2)):
 
        if oracion2[i] == ' ':
            inicial = oracion2[i+1]
 
            if inicial not in d:
                d[inicial] = 1
            else:
                d[inicial] += 1
 
    return d
 
def palabras_repetidas(oracion):
    string = oracion.lower()
    lista = string.split()
    repetidas = []
    for i in lista:
        if lista.count(i)>1 and i not in repetidas:
            repetidas.append(i)
    return repetidas