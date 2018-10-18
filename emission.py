from threading import Thread
import json

class Emission(Thread):
    def __init__(self, connexion, verrou):
        Thread.__init__(self)
        self.connexion = connexion
        self.is_running = True
        self.verrou = verrou
        self.cache = None

    def run(self):
        while self.is_running :
            with self.verrou:
                message = self.cache
                if message != None:
                    self.connexion.send(message.encode())
                    self.cache = None

    def send(self, action):
        with self.verrou:
            self.cache = json.dumps(action)
