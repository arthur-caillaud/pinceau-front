from Tkinter import Button, BOTTOM, LEFT

class ColorButton:
    def __init__(self, frame, color, change_color):
        self.__frame = frame
        self.__color = color
        self.__tmp_color = ColorButton.to_tmp_color(self.__color)
        self.__final_color = ColorButton.to_final_color(self.__color)
        self.__change_color = lambda: change_color(self.__tmp_color, self.__final_color)
        self.__button = Button(self.__frame, text=self.__color.upper(), command=self.__change_color)

    def pack(self):
        self.__button.pack(side = LEFT)

    @staticmethod
    def to_tmp_color(color):
        if color == 'red':
            return '#E57373'
        elif color == 'green':
            return '#81C784'
        elif color == 'blue':
            return '#64B5F6'
        elif color == 'orange':
            return '#FFB74D'
        elif color == 'yellow':
            return '#FFF176'
        elif color == 'purple':
            return '#9575CD'
        elif color == 'pink':
            return '#F06292'

    @staticmethod
    def to_final_color(color):
        if color == 'red':
            return '#F44336'
        elif color == 'green':
            return '#4CAF50'
        elif color == 'blue':
            return '#2196F3'
        elif color == 'orange':
            return '#FF9800'
        elif color == 'yellow':
            return '#FFEB3B'
        elif color == 'purple':
            return '#673AB7'
        elif color == 'pink':
            return '#E91E63'

class RedButton(ColorButton):
    def __init__(self, frame, change_color):
        ColorButton.__init__(self, frame, 'red', change_color)

class GreenButton(ColorButton):
    def __init__(self, frame, change_color):
        ColorButton.__init__(self, frame, 'green', change_color)

class BlueButton(ColorButton):
    def __init__(self, frame, change_color):
        ColorButton.__init__(self, frame, 'blue', change_color)

class OrangeButton(ColorButton):
    def __init__(self, frame, change_color):
        ColorButton.__init__(self, frame, 'orange', change_color)

class YellowButton(ColorButton):
    def __init__(self, frame, change_color):
        ColorButton.__init__(self, frame, 'yellow', change_color)

class PurpleButton(ColorButton):
    def __init__(self, frame, change_color):
        ColorButton.__init__(self, frame, 'purple', change_color)

class PinkButton(ColorButton):
    def __init__(self, frame, change_color):
        ColorButton.__init__(self, frame, 'pink', change_color)
