from Tkinter import Tk
from canvas import PinceauCanvas

class GUI:
    def __init__(self):
        self.__root = Tk()
        self.__root.title("Pinceau.io")

        self.__canvas = PinceauCanvas(self.__root, 1000, 1000)
        self.__canvas.pack()

    def run(self):
        self.__root.mainloop()

    def draw(self, shape):
        self.__canvas.draw(shape)

    def set_emission_socket(self, emission_socket):
        self.__canvas.set_emission_socket(emission_socket)
