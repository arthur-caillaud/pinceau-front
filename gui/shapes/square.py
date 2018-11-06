# Internal modules
try:
    from straight_shape import StraightShape
    from rectangle import Rectangle
except ImportError:
    from gui.shapes.straight_shape import StraightShape
    from gui.shapes.rectangle import Rectangle

class Square(Rectangle, StraightShape):
    def __init__(self, shape):
        Rectangle.__init__(self, shape)
        StraightShape.__init__(self, shape)
