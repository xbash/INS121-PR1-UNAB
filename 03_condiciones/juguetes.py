# Buenos : 1-2
# Reparables: 3-7
#Irreparabales: 8-9
a = 1
buenos = 0
reparables = 0
irreparables = 0
while a != 0:
    a = int(input("Ingrese danio:"))
    if a == 1 or a == 2:
        buenos += 1 #buenos = buenos + 1
    elif a >= 3 and a <= 7:
        reparables += 1
    elif a == 0:
        break
    else:
        irreparables +=1
print(buenos,reparables,irreparables)
print ("Buenos: "+str((buenos/(buenos+reparables+irreparables))*100)+"%")
print ("Reparables: "+str((reparables/(buenos+reparables+irreparables))*100)+"%")
print ("Irreparables: "+str((irreparables/(buenos+reparables+irreparables))*100)+"%")
