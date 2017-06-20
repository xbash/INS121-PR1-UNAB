"""
Ejemplo de input.txt:
hola mundo
chao mundo feo
estamos en clases de
programacion
"""
archivo = open ("02_MostarLineas2.txt")
for linea in archivo :
    print (linea, end="")
archivo.close()
