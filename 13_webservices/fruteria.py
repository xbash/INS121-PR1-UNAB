import json

data = {"Fruteria":
 [
  {"Fruta":
   [
    {"Nombre":"Manzana","Cantidad":10},
    {"Nombre":"Pera","Cantidad":20},
    {"Nombre":"Naranja","Cantidad":30}
   ]
  },
  {"Verdura":
   [
    {"Nombre":"Lechuga","Cantidad":80},
    {"Nombre":"Tomate","Cantidad":15},
    {"Nombre":"Pepino","Cantidad":50}
   ]
  }
 ]
}

#encoded
data_string = json.dumps(data)

#decoded
decoded = json.loads(data_string)

print("-"*30)
print("Tenemos "+str(decoded["Fruteria"][1]["Verdura"][0]["Cantidad"])+" Lechugas.")
print("Tenemos las siguientes verduras: "+str(decoded["Fruteria"][1]["Verdura"]))
for 