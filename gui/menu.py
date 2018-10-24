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
        Button(self.__color_buttons, text="Yellow", command=self.change_to_yellow).pack(side=LEFT)
        Button(self.__color_buttons, text="Purple", command=self.change_to_purple).pack(side=LEFT)
        Button(self.__color_buttons, text="Pink", command=self.change_to_pink).pack(side=LEFT)

    def change_to_rectangle(self):
        self.__change_shape('rectangle')

    def change_to_oval(self):
        self.__change_shape('oval')

    def change_to_line(self):
        self.__change_shape('line')

    def change_to_red(self):
        self.__change_color('#E57373', '#F44336')

    def change_to_green(self):
        self.__change_color('#81C784', '#4CAF50')

    def change_to_blue(self):
        self.__change_color('#64B5F6', '#2196F3')

    def change_to_orange(self):
        self.__change_color('#FFB74D', '#FF9800')

    def change_to_yellow(self):
        self.__change_color('#FFF176', '#FFEB3B')

    def change_to_purple(self):
        self.__change_color('#9575CD', '#673AB7')

    def change_to_pink(self):
        self.__change_color('#F06292', '#E91E63')
