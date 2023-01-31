from graphics import *
from Button import *


def Ball():
    win  = GraphWin("Ball", 550, 550)
    x = 275
    y = 100
    ball = Circle(Point(x, y), 15)
    ball.draw(win)
    win.setBackground("White")
    while True:
        ball.undraw()
        y = y**1.001
        ball = Circle(Point(x, y), 15)
        ball.draw(win)
        time.sleep(0.01)
        if y >= 530:
            ball.undraw()
            y = y**0.9
            ball = Circle(Point(x, y), 15)
            ball.draw(win)
            time.sleep(0.01)
            if y <= 100:
                break


def main():
    Ball()


if __name__ == "__main__":
    main()
