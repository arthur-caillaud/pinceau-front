# Internal modules
try :
    from straight_shape import StraightShape
    from line import Line
except ImportError:
    from gui.shapes.straight_shape import StraightShape
    from gui.shapes.line import Line

class Diagonal(Line, StraightShape):
    def __init__(self, shape):
        Line.__init__(self, shape)
        StraightShape.__init__(self, shape)
