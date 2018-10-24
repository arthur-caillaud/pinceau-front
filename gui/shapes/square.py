from straight_shape import StraightShape

class Square(StraightShape):
    def __init__(self, shape):
        StraightShape.__init__(self, shape)

    def draw_on(self, canvas):
        return canvas.create_rectangle(self._x1, self._y1, self._x2, self._y2, fill=self._fill)
