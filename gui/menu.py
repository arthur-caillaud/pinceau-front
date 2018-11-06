# External modules
try:
    from Tkinter import Frame, BOTTOM
except ImportError:
    from tkinter import Frame, BOTTOM
# Internal modules
try:
    from buttons import create_ColorButton, create_ShapeButton
except ImportError:
    from gui.buttons import create_ColorButton, create_ShapeButton

class PinceauMenu:
    def __init__(self, master, change_color, change_shape):
        self.__master = master
        self.__color_buttons_frame = Frame(self.__master)
        self.__shape_buttons_frame = Frame(self.__master)
        self.__change_color = change_color
        self.__change_shape = change_shape
        self.__color_buttons = ['red', 'green', 'blue', 'orange', 'yellow', 'purple', 'pink', 'brown', 'white', 'black']
        self.__shape_buttons = ['rectangle', 'oval', 'line', 'sticker']

    def pack(self):
        self.__color_buttons_frame.pack(side = BOTTOM)
        self.__shape_buttons_frame.pack(side = BOTTOM)
        for color in self.__color_buttons:
            create_ColorButton(self.__color_buttons_frame, color, self.__change_color).pack()
        for shape in self.__shape_buttons:
            create_ShapeButton(self.__shape_buttons_frame, shape, self.__change_shape).pack()
