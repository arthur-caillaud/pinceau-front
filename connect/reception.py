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
        is_running = self.is_running()
        while is_running :
            connexion, verrou, cache = self.get_connexion(), self.get_verrou(), self.get_cache()
            message = cache + connexion.recv(1024)
            try:
                shapes = json.loads(message)
                self.set_cache('')
                with verrou:
                    for shape in shapes:
                        self.draw(shape)
            except:
                self.set_cache(message)
    # Getters
    def get_verrou(self):
        return self.__verrou
    def get_connexion(self):
        return self.__connexion
    def is_running(self):
        return self.__is_running
    def get_cache(self):
        return self.__cache
    # Setters
    def set_draw(self, draw_func):
        self.draw = draw_func
    def set_cache(self, cache):
        self.__cache = cache
