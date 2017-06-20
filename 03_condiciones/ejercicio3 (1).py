monto = input("Monto a pagar= ")
pagar = input("con cuanto paga =")

vuelto = pagar - monto

if (vuelto /  500) > 0:
	print "500 = ", vuelto / 500
	vuelto = vuelto - 500 * (vuelto/500)
	print "queda = ", vuelto
if (vuelto /  100) > 0:
	print "100 = ", vuelto / 100
	vuelto = vuelto - 100 * (vuelto/100)
	print "queda = ", vuelto
if (vuelto /  50) > 0:
	print "50 = ", vuelto / 50
	vuelto = vuelto - 50 * (vuelto/50)
	print "queda = ", vuelto
if (vuelto /  10) > 0:
	print "10 = ", vuelto / 10
	vuelto = vuelto - 10 * (vuelto/10)
	print "queda = ", vuelto
if (vuelto /  5) > 0:
	print "5 = ", vuelto / 5
	vuelto = vuelto - 5 * (vuelto/5)
	print "queda = ", vuelto
if (vuelto /  1) > 0:
	print "1= ", vuelto / 1
	vuelto = vuelto - 1 * (vuelto/1)
	print "queda = ", vuelto
