# Internal modules
try:
    from shape import Shape
except ImportError:
    from gui.shapes.shape import Shape

# Class conditionning the new shape to a "straight shape".
# A rectangle becomes a square, a oval becomes a circle and
# a line becomes a diagonal.
class StraightShape(Shape):
    def __init__(self, shape):
        # Parent __init__
        Shape.__init__(self, shape)
        # Self __init__
        x1x2_abs = abs(self._x2 - self._x1)
        y1y2_abs = abs(self._y2 - self._y1)
        if x1x2_abs < y1y2_abs :
            self.set_x2y2(x1x2_abs)
        else :
            self.set_x2y2(y1y2_abs)
    # We define methods acting on the coordinates of the shape being created.
    # We change the coordinates so that the shape remains "straight".
    def set_x2y2(self, dist):
        x1x2 = self._x2 - self._x1
        y1y2 = self._y2 - self._y1
        if x1x2 < 0:
            if y1y2 < 0:
                self.set_x2y2_topleft(dist)
            else:
                self.set_x2y2_bottomleft(dist)
        else:
            if y1y2 < 0:
                self.set_x2y2_topright(dist)
            else:
                self.set_x2y2_bottomright(dist)

    def set_x2y2_topleft(self, dist):
        self._x2 = self._x1 - dist
        self._y2 = self._y1 - dist

    def set_x2y2_bottomleft(self, dist):
        self._x2 = self._x1 - dist
        self._y2 = self._y1 + dist

    def set_x2y2_topright(self, dist):
        self._x2 = self._x1 + dist
        self._y2 = self._y1 - dist

    def set_x2y2_bottomright(self, dist):
        self._x2 = self._x1 + dist
        self._y2 = self._y1 + dist
