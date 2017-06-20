while True:
    z = int(input("Ingrese Z: "))
    var = 0
    for n in range(z):
        var = var + ((-1)**n)/((n*2)+1)
    print (var*4)
