#deluge

Herramienta para hacer pruebas desde un cliente Deluge

##Requirements

    Deluge 1.3.x
    Python 2.6, 2.7, 3.3, 3.4
    deluge-client (https://pypi.python.org/pypi/deluge-client/1.0.1)

##Usage
En primer lugar, se lanza el servidor de torrents `sudo deluged`

Opciones disponibles desde el Terminal:
### Status
Listarlo  todo
`python deluge.py -s -list`

Listar los pares (peers)
`python deluge.py -s -peers`

### Add
Añadir torrent por magnet link
`python deluge.py -add -magnet <uri>` 

##Notas
El 'username' y 'password' se pueden encontrar en `home/.config/deluge/auth` donde también se pueden añadir usuarios con diferentes niveles (http://dev.deluge-torrent.org/wiki/UserGuide/Authentication)

Lanzar la consola de deluge `sudo deluge -u console`

Lanzar la interfaz web `sudo deluge-web` 
