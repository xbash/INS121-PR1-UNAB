

num= int(raw_input('ingrese numero :'))
for i in range(1,18,1):
    for j in range(1,18,1):
        for k in range(1,18,1):
            result = i + j + k
            if result == num:
                print "Para :",num,"los sumandos son :",i, " ",j," ",k
