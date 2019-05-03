from pyzabbix import ZabbixAPI
import sys
from pprint import pprint
import getpass
#################################################################
#                                                               #
#                                                               #
#                                                               #
#               Script creado por Team Monitoreo                #
#                           V.1.0                               #
#                   API Version 3.0.17                          #
#                                                               #
#################################################################


#Para utilizar este script se debe instalar la libreria pyzabbix
#La pueden instalar haciendo pip install pyzabbix
usuario = input("Ingrese nombre de usuario: ")
password = getpass.getpass("Ingrese password: ")
zapi = ZabbixAPI("http://clsgprdzabmtr01.ml.com/zabbix") #aqui le paso la informacion del server, tambien puedo pasar user y pass por aca
zapi.login(usuario,password)#Llamo a las variables de usuario y contraseña que solicité anteriormente
print("Conectado a Zabbix API Version %s" % zapi.api_version())#El OK de la conexion

hgroups = [ { 'name': 'parceritos1' }, { 'name': 'parceritos2' } ]#agrego tantos grupos como quiera, respetando este formato
query= zapi.do_request('hostgroup.create', hgroups)
pprint(query) #imprime los ID de los grupos creados