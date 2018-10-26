# External modules
try:
    from Tkinter import Canvas
except:
    from tkinter import Canvas
# Internal modules
from shapes import Oval, Rectangle, Line, Circle, Square, Diagonal, Sticker

class PinceauCanvas:

    def __init__(self, master, width, height):
        self.__master = master
        self.__width = width
        self.__height = height
        self.__tmp = {}
        self.__tmp_rendered = None
        self.__shapes = []
        self.__emission_socket = None
        # Default constants
        self.__shape_mode = 'normal'
        self.__shape_type = 'rectangle'
        self.__tmp_color = '#E57373'
        self.__final_color = '#F44336'

        self.__canvas = Canvas(self.__master, width=self.__width, height=self.__height)
        self.__canvas.grid(row=2, column=0)
        self.bind_events()

    def set_emission_socket(self, emission_socket):
        self.__emission_socket = emission_socket

    def switch_shape_mode(self):
        self.__shape_mode = ('straight' if self.__shape_mode == 'normal' else 'normal')

    def change_color(self, tmp_color, color):
        self.__tmp_color = tmp_color
        self.__final_color = color

    def change_shape(self, shape_type):
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
        keycode = event.keycode
        if keycode == 131330 or keycode == 131074 or keycode == 131076: # Maj key is pressed
            self.switch_shape_mode()

    def mouse_click(self, event):
        self.__canvas.focus_set()
        self.__tmp = {
            'action': 'add',
            'x1': event.x,
            'y1': event.y,
            'x2': event.x,
            'y2': event.y,
            'mode': self.__shape_mode,
            'type': self.__shape_type,
            'fill': self.__tmp_color
        }

    def mouse_drag(self, event):
        self.__canvas.focus_set()
        self.__tmp['x2'] = event.x
        self.__tmp['y2'] = event.y
        self.__tmp['mode'] = self.__shape_mode
        self.__tmp_rendered = self.draw(self.__tmp)

    def mouse_release(self, event):
        self.__tmp['fill'] = self.__final_color
        if self.__tmp['type'] is not None:
            final_shape = self.draw(self.__tmp)
            self.__shapes.append(final_shape)
            self.__emission_socket.send(self.__tmp)
        # Reset temp shape
        self.__tmp = {}
        self.__tmp_rendered = None

    def draw(self, shape):
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
        elif shape['type'] == 'sticker':
            rendered_shape = Sticker(shape)
        return rendered_shape.draw_on(self.__canvas)
