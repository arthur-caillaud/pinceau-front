class Rectangle():
    def __init__(self, shape):
        self.__x1 = shape['x1']
        self.__x2 = shape['x2']
        self.__y1 = shape['y1']
        self.__y2 = shape['y2']
        self.__fill = shape['fill']

    def draw_on(self, canvas):
        return canvas.create_rectangle(self.__x1, self.__y1, self.__x2, self.__y2, fill=self.__fill)
