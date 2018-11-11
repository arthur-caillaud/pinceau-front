# Internal modules
try :
    from rectangle import Rectangle
    from oval import Oval
    from square import Square
    from circle import Circle
    from line import Line
    from diagonal import Diagonal
except ImportError:
    from gui.shapes.rectangle import Rectangle
    from gui.shapes.oval import Oval
    from gui.shapes.square import Square
    from gui.shapes.circle import Circle
    from gui.shapes.line import Line
    from gui.shapes.diagonal import Diagonal
