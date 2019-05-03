#################################################################
#                                                               #
#                                                               #
#                                                               #
#               Script creado por Team Monitoreo                #
#                           V.1.0                               #
#                   API Version 3.0.17                          #
#                   Crear Hosts en masa                         #
#################################################################

from pyzabbix import ZabbixAPI
import sys
from pprint import pprint
import getpass
import json
#Para utilizar este script se debe instalar la libreria pyzabbix
#La pueden instalar haciendo pip install pyzabbix
usuario = input("Ingrese nombre de usuario: ")
password = getpass.getpass("Ingrese password: ")
zapi = ZabbixAPI("http://clsgprdzabmtr01.ml.com/zabbix") #aqui le paso la informacion del server, tambien puedo pasar user y pass por aca
zapi.login(usuario,password)#Llamo a las variables de usuario y contraseña que solicité anteriormente
print("Conectado a Zabbix API Version %s" % zapi.api_version())#El OK de la conexion

with open('lista.json') as file: #Aqui leo el archivo donde estan los Host lo cargo y lo paso como variable
    data = json.load(file)
query= zapi.do_request('host.create', data)
pprint(query) #imprime los ID de los grupos creados