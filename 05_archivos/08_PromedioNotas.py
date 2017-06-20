archivo = open("08_input.txt")
promedio_general = 0
alumnos = 0
aprobados = []
reprobados = []
for linea in archivo:
    linea = linea.strip().split(":")
    nombre = linea[0]
    apellido = linea[1]
    nota1 = int(linea[2])
    nota2 = int(linea[3])
    nota3 = int(linea[4])
    promedio = (nota1+nota2+nota3)/3
    if promedio >= 40:
        aprobados.append(nombre+" "+apellido)
    else:
        reprobados.append(nombre+" "+apellido)
    #print("Promedio de "+nombre+" "+apellido+": "+str(promedio))
    promedio_general += promedio
    alumnos +=1
#print("Promedio general es: "+str(promedio_general/alumnos))
def ArrayToFile(lista,archivo):
    abrir = open(archivo,"w+")
    for i in lista:
        abrir.write(str(i)+"\n")
    abrir.close()

ArrayToFile(aprobados,"08_aprobados.txt")
ArrayToFile(reprobados,"08_reprobados.txt")

print("Alumnos aprobados: "+str(aprobados))
print("Alumnos reprobados: "+str(reprobados))
archivo.close()

