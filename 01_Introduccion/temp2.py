num = 1
par = 0
impar = 0
while num < 2548:
	if(num%2 == 0):
		print(num,": es par")
		par +=+1
	else:
		print(num,": es impar")
		impar +=1
	num += 1
print("hay",par,"numeros par")
print("hay",impar,"numeros impar")