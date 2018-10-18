from gui import GUI
import socket
from threading import Lock
import time
from emission import Emission
from reception import Reception

hote = "localhost"
port = 13803

connexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion.connect((hote, port))
print("Connexion etablie avec le serveur sur le port {}".format(port))

lock = Lock()
receptionThread = Reception(connexion, lock)
emissionThread = Emission(connexion, lock)

receptionThread.start()
emissionThread.start()

GUI(emissionThread).run()
