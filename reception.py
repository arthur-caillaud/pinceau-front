from threading import Thread

class Reception(Thread):
    def __init__(self, connexion, verrou):
        Thread.__init__(self)
        self.__connexion = connexion
        self.__is_running = True
        self.__verrou = verrou

    def run(self):
        while self.__is_running :
            message = self.__connexion.recv(1024).decode()
            if message.upper() == 'STOP':
                self.__is_running = False
                self.__connexion.close()
            else :
                print message
