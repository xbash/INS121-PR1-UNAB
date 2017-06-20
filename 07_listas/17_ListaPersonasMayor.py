#ptyhon 3.4
"""
Da las listas
    edades=[10,27,17]
    nombres=["Juanito","Clavo","un Clavito"]
Donde la pesona con edad edades[i] se llama nombres[i], indicar nombre de:
    persona mayot
    persona menor
"""
edades=[3,5,8,12,18]
nombres=["","","","",]
edadMayor=edades[0]
edadMenor=edades[0]
indiceMayor=0
indiceMenor=0
#[0,....,len(edades)-1]
for i in range(len(edades)):
    if edades[i]>edadMayor:
        edadMayor=edades[i]
        indiceMayor=i
    if edades[i]<edadMenor:
        edadMenor=edades[i]
        indiceMenor=i
print("Mayor",nombres[indiceMayor])
print("Menor",nombres[indiceMenor])
