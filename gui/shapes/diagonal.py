# Internal modules
try :
    from straight_shape import StraightShape
    from line import Line
except ImportError:
    from gui.shapes.straight_shape import StraightShape
    from gui.shapes.line import Line

# A diagonal is a "straight line". Then it herits from
# the Line class and StraightShape class.
class Diagonal(Line, StraightShape):
    def __init__(self, shape):
        Line.__init__(self, shape)
        StraightShape.__init__(self, shape)
