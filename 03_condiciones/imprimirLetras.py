#python 3.4
# imprime letras en posiciones impares de un string de palabra
i = 0
for letra in "holanda que talca?":
	if i%2==1:
		print(letra, end=" ")
	i+=1
print()