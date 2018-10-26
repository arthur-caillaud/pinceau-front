from shape import Shape

class Line(Shape):
    def __init__(self, shape):
        Shape.__init__(self, shape)

    def draw_on(self, canvas):
        return canvas.create_line(self._x1, self._y1, self._x2, self._y2, fill=self._fill, width=2)
