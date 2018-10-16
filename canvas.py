from Tkinter import Canvas

class PinceauCanvas:
    def __init__(self, master, width, height):
        self.__master = master
        self.__width = width
        self.__height = height
        self.__tmp = {}
        self.__tmp_rendered = None
        self.__shapes = []

        self.__canvas = Canvas(self.__master, width=self.__width, height=self.__height)
        self.bind_events()

    def pack(self):
        self.__canvas.pack()

    def bind_events(self):
        self.__canvas.bind('<Button-1>', self.mouse_click)
        self.__canvas.bind('<B1-Motion>', self.mouse_drag)
        self.__canvas.bind('<ButtonRelease-1>', self.mouse_release)

    def mouse_click(self, event):
        self.__canvas.focus_set()
        self.__tmp = { 'x0': event.x, 'y0': event.y }

    def mouse_drag(self, event):
        self.__tmp_rendered = self.create_rectangle_from_mouse(event, 'cyan')

    def mouse_release(self, event):
        final_shape = self.create_rectangle_from_mouse(event, 'blue')
        self.__shapes.append(final_shape)
        # Reset temp shape
        self.__tmp = {}
        self.__tmp_rendered = None

    def create_rectangle_from_mouse(self, event, color):
        self.__canvas.focus_set()
        x0 = self.__tmp['x0']
        y0 = self.__tmp['y0']
        x1 = event.x
        y1 = event.y
        self.__canvas.delete(self.__tmp_rendered)
        return self.__canvas.create_rectangle(x0, y0, x1, y1, fill=color)
