from straight_shape import StraightShape
from oval import Oval

class Circle(Oval, StraightShape):
    def __init__(self, shape):
        Oval.__init__(self, shape)
        StraightShape.__init__(self, shape)
