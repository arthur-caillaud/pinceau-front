# External Modules
try:
    from Tkinter import Tk
except ImportError:
    from tkinter import Tk
# Internal Modules
from canvas import PinceauCanvas
from menu import PinceauMenu

class GUI:
    def __init__(self):
        self.__root = Tk()
        self.__root.title("Pinceau.io")

        self.__canvas = PinceauCanvas(self.__root, 1000, 1000)
        self.__menu = PinceauMenu(self.__root, self.__canvas.change_color, self.__canvas.change_shape)
        self.__menu.pack()
        self.__canvas.pack()

    def run(self):
        self.__root.mainloop()

    def draw(self, shape):
        self.__canvas.draw(shape)

    def set_send(self, send_func):
        self.__canvas.set_send(send_func)
