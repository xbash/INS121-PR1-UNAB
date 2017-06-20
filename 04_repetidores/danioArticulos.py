#python 3.4
#Autor: @kokesepulveda
#Bajo: 1-2
#Medio: 3-7
#Alto: 8-9

bajo = 0
medio = 0
alto = 0
dano = 1
print ("Ingrese danios de articulos, para terminar presione 0")
while dano !=0:
	dano = int(input("Ingrese danio del articulo: "))
	if dano >=1 and dano <=2:
		bajo +=1
	elif dano >=3 and dano <=7:
		medio +=1
	elif dano >=8 and dano <=9:
		alto +=1
print ("Bajos: "+str(bajo/(bajo+medio+alto))*100)+"%")
print ("Medio: "+str(medio/(bajo+medio+alto))*100)+"%")
print ("Alto:  "+str(alto/(bajo+medio+alto))*100)+"%")
