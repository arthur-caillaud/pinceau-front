class Square():
    def __init__(self, shape):
        self.__x1 = shape['x1']
        self.__y1 = shape['y1']
        x1x2_abs = abs(shape['x2'] - shape['x1'])
        y1y2_abs = abs(shape['y2'] - shape['y1'])
        x1x2 = shape['x2'] - shape['x1']
        y1y2 = shape['y2'] - shape['y1']
        if x1x2_abs < y1y2_abs :
            self.__x2 = self.__x1 + x1x2
            self.__y2 = self.__y1 + x1x2
        else :
            self.__x2 = self.__x1 + y1y2
            self.__y2 = self.__y1 + y1y2
        self.__fill = shape['fill']

    def draw_on(self, canvas):
        return canvas.create_rectangle(self.__x1, self.__y1, self.__x2, self.__y2, fill=self.__fill)
