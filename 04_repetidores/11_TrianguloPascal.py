"""
Triángulo de Pascal
Basado en código pascal.c
"""

LINEAS = 14
pasc = [0] * LINEAS
x = 0
i = 1

while i<=LINEAS :
	j = x
	while (j>=0) :
		if j==x or j==0 :
			pasc[j] = 1
		else :
			pasc[j] = pasc[j] + pasc[j-1]
		j -= 1
	x += 1
	print()
	for j in range (1, LINEAS-i+1) :
		print("   ", end="")
	for j in range(x) :
		print("%3d   " % pasc[j], end="")
	i += 1
print("\n")
