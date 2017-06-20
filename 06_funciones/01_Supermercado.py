#python27
#Uso de funciones

def productos():
	print "\n--------------------"
	print "[1] leche"
	print "[2] cuadernos"
	print "[3] refresco"
	opcion = input("Ingresar opcion: ")
	#print "Ingresar opcion: "
	#opcion = input()
	if opcion == 1:
		leche()
	if opcion == 2:
		cuadernos()
	if opcion == 3:
		refresco()

def leche():
	chocolate = 650
	frutilla = 650
	blanca = 650
	print "\n--------------------"
	print "[1] chocolate"
	print "[2] frutilla"
	print "[3] blanca"
	opcion = input("Ingresar opcion: ")
	#print "\n Ingresar opcion: "
	#opcion = input()
	if opcion == 1:
		pagar(chocolate)
	if opcion == 2:
		pagar(frutilla)
	if opcion == 3:
		pagar(blanca)
		
def cuadernos():
	universitario = 850
	hoja_b = 750
	print "\n--------------------"
	print "[1] universitario"
	print "[2] hoja_b"
	opcion = input("Ingresar opcion: ")
	#print "\n Ingresar opcion: "
	#opcion = input()
	if opcion == 1:
		pagar(universitario)
	if opcion == 2:
		pagar(hoja_b)

def refresco():
	sprite = 700
	coca_cola = 800
	cherry_cola = 900
	print "\n--------------------"
	print "[1] sprite"
	print "[2] coca-cola"
	print "[3] cherry-cola"
	opcion = input("Ingresar opcion: ")
	if opcion == 1:
		pagar(sprite)
	if opcion == 2:
		pagar(coca_cola)
	if opcion == 3:
		pagar(cherry_cola)
	
def pagar(compra):
	#se definen los medios de pago para aplicar un descuento
	efectivo = 0.95
	cheque = 0.85
	tarjeta = 0.7
	total = 0
	print "\n--------------------"
	print "[1] efectivo"
	print "[2] cheque"
	print "[3] tarjeta"
	opcion = input("Ingresar opcion: ")
	#print "\n Ingresar opcion: "
	if opcion == 1:
		total = compra * efectivo
		print "\n--------------------"
		print "tiene que pagar la suma de: $",total
	if opcion == 2:
		total = compra * cheque
		print "\n--------------------"
		print "tiene que pagar la suma de: $",total
	if opcion == 3:
		total = compra * tarjeta
		print "\n--------------------"
		print "tiene que pagar la suma de: $",total

n = 0
print "HOLA BLA BLA"
while n == 0:
	print "\n--------------------"
	print "[1] ver productos"
	print "[2] salir"
	opcion = input("Ingresar opcion: ")
	#print "\n Ingresar opcion: "
	#opcion = input()
	if opcion == 1:
		productos()
	else:
		print "Gracias por la visita!"
		n += 1
	#else:
	#	exit()