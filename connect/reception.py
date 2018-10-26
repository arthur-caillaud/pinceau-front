from threading import Thread
import json

class Reception(Thread):
    def __init__(self, connexion, verrou):
        Thread.__init__(self)
        self.__connexion = connexion
        self.__is_running = True
        self.__verrou = verrou

    def run(self):
        while self.__is_running :
            message = self.__connexion.recv(1024)
            print message
            shape = json.loads(message)
            print shape
            with self.__verrou:
                self.__draw(message)

    def set_draw(self, draw_func):
        self.__draw = draw_func
