import turtle

class Artist:

    def __init__(self, t):
        self.t = t
    
    def triangle(self, size):
        for i in range(3):
            self.t.right(120)
            self.t.forward(size)

    def star(self, size):
        for i in range(4):
            self.t.right(140)
            self.t.forward(size)
        self.t.right(150)
        self.t.forward(size)


    def circle(self, size):
        for i in range(360):
            self.t.right(1)
            self.t.forward(size)

    def square(self, size):
        for i in range(4):
            self.t.forward(size)
            self.t.right(90)

    def polygon(self, sides, size = 20):
        for i in range(sides):
            self.t.forward(20)
            self.t.right(360/int(sides))

    def hexagon(self, size = 20):
        for i in range(6):
            self.t.forward(size)
            self.t.right(60)

    def octagon(self, size = 20):
        for i in range(6):
            self.t.forward(100)
            self.t.right(45) 

    def move(self, x, y):
        self.t.penup()
        self.t.goto(x, y)
        self.t.pendown()

def main():

    canvas = turtle.Screen()
    canvas.bgcolor("red")
    canvas.title("Artist")
    t = turtle.Turtle()
    t.shape("turtle")
    t.speed(5)
    art = Artist(t)
    x = int(input("Pick how many sides this shape should be: "))
    art.polygon(x)
    art.move(140, 0)
    y = int(input("How large should this shape be? "))
    art.triangle(y)
    art.move(150,200)
    z = int(input("How large should this shape be? "))
    art.star(z)
    art.move(-150, 200)
    a = int(input("How large should this shape be? "))
    art.circle(a)
    art.move(0, -200)
    b = int(input("How large should this shape be? "))
    art.square(b)
    
    


if __name__ == "__main__":
    main()
