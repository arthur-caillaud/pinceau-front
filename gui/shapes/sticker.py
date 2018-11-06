# External modules
from PIL import ImageTk, Image
try:
    from Tkinter import PhotoImage, NW
except ImportError:
    from tkinter import PhotoImage, NW
# Internal modules
try:
    from straight_shape import StraightShape
except ImportError:
    from gui.shapes.straight_shape import StraightShape

class Sticker(StraightShape):
    def __init__(self, shape):
        StraightShape.__init__(self, shape)

    def draw_on(self, canvas):
        image = ImageTk.PhotoImage(Image.open("stickers/laugh.png"))
        canvas_image = canvas.create_image(self._x1, self._y1, image=image, anchor=NW)
        return canvas_image
