from turtle import Turtle

FONT = ("Ariel", 18, "normal")


class DrawStates(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()

    def write_location(self, state_name, x, y):
        self.goto(x, y)
        self.write(f"{state_name}", align="center", font=FONT)
