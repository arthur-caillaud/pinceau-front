from straight_shape import StraightShape
try:
    from Tkinter import PhotoImage
except:
    from tkinter import PhotoImage

class Sticker(StraightShape):
    def __init__(self, shape):
        StraightShape.__init__(self, shape)

    def draw_on(self, canvas):
        image = PhotoImage(file="stickers/laugh.png")
        return canvas.create_image(self._x1, self._x2, image=image, anchor=NW)
