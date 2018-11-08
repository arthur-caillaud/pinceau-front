# External Modules
try:
    from Tkinter import Tk
except ImportError:
    from tkinter import Tk
# Internal Modules
try:
    from canvas import PinceauCanvas
    from menu import PinceauMenu
except ImportError:
    from gui.canvas import PinceauCanvas
    from gui.menu import PinceauMenu

# Class correcponding to the graphic user interface.
# We give it a size and a menu.
class GUI:
    def __init__(self):
        # Root
        self.__root = Tk()
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__root.title("Pinceau.io")
        # Properties
        self.__canvas = PinceauCanvas(self.__root, 1000, 1000)
        self.__menu = PinceauMenu(self.__root, self.__canvas.change_color, self.__canvas.change_shape)
        self.__menu.pack()
        self.__canvas.pack()
    # Main loop
    def run(self):
        self.__root.mainloop()
    def close(self):
       self.__root.destroy()
       self.__close_emission()
       self.__close_reception()
    # Exposed methods
    def draw(self, shape):
        # Methods enabling the drawing of a shape on the whiteboard.
        self.__canvas.draw(shape)
    def erase(self, shape):
        # Methods used to erase a shape on the whiteboard.
        self.__canvas.erase(shape)
    # Setters
    def set_send(self, send_func):
        self.__canvas.set_send(send_func)
    def set_close_emission(self, close_func):
        self.__close_emission = close_func
    def set_close_reception(self, close_func):
        self.__close_reception = close_func
