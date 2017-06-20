import urllib.request, json
url = "https://libredte.cl/api/estadisticas/produccion"
response = urllib.request.urlopen(url)
data = json.loads(response.read())
print(data)