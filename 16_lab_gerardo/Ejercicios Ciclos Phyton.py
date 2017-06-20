## Hacer un for desde 1 al 100 y que en el numero 50
## pregunte si quiere continuar 1:si 0:no
for contador in range(1,100):
	print("Iteración", contador)
	if contador==50:
		pregunta = int(input("Parar? 1:SI 0:NO "))
		if pregunta==1:
			break
		else:
			print("Sigo")
			pass
		pass
	pass

## numeros primos
es_primo = 1
for contador in range(2,20):
	for contador_dos in range(2,contador):
		if contador%contador_dos==0:
			es_primo = 0
			break
			pass
		pass
	if es_primo==0:
		print("No es primo",contador)
	else:
		print("Es primo",contador)
		pass
	es_primo = 1
	pass

## numeros pares hasta el 100
for contador in range(0,100):
	if contador%2==0:
		print("Número Par", contador)
		pass
	pass

## numeros impares hasta el 100
for contador in range(0,100):
	if contador%2==1:
		print("Número Par", contador)
		pass
	pass

## determinar si un numero es par o no
numero = int(input("Ingrese Número "))
if numero%2==0:
	print("Es número par")
else:
	print("Es número impar")
	pass

## multiplos de...
multiplo = int(input("Ingresa el número "))
for contador in range(1,10):
	print(contador*multiplo)
	pass

## pares usando while 	
contador = 0
while contador < 5:
	if contador%2==0:
		print("Número par",contador)
		pass
	contador = contador + 1
	pass

