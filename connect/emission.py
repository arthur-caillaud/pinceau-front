# External modules
from threading import Thread
import json
# Class corresponding to the emission of a thread.
# Each object of this class is a Thread that will be running when,
# someone is drawing a shape.
class Emission(Thread):
    def __init__(self, connexion, verrou):
        Thread.__init__(self)
        self.__connexion = connexion
        self.__is_running = True
        self.__verrou = verrou
        self.__cache = None
    # We make sure that there is a Lock between each Thread so that the shapes,
    # are drawn one after each other.
    def run(self):
        self.connect()
        while self.__is_running :
            with self.__verrou:
                message = self.__cache
                if message != None:
                    self.__connexion.send(message)
                    self.__cache = None
    # If the message to send to the server is a shape, this method is used.
    def send(self, action):
        self.__cache = json.dumps(action).encode()
    # If the message to send to the server is a connection request,
    # then this method is used.
    def connect(self):
        self.send({'action': 'connect'})
