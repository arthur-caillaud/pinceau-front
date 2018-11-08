# External modules
import socket
from threading import Lock
import time
# Internal modules
from gui import GUI
from connect import Emission, Reception

port = 5000
connexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion.connect(('localhost', port))
print("Connexion established with server on port {}".format(port))

lock = Lock()
emission_socket = Emission(connexion, lock)
gui = GUI()
reception_socket = Reception(connexion, lock)

gui.set_send(emission_socket.set_cache)
gui.set_close_emission(emission_socket.close)
gui.set_close_reception(reception_socket.close)
reception_socket.set_draw(gui.draw)
reception_socket.set_erase(gui.erase)

emission_socket.start()
reception_socket.start()
gui.run()
