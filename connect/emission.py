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
                self.send_cache()
    # Send the content of the cache to the backend server
    def send_cache(self):
        action = self.__cache
        if action != None:
            message = json.dumps(action).encode()
            self.__connexion.send(message)
            self.__cache = None
            if action['action'] == 'disconnect':
                self.__is_running = False
    # Set the cache that will be send to the backend server
    def set_cache(self, action):
        self.__cache = action
    # The first request emitted to the server is a sync request to get all past actions
    def connect(self):
        self.set_cache({'action': 'sync'})
    def close(self):
        self.set_cache({'action': 'disconnect'})
