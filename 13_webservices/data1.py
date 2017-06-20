# -*- coding: utf-8 -*-
#importacion de librerias
import urllib.request, json

#leer json api
url = "https://libredte.cl/api/estadisticas/produccion"
try:
	response = urllib.request.urlopen(url)
	data = json.loads(response.read().decode())
	print(data)
	print((data["contribuyentes_activos"]))
	#Loop para mostrar resultados
	for item in data:
		print((item['contribuyentes_activos'][item]['razon_social']))