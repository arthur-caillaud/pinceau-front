from Tkinter import Frame, BOTTOM
from buttons import *

class PinceauMenu:
    def __init__(self, master, change_color, change_shape):
        self.__master = master
        self.__color_buttons_frame = Frame(self.__master)
        self.__shape_buttons_frame = Frame(self.__master)
        self.__change_color = change_color
        self.__change_shape = change_shape
        self.__buttons = [
            RedButton(self.__color_buttons_frame, self.__change_color),
            GreenButton(self.__color_buttons_frame, self.__change_color),
            BlueButton(self.__color_buttons_frame, self.__change_color),
            OrangeButton(self.__color_buttons_frame, self.__change_color),
            YellowButton(self.__color_buttons_frame, self.__change_color),
            PurpleButton(self.__color_buttons_frame, self.__change_color),
            PinkButton(self.__color_buttons_frame, self.__change_color),
            RectangleButton(self.__shape_buttons_frame, self.__change_shape),
            OvalButton(self.__shape_buttons_frame, self.__change_shape),
            LineButton(self.__shape_buttons_frame, self.__change_shape),
        ]

    def pack(self):
        self.__color_buttons_frame.pack(side = BOTTOM)
        self.__shape_buttons_frame.pack(side = BOTTOM)
        for button in self.__buttons:
            button.pack()
