from Tkinter import Canvas

class PinceauCanvas:
    def __init__(self, master, emissionSocket, width, height):
        self.__master = master
        self.__width = width
        self.__height = height
        self.__tmp = {}
        self.__tmp_rendered = None
        self.__shapes = []
        self.__emissionSocket = emissionSocket

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
        self.__tmp = { 'x1': event.x, 'y1': event.y }

    def mouse_drag(self, event):
        self.__canvas.focus_set()
        self.__tmp['x2'] = event.x
        self.__tmp['y2'] = event.y
        self.__tmp['fill'] = 'cyan'
        self.__tmp_rendered = self.create_rectangle(self.__tmp)

    def mouse_release(self, event):
        self.__tmp['fill'] = 'blue'
        self.__tmp['action'] = 'add'
        final_shape = self.create_rectangle(self.__tmp)
        self.__shapes.append(final_shape)
        self.__emissionSocket.send(self.__tmp)
        # Reset temp shape
        self.__tmp = {}
        self.__tmp_rendered = None

    def create_rectangle(self, shape):
        x1 = shape['x1']
        x2 = shape['x2']
        y1 = shape['y1']
        y2 = shape['y2']
        fill = shape['fill']
        self.__canvas.delete(self.__tmp_rendered)
        return self.__canvas.create_rectangle(x1, y1, x2, y2, fill=fill)
