# Internal modules
try:
    from colors import ColorButton
    from shapes import ShapeButton
except ImportError:
    from gui.buttons.colors import ColorButton
    from gui.buttons.shapes import ShapeButton

create_ColorButton = ColorButton.create
create_ShapeButton = ShapeButton.create
