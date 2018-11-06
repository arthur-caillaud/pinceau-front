# Internal modules
try :
    from straight_shape import StraightShape
    from oval import Oval
except ImportError:
    from gui.shapes.straight_shape import StraightShape
    from gui.shapes.oval import Oval

# A circle is a straight oval. Then it herits from
# the Oval class and StraightShape class.
class Circle(Oval, StraightShape):
    def __init__(self, shape):
        Oval.__init__(self, shape)
        StraightShape.__init__(self, shape)
