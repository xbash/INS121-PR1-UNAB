def muchos_pcn():
    i = raw_input("Cuantos numeros quiere procesar: ")
        for j in range(0,i):
            x = raw_input("Ingrese un numero: ")
                if x > 0:
                    print ("Numero positivo")
                elif x == 0:
                    print ("Igual a 0")
                else:
                    print ("Numero negativo")
