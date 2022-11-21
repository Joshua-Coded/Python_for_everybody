import tkinter as TK

class Polygon:
    def __init__(self, sides, name, size=100, color="red", line_thicken="80"):
        self.sides = sides
        self.name = name
        self.size = size
        self.line_thicken = line_thicken
        self.interior_angle = (self.sides-2) * 180
        self.angle = self.interior_angle/self.sides


    def draw(self):
        for i in range(self.sides):
            TK.pensize(self.line_thicken)
            TK.color(self.color)
            TK.forward(100)
            TK.right(180-self.angle)
        TK.done()

sqaure = Polygon("Sqaure", 4)
triangle = Polygon("Triangle", 3)
pentagon = Polygon("Pentagon", 8)
hexagon = Polygon("Hexagon", 6)


hexagon.draw()