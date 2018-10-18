from gui import GUI
import socket
from threading import Lock
import time
from emission import Emission
from reception import Reception

host = "localhost"
port = 5000

connexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion.connect((host, port))
print("Connexion established with server on port {}".format(port))

lock = Lock()
receptionThread = Reception(connexion, lock)
emissionThread = Emission(connexion, lock)

receptionThread.start()
emissionThread.start()

GUI(emissionThread).run()
