from straight_shape import StraightShape

class Circle(StraightShape):
    def __init__(self, shape):
        StraightShape.__init__(self, shape)

    def draw_on(self, canvas):
        return canvas.create_oval(self._x1, self._y1, self._x2, self._y2, fill=self._fill)
