from threading import Thread
import json

class Emission(Thread):
    def __init__(self, connexion, verrou):
        Thread.__init__(self)
        self.__connexion = connexion
        self.__is_running = True
        self.__verrou = verrou
        self.__cache = None

    def run(self):
        self.connect()
        while self.__is_running :
            with self.__verrou:
                message = self.__cache
                if message != None:
                    self.__connexion.send(message)
                    self.__cache = None

    def send(self, action):
        self.__cache = json.dumps(action).encode()

    def connect(self):
        self.send({'action': 'connect'})
