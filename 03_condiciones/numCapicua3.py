numero=int(input("Ingrese un numero "))
numFinal=numero
digito=0
while(numero!=0):
    resto=numero%10
    numero=numero/10
    digito=digito*10+resto
if(digito==numFinal):
    print("Numero capicua")
else:
    print("Numero no es capicua")
