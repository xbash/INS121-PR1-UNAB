#python 3.4
#Autor: @kokesepulveda
#Cuenta las vocales que existe en una frase
a = 0
e = 0
i = 0
o = 0
u = 0
Palabra = "hola mundo mundialee"
for letra in Palabra:
	if letra == "a":
		a+=1
	elif letra == "e":
		e+=1
	elif letra == "i":
		i+=1
	elif letra == "o":
		o+=1
	elif letra == "u":
		u+=1
print("a=",a,"e=",e)