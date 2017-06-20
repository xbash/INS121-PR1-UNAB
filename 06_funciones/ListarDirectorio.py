#python3
#Autor: @kokesepulveda
import os
def listarDirectorio(d,exte):
  #os.listdir(d) Lista contenido de directorio
  for i in os.listdir(d):
    if os.path.isdir(d+"\\"+i):
      listarDirectorio(d+"\\"+i,exte)
    if ext(i) == exte:
      print (i)
      
def ext(a):
  lista = a.split(".")
  return (lista[len(lista)-1])

listarDirectorio("D:\MegaNZ\03_UNAB\2016-SEM4\INS121_Progra1","txt")
