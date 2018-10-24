from Tkinter import Frame, Button, BOTTOM, LEFT

class PinceauMenu:
    def __init__(self, master, change_color, change_shape):
        self.__master = master
        self.__color_buttons = Frame(self.__master)
        self.__shape_buttons = Frame(self.__master)
        self.__change_color = change_color
        self.__change_shape = change_shape

    def pack(self):
        self.__color_buttons.pack(side = BOTTOM)
        self.__shape_buttons.pack(side = BOTTOM)
        Button(self.__shape_buttons, text="Rectangle", command=self.change_to_rectangle).pack(side=LEFT)
        Button(self.__shape_buttons, text="Oval", command=self.change_to_oval).pack(side=LEFT)
        Button(self.__shape_buttons, text="Line", command=self.change_to_line).pack(side=LEFT)
        Button(self.__color_buttons, text="Red", command=self.change_to_red).pack(side=LEFT)
        Button(self.__color_buttons, text="Green", command=self.change_to_green).pack(side=LEFT)
        Button(self.__color_buttons, text="Blue", command=self.change_to_blue).pack(side=LEFT)
        Button(self.__color_buttons, text="Orange", command=self.change_to_orange).pack(side=LEFT)

    def change_to_rectangle(self):
        self.__change_shape('rectangle')

    def change_to_oval(self):
        self.__change_shape('oval')

    def change_to_line(self):
        self.__change_shape('line')

    def change_to_red(self):
        self.__change_color('magenta', 'red')

    def change_to_green(self):
        self.__change_color('green', 'green')

    def change_to_blue(self):
        self.__change_color('cyan', 'blue')

    def change_to_orange(self):
        self.__change_color('yellow', 'orange')
