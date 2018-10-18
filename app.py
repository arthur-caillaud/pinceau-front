from gui import GUI
import socket
from threading import Lock
import time
from emission import Emission
from reception import Reception

host = "localhost"
port = 5001

connexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion.connect((host, port))
print("Connexion established with server on port {}".format(port))

lock = Lock()
emissionThread = Emission(connexion, lock)
gui = GUI(emissionThread)
receptionThread = Reception(connexion, lock, gui)

emissionThread.start()
receptionThread.start()
gui.run()
