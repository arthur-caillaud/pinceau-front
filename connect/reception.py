# External modules
from threading import Thread
import json

class Reception(Thread):
    # Constructors
    def __init__(self, connexion, verrou):
        # Reception is a child of Thread
        Thread.__init__(self)
        # Properties
        self.__connexion = connexion
        self.__is_running = True
        self.__verrou = verrou
        self.__cache = ''
    # Methods
    def run(self):
        while self.__is_running :
            message = self.__cache + self.__connexion.recv(1024).decode()
            try:
                shapes = json.loads(message)
                self.__cache = ''
                with self.__verrou:
                    for shape in shapes:
                        if shape['action'] == 'add':
                            self.draw(shape)
                        elif shape['action'] == 'erase':
                            self.erase(shape)
            except:
                self.__cache = message
    # Setters
    def set_draw(self, draw_func):
        self.draw = draw_func
    def set_erase(self, erase_func):
        self.erase = erase_func
