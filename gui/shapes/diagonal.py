from straight_shape import StraightShape
from line import Line

class Diagonal(Line, StraightShape):
    def __init__(self, shape):
        Line.__init__(self, shape)
        StraightShape.__init__(self, shape)
