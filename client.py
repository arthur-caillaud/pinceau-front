import socket
from threading import Thread

hote = "localhost"
port = 13800

class Reception(Thread):
    def __init__(self, connexion):
        Thread.__init__(self)
        self.connexion = connexion
        self.is_running = True

    def run(self):
        while self.is_running :
            message_recu = self.connexion.recv(1024).decode()
            if message_recu.upper() == 'STOP':
                self.is_running = False
                print('fermeture_connexion')
                self.connexion.close()
            else :
                print(message_recu)


class Emission(Thread):
    def __init__(self, connexion):
        Thread.__init__(self)
        self.connexion = connexion
        self.is_running = True

    def run(self):
        while self.is_running :
            message_envoyer = input('')
            self.connexion.send(message_envoyer.encode())


connexion_au_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_au_serveur.connect((hote, port))
print("Connexion établie avec le serveur sur le port {}".format(port))


Reception(connexion_au_serveur).start()
Emission(connexion_au_serveur).start()
