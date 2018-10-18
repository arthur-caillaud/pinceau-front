from threading import Thread

class Reception(Thread):
    def __init__(self, connexion, verrou):
        Thread.__init__(self)
        self.connexion = connexion
        self.is_running = True
        self.verrou = verrou

    def run(self):
        while self.is_running :
            message = self.connexion.recv(1024).decode()
            if message.upper() == 'STOP':
                self.is_running = False
                print('fermeture_connexion')
                self.connexion.close()
            else :
                print(message)
