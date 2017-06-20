
# -*- coding: utf-8 -*-
#importacion de librerias
import urllib.request, json

req = urllib.request("https://libredte.cl/api/estadisticas/produccion")
opener = urllib.build_opener()
f = opener.open(req)
json = json.loads(f.read())
print(json)
print(json['unit'])

# Array example

import urllib2, json
req = urllib2.Request("http://vimeo.com/api/v2/video/38356.json")
opener = urllib2.build_opener()
f = opener.open(req)
json = json.loads(f.read())
print(json)
print(json[0]['title'])