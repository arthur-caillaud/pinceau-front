# External modules
from Tkinter import Canvas
# Internal modules
from rectangle import Rectangle
from oval import Oval

class PinceauCanvas:
    SHAPE_TYPE = 'oval'
    TMP_COLOR = 'magenta'
    FINAL_COLOR = 'red'

    def __init__(self, master, width, height):
        self.__master = master
        self.__width = width
        self.__height = height
        self.__tmp = {}
        self.__tmp_rendered = None
        self.__shapes = []
        self.__emission_socket = None

        self.__canvas = Canvas(self.__master, width=self.__width, height=self.__height)
        self.bind_events()

    def set_emission_socket(self, emission_socket):
        self.__emission_socket = emission_socket

    def pack(self):
        self.__canvas.pack()

    def bind_events(self):
        self.__canvas.bind('<Button-1>', self.mouse_click)
        self.__canvas.bind('<B1-Motion>', self.mouse_drag)
        self.__canvas.bind('<ButtonRelease-1>', self.mouse_release)

    def mouse_click(self, event):
        self.__canvas.focus_set()
        self.__tmp = { 'x1': event.x, 'y1': event.y, 'action': 'add' }

    def mouse_drag(self, event):
        self.__canvas.focus_set()
        self.__tmp['x2'] = event.x
        self.__tmp['y2'] = event.y
        self.__tmp['type'] = PinceauCanvas.SHAPE_TYPE
        self.__tmp['fill'] = PinceauCanvas.TMP_COLOR
        self.__tmp_rendered = self.draw(self.__tmp)

    def mouse_release(self, event):
        self.__tmp['fill'] = PinceauCanvas.FINAL_COLOR
        final_shape = self.draw(self.__tmp)
        self.__shapes.append(final_shape)
        self.__emission_socket.send(self.__tmp)
        # Reset temp shape
        self.__tmp = {}
        self.__tmp_rendered = None

    def draw(self, shape):
        self.__canvas.delete(self.__tmp_rendered)
        rendered_shape = None
        if shape['type'] == 'rectangle':
            rendered_shape = Rectangle(shape)
        elif shape['type'] == 'oval':
            rendered_shape = Oval(shape)
        return rendered_shape.draw_on(self.__canvas)
