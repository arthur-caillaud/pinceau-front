from Tkinter import Button, BOTTOM, LEFT

class ShapeButton:
    def __init__(self, frame, shape, change_shape):
        self.__frame = frame
        self.__shape = shape
        self.__change_shape = lambda: change_shape(self.__shape)
        self.__button = Button(self.__frame, text=self.__shape.upper(), command=self.__change_shape)

    def pack(self):
        self.__button.pack(side = LEFT)

class RectangleButton(ShapeButton):
    def __init__(self, frame, change_shape):
        ShapeButton.__init__(self, frame, 'rectangle', change_shape)

class OvalButton(ShapeButton):
    def __init__(self, frame, change_shape):
        ShapeButton.__init__(self, frame, 'oval', change_shape)

class LineButton(ShapeButton):
    def __init__(self, frame, change_shape):
        ShapeButton.__init__(self, frame, 'line', change_shape)
