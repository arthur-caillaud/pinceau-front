# External modules
from threading import Thread
import json
# Class corresponding to the reception of a thread.
# Each object of this class is a Thread that will be running when,
# the user is listening to the server to know if ant new shape has been drawn.
class Reception(Thread):
    # Constructors
    def __init__(self, connexion, verrou):
        # Reception is a child of Thread
        Thread.__init__(self)
        # Properties
        self.__connexion = connexion
        self.__is_running = True
        self.__verrou = verrou
        # The cache is used to store all the existing shapes on the
        # whiteboard when a new client is connecting. Indeed, he needs to
        # receive all the shapes drawn by other clients before.
        # For decoding purposes, we reshape the message composed of maybe
        # +1024 characters.
        self.__cache = ''
    # Methods
    def run(self):
        while self.__is_running :
            message = self.__cache + self.__connexion.recv(1024).decode()
            try:
                shapes = json.loads(message)
                self.__cache = ''
                # We make sure that there is a Lock between each Thread so that the shapes,
                # are received and printed one after each other.
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
        # This method is used in app.py. It stores the received shape.
        # Obviously, each reception thread receives its own shape to draw.
        self.draw = draw_func
    def set_erase(self, erase_func):
        self.erase = erase_func
