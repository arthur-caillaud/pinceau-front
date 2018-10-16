from Tkinter import Tk
from canvas import PinceauCanvas

class GUI:
    def __init__(self):
        self.root = Tk()
        self.root.title("Pinceau.io")

        self.canvas = PinceauCanvas(self.root, 1000, 1000)
        self.canvas.pack()

    def run(self):
        self.root.mainloop()