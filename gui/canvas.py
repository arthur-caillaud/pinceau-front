# External modules
try:
    from Tkinter import Canvas
except ImportError:
    from tkinter import Canvas
# Internal modules
try:
    from shapes import Oval, Rectangle, Line, Circle, Square, Diagonal
except ImportError:
    from gui.shapes import Oval, Rectangle, Line, Circle, Square, Diagonal

# This class contains the methods explaining how to draw a shape using the mouse
class PinceauCanvas:
    def __init__(self, master, width, height):
        self.__master = master
        self.__width = width
        self.__height = height
        self.__tmp = {}
        self.__tmp_rendered = None
        self.__shapes = []
        # Default constants
        self.__draw_mode = 'add'
        self.__shape_mode = 'normal'
        self.__shape_type = 'rectangle'
        self.__tmp_color = '#E57373'
        self.__final_color = '#F44336'
        # Main canvas
        self.__canvas = Canvas(self.__master, width=self.__width, height=self.__height)
        self.bind_events()

    def set_send(self, send_func):
        # Method sending the drawn shape to the server.
        self.__send = send_func

    def switch_shape_mode(self):
        # Method enabling to switch from a straight shape to a nomrmal shape
        # and vice-versa.
        self.__shape_mode = ('straight' if self.__shape_mode == 'normal' else 'normal')

    def switch_draw_mode(self):
        # Method enabling to switch from the drawing mode to the erasing mode
        # and vice-versa.
        self.__draw_mode = ('erase' if self.__draw_mode == 'add' else 'add')

    def change_color(self, tmp_color, color):
        # Method enabling to switch from one color to another.
        self.__tmp_color = tmp_color
        self.__final_color = color

    def change_shape(self, shape_type):
        # Method enabling to switch from one shape to another.
        self.__shape_type = shape_type

    def pack(self):
        self.__canvas.pack()

    def bind_events(self):
        self.__canvas.bind('<KeyPress>', self.key_press)
        self.__canvas.bind('<KeyRelease>', self.key_press)
        self.__canvas.bind('<Button-1>', self.mouse_click)
        self.__canvas.bind('<B1-Motion>', self.mouse_drag)
        self.__canvas.bind('<ButtonRelease-1>', self.mouse_release)

    def key_press(self, event):
        # Method to detect if the 'CTRL' key or 'MAJ' key is pressed using the
        # keycodes from iOS and Windows.
        # Indeed, if 'CTRL' is pressed, we turn to erasing mode.
        # And if 'MAJ" is pressed, we turn to straight shapes mode.
        keycode = event.keycode
        if keycode == 262145 or keycode == 262401 or keycode == 17: # Ctrl key is pressed
            self.switch_draw_mode()
        if keycode == 131330 or keycode == 131074 or keycode == 131076 or keycode == 16: # Maj key is pressed
            self.switch_shape_mode()

    def mouse_click(self, event):
        self.__canvas.focus_set()
        x, y = event.x, event.y
        if self.__draw_mode == 'erase':
            action = {'action': 'erase', 'x': x, 'y': y}
            self.erase(action)
            self.__send(action)
        elif self.__draw_mode == 'add':
            self.__tmp = {
                'action': 'add',
                'x1': x,
                'y1': y,
                'x2': x,
                'y2': y,
                'mode': self.__shape_mode,
                'type': self.__shape_type,
                'fill': self.__tmp_color
            }

    def erase(self, action):
        # Method erasing a shape on the canvas.
        x, y = action['x'], action['y']
        shape = self.__canvas.find_closest(x, y)
        if shape:
            self.__canvas.delete(shape)

    def mouse_drag(self, event):
        if self.__draw_mode == 'add':
            self.__canvas.focus_set()
            self.__tmp['x2'] = event.x
            self.__tmp['y2'] = event.y
            self.__tmp['mode'] = self.__shape_mode
            self.__tmp_rendered = self.draw(self.__tmp)

    def mouse_release(self, event):
        if self.__draw_mode == 'add':
            self.__tmp['fill'] = self.__final_color
            if self.__tmp['type'] is not None:
                final_shape = self.draw(self.__tmp)
                self.__shapes.append(final_shape)
                self.__send(self.__tmp)
            # Reset temp shape
            self.__tmp = {}
            self.__tmp_rendered = None

    def draw(self, shape):
        # Method drawing a shape on the canvas.
        self.__canvas.delete(self.__tmp_rendered)
        rendered_shape = None
        if shape['type'] == 'rectangle' and shape['mode'] == 'normal':
            rendered_shape = Rectangle(shape)
        elif shape['type'] == 'rectangle' and shape['mode'] == 'straight':
            rendered_shape = Square(shape)
        elif shape['type'] == 'oval' and shape['mode'] == 'normal':
            rendered_shape = Oval(shape)
        elif shape['type'] == 'oval' and shape['mode'] == 'straight':
            rendered_shape = Circle(shape)
        elif shape['type'] == 'line' and shape['mode'] == 'normal':
            rendered_shape = Line(shape)
        elif shape['type'] == 'line' and shape['mode'] == 'straight':
            rendered_shape = Diagonal(shape)
        shape_id = rendered_shape.draw_on(self.__canvas)
        return shape_id
