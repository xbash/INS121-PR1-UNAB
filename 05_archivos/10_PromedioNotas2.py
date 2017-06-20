"""
Ejemplo de 10_PromedioNotas2.txt
4
5.5
3.9
6.2
"""
suma = 0
numeros = 0
archivo = open ("10_PromedioNotas2.txt")
for linea in archivo :
    suma += float(linea) #suma = suma + float(linea)
    numeros += 1 #numeros = numeros + 1
archivo.close()
promedio = round(suma/numeros, 1)
print("El promedio de las notas es: ",promedio)
 
