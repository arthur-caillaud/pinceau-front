from threading import Thread
import json

class Reception(Thread):
    def __init__(self, connexion, verrou):
        Thread.__init__(self)
        self.__connexion = connexion
        self.__is_running = True
        self.__verrou = verrou
        self.__gui = None

    def run(self):
        while self.__is_running :
            message = json.loads(self.__connexion.recv(1024))
            with self.__verrou:
                self.__gui.draw(message)

    def set_gui(self, gui):
        self.__gui = gui
