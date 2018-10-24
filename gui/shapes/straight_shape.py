from shape import Shape

class StraightShape(Shape):
    def __init__(self, shape):
        # Parent __init__
        Shape.__init__(self, shape)
        # Self __init__
        x1x2_abs = abs(self._x2 - self._x1)
        y1y2_abs = abs(self._y2 - self._y1)
        x1x2 = self._x2 - self._x1
        y1y2 = self._y2 - self._y1
        if x1x2_abs < y1y2_abs :
            self._x2 = self._x1 + x1x2
            self._y2 = self._y1 + x1x2
        else :
            self._x2 = self._x1 + y1y2
            self._y2 = self._y1 + y1y2
