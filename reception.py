from threading import Thread
import json

class Reception(Thread):
    def __init__(self, connexion, verrou, gui):
        Thread.__init__(self)
        self.__connexion = connexion
        self.__is_running = True
        self.__verrou = verrou
        self.__gui = gui

    def run(self):
        while self.__is_running :
            with self.__verrou:
                message = json.loads(self.__connexion.recv(1024))
                message['fill'] = 'red'
                self.__gui.draw(message)
