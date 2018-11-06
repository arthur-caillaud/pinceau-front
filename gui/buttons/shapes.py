# External modules
try:
    from Tkinter import Button, BOTTOM, LEFT
except ImportError:
    from tkinter import Button, BOTTOM, LEFT

class ShapeButton:
    # Class defining the shape buttons from the menu bar.
    def __init__(self, frame, shape, change_shape):
        self.__frame = frame
        self.__shape = shape
        self.__change_shape = lambda: change_shape(self.__shape)
        self.__button = Button(self.__frame, text=self.__shape.upper(), command=self.__change_shape)

    @staticmethod
    def create(frame, shape, change_shape):
        if shape == 'rectangle':
            return RectangleButton(frame, change_shape)
        elif shape == 'oval':
            return OvalButton(frame, change_shape)
        elif shape == 'line':
            return LineButton(frame, change_shape)
        elif shape == 'sticker':
            return StickerButton(frame, change_shape)

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

class StickerButton(ShapeButton):
    def __init__(self, frame, change_shape):
        ShapeButton.__init__(self, frame, 'sticker', change_shape)
