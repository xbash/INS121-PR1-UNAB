monto = int(input("Monto a pagar= "))
pagar = int(input("con cuanto paga ="))

vuelto = pagar - monto

if (vuelto /  500) > 0:
	print ("500 = ", int(vuelto / 500))
	vuelto = vuelto - 500 * int(vuelto/500)
	print ("queda = ", vuelto)
if (vuelto /  100) > 0:
	print ("100 = ", int(vuelto / 100))
	vuelto = vuelto - 100 * int(vuelto/100)
	print ("queda = ", vuelto)
if (vuelto /  50) > 0:
	print ("50 = ", int(vuelto / 50))
	vuelto = vuelto - 50 * int(vuelto/50)
	print ("queda = ", vuelto)
if (vuelto /  10) > 0:
	print ("10 = ", int(vuelto / 10))
	vuelto = vuelto - 10 * int(vuelto/10)
	print ("queda = ", vuelto)
if (vuelto /  5) > 0:
	print ("5 = ", int(vuelto / 5))
	vuelto = vuelto - 5 * int(vuelto/5)
	print ("queda = ", vuelto)
if (vuelto /  1) > 0:
	print ("1= ", int(vuelto / 1))
	vuelto = vuelto - 1 * int(vuelto/1)
	print ("queda = ", vuelto)
