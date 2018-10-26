try:
    from Tkinter import Button, BOTTOM, LEFT
except:
    from tkinter import Button, BOTTOM, LEFT

class ColorButton:
    def __init__(self, frame, color, change_color):
        self.__frame = frame
        self.__color = color
        self.__tmp_color = ColorButton.to_tmp_color(self.__color)
        self.__final_color = ColorButton.to_final_color(self.__color)
        self.__change_color = lambda: change_color(self.__tmp_color, self.__final_color)
        self.__button = Button(self.__frame, text=self.__color.upper(), command=self.__change_color)

    @staticmethod
    def create(frame, color, change_color):
        if color == 'red':
            return RedButton(frame, change_color)
        elif color == 'green':
            return GreenButton(frame, change_color)
        elif color == 'blue':
            return BlueButton(frame, change_color)
        elif color == 'orange':
            return OrangeButton(frame, change_color)
        elif color == 'yellow':
            return YellowButton(frame, change_color)
        elif color == 'purple':
            return PurpleButton(frame, change_color)
        elif color == 'pink':
            return PinkButton(frame, change_color)
        elif color == 'brown':
            return BrownButton(frame, change_color)
        elif color == 'white':
            return WhiteButton(frame, change_color)
        elif color == 'black':
            return BlackButton(frame, change_color)

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
        elif color == 'brown':
            return '#A1887F'
        elif color == 'white':
            return '#FAFAFA'
        elif color == 'black':
            return '#424242'

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
        elif color == 'brown':
            return '#795548'
        elif color == 'white':
            return '#FFFFFF'
        elif color == 'black':
            return '#212121'

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

class BrownButton(ColorButton):
    def __init__(self, frame, change_color):
        ColorButton.__init__(self, frame, 'brown', change_color)

class WhiteButton(ColorButton):
    def __init__(self, frame, change_color):
        ColorButton.__init__(self, frame, 'white', change_color)

class BlackButton(ColorButton):
    def __init__(self, frame, change_color):
        ColorButton.__init__(self, frame, 'black', change_color)
