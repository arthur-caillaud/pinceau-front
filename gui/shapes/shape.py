class Shape:
    def __init__(self, shape):
        self._x1 = shape['x1']
        self._x2 = shape['x2']
        self._y1 = shape['y1']
        self._y2 = shape['y2']
        self._fill = shape['fill']

    def draw_on(self, canvas):
        return self
