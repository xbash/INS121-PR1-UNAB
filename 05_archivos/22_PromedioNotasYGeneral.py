archivo = open("22_PromedioNotasYGeneral.txt","r")
contador = 0
for linea in archivo:
    contador += 1
    datos = linea.strip().split(";")
    notas=[]
    suma = 0
    for x in range(1,len(datos)):
        notas.append(float(datos[x]))
        for n in notas:
            suma = suma + n
            promedio = round((suma / len(notas)),1)
            print("El promedio de",datos[0]," es :",promedio)
            sumaGeneral = 0
            sumaGeneral = sumaGeneral + promedio
            promedioGeneral = round((sumaGeneral / contador),1)
            print("El promedio general es :",promedioGeneral)
archivo.close()