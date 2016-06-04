''' 
HERRAMIENTA/PRUEBAS PARA DELUGE

@version: 0
@autor: David Ramirez Sierra
@doc: Funciones RPC --> http://deluge.readthedocs.io/en/develop/core/rpc.html 

'''

import sys
import time
from deluge_client import DelugeRPCClient # https://github.com/JohnDoee/deluge-client

servidor='127.0.0.1'
puerto= 58846 # De tipo entero
username='localclient' # Se puede ver en home/.config/deluge/auth . Este es de level 10 = admin
password='a66a712b37e2aba2b7873856a0b4de49281a42a7' # Se puede ver en home/.config/deluge/auth

client = DelugeRPCClient(servidor, puerto, username, password)
client.connect()

if client.connected: 
	print "Conectado a " +servidor+':'+str(puerto)

if len(sys.argv) > 1:

	if sys.argv[1] == '-add':

		if sys.argv[2] == '-magnet':
			uri = sys.argv[3]
			client.call('core.add_torrent_magnet', uri,{})
		elif sys.argv[2] == '-torrent':
			uri = sys.argv[3]
			# TODO
		else:
			print 'Error: Algo no va bien...'

	elif sys.argv[1] == '-s':
		status = client.call('core.get_torrents_status', {}, [])

		if sys.argv > 2:
			if sys.argv[2] == '-list':
				print 'Num. de Torrents: '+ str(len(status))
				c=0
				for i in status.values():
					c+=1			
					print '////////////// TORRENT '+str(c)+' //////////////'
					for clave, valor in i.iteritems():
						print clave+': '+str(valor)

			if sys.argv[2] == '-peers':
				c=0
				for i in status.values():
					c+=1			
					print '////////////// TORRENT '+str(c)+' //////////////'
					pares =  i['peers']
					print 'Num. de pares: '+ str(len(pares))
					for p in pares:
						print 'IP: '+str(p['ip'])+ ','+p['country']


		



