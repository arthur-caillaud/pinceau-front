from Tkinter import Tk
from canvas import PinceauCanvas

class GUI:
    def __init__(self, emissionSocket):
        self.__root = Tk()
        self.__root.title("Pinceau.io")

        self.__canvas = PinceauCanvas(self.__root, emissionSocket, 1000, 1000)
        self.__canvas.pack()

    def run(self):
        self.__root.mainloop()

    def draw(self, shape):
        self.__canvas.create_rectangle(shape)
