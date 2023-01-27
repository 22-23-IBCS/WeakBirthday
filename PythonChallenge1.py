from graphics import *
from Button import *


def main():
    win = GraphWin("Python Challenge Problems", 800, 600)

    n1text = Text(Point(80, 100), "Enter a noun")
    n2text = Text(Point(80, 200), "Enter a noun")
    Vtext = Text(Point(80, 300), "Enter a verb")
    Atext = Text(Point(80, 400), "Enter a adjective")
    Extext = Text(Point(80, 500), "Enter a Excalmation")
    
    noun1 = Entry(Point(200, 100), 20)
    noun1.draw(win)
    
    noun2 = Entry(Point(200, 200), 20)
    noun2.draw(win)
    
    verb = Entry(Point(200, 300), 20)
    verb.draw(win)
    
    adjective = Entry(Point(200, 400), 20)
    adjective.draw(win)

    excalmation = Entry(Point(200, 500), 20)
    excalmation.draw(win)

    B = Button(win, Point(400, 500), Point(520, 580), "tomato", "Generate!")

    while True:

        m = win.getMouse()

        if B.isClicked(m):
            Noun1 = noun1.draw(win)
        



if __name__ == "__main__":
    main()
