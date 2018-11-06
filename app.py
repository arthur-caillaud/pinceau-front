# External modules
import socket
from threading import Lock
import time
# Internal modules
from gui import GUI
from connect import Emission, Reception

port = 5000

connexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion.connect(('138.195.244.85', port))
print("Connexion established with server on port {}".format(port))

lock = Lock()
emission_socket = Emission(connexion, lock)
gui = GUI()
reception_socket = Reception(connexion, lock)

gui.set_send(emission_socket.send)
reception_socket.set_draw(gui.draw)

emission_socket.start()
reception_socket.start()
gui.run()
