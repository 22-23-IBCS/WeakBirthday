from graphics import *
from Button import *

def main():
    
    win = GraphWin("Character Creation", 800, 600)

    B1 = Button(win, Point(650, 40), Point(750, 110), "honeydew2", "Face")

    B2 = Button(win, Point(650, 100), Point(750, 150), "pink", "Big Eyes")
    B3 = Button(win, Point(650, 150), Point(750, 200), "ivory", "Small Eyes")
    B4 = Button(win, Point(650, 200), Point(750, 250), "rosybrown", "Smile")
    B5 = Button(win, Point(650, 250), Point(750, 300), "oldlace", "Frown")
    B6 = Button(win, Point(650, 300), Point(750, 350), "bisque", "Round Ears")
    B7 = Button(win, Point(650, 350), Point(750, 400), "honeydew", "Block Ears")
    Face = Oval(Point(150, 50), Point(550, 550))
    
#eyes
    bigEye1 = Circle(Point(350, 250), 50)
    bigEye2 = Circle(Point(450, 250), 40)
    smallEye1 = Circle(Point(350, 250), 20)
    smallEye2 = Circle(Point(450, 250), 20)

#mouth
    smile = Circle(Point(350, 500), 100)
    smile2 = Circle(Point(350, 475), 100)
    frown = Circle(Point(350, 800), 100)
    frown2 = Circle(Point(350, 775), 100)

#ears
    roundEars1 = Oval(Point(150, 50), Point(550, 550))
    roundEars2 = Oval(Point(150, 50), Point(550, 550))
    blockEars1 = Rectangle(Point(150, 50), Point(550, 550))
    blockEars2 = Rectangle(Point(150, 50), Point(550, 550))
    
    Q = Quit(win, Point(650, 500), Point(750, 575), "salmon", "Quit")

    m = win.getMouse()
    while True:
        if B1.isClicked(m):
            Face.undraw()
            Face.draw(win)

        if B2.isClicked(m):
            bigEye1.undraw()
            bigEye2.undraw()
            bigEye1.draw(win)
            bigEye2.draw(win)

        if B3.isClicked(m):
            smallEye1.undraw()
            smallEye2.undraw()
            smallEye1.draw(win)
            smallEye2.draw(win)

        if B4.isClicked(m):
            smile.undraw()
            smile2.undraw()
            smile.draw(win)
            smile2.draw(win)

        if B5.isClicked(m):
            frown.undraw()
            frown2.undraw()
            frown.draw(win)
            frown2.draw(win)

        if B6.isClicked(m):
            roundEars1.undraw()
            roundEars2.undraw()
            roundEars1.draw(win)
            roundEars2.draw(win)

        if B7.isClicked(m):
            blockEars1.undraw()
            blockEars2.undraw()
            blockEars1.draw(win)
            blockEars2.draw(win)

        if Q.isClicked(m):
            break
        m = win.getMouse()

    win.close()

    
if __name__ == "__main__":
    main()
