from straight_shape import StraightShape
from rectangle import Rectangle

class Square(Rectangle, StraightShape):
    def __init__(self, shape):
        Rectangle.__init__(self, shape)
        StraightShape.__init__(self, shape)
