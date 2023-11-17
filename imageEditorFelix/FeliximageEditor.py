from graphics import*
from Button import*
import statistics
import random

# methods for each filter. You need to complete each method by editing
# the image 'cats' and changing the r, g, b values.
def brighten(cats):
    for i in range(500):
        for j in range(451):
            pix = cats.getPixel(i, j)
            r,g,b = pix[0], pix[1], pix[2]
            r = min(255, r+50)
            g = min(255, g+50)
            b = min(255, b+50)
            cats.setPixel(i, j, color_rgb(r,g,b))

def darken(cats):
    r = 120
    g = 120
    b = 120
    for i in range(500):
        for j in range(451):
            pix = cats.getPixel(i, j)
            r, g, b = pix[0], pix[1], pix[2]
            r = max(0, r-30)
            b = max(0, b-20)
            g = max(0, g-20)
            cats.setPixel(i, j, color_rgb(r,g,b))

def blurr(cats):
    for i in range(1, 499):
        for j in range(1, 450):
            pix1 = cats.getPixel(i, j)
            pix2 = cats.getPixel(i + 1, j)
            pix3 = cats.getPixel(i - 1, j)
            pix4 = cats.getPixel(i, j + 1)
            pix5 = cats.getPixel(i, j - 1)

            r = round((pix1[0] + pix2[0] + pix3[0] + pix4[0] + pix5[0])/ 5)
            g = round((pix1[1] + pix2[1] + pix3[1] + pix4[1] + pix5[1])/ 5)
            b = round((pix1[2] + pix2[2] + pix3[2] + pix4[2] + pix5[2])/ 5)
            cats.setPixel(i, j, color_rgb(r, g, b))
            
def onlyColor(cats):
    for i in range(500):
        for j in range(451):
            pix = cats.getPixel(i, j)
            r, g, b = pix[0], pix[1], pix[2]
            l = [r,g,b]
            if r > 160 and g < 100 and b < 100:
                r, g, b = pix[0], pix[1], pix[2]
            else:
                r = int(statistics.mean(l))
                g = int(statistics.mean(l))
                b = int(statistics.mean(l))
            cats.setPixel(i, j, color_rgb(r,g,b))
            
def saturate(cats):
    for i in range(500):
        for j in range(451):
            pix = cats.getPixel(i, j)
            r, g, b = pix[0], pix[1], pix[2]
            m = max(r, b, g)
            if r == m:
                r=r*1.2
            elif b == m:
                b=b*1.2
            elif g == m:
                g=g*1.2
            r = min(255, round(r))
            g = min(255, round(g))
            b = min(255, round(b))
            cats.setPixel(i, j, color_rgb(r, g, b))
            
def specialFilter(cats):
    for i in range(500):
        for j in range(451):
            s = []
            pix = cats.getPixel(i, j)
            r = pix[0]
            g = pix[1]
            b = pix[2]
            cats.setPixel(i, j, color_rgb(g,r,b))

            
def main():

    win = GraphWin("Image Editor", 800, 600)
    close = Button(win, "grey", "Quit", Point(80, 560), 45)
    bright = Button(win, "white", "Brighten", Point(720, 50), 45)
    dark = Button(win, "white", "Darken", Point(720, 150), 45)
    blur = Button(win, "white", "Blur", Point(720, 250), 45)
    sat = Button(win, "white", "Saturate", Point(720, 350), 45)
    spec = Button(win, "white", "Inverse", Point(720, 450), 45)
    only = Button(win, "white", "only Color", Point(720, 550), 45)
    res = Button(win, "white", "RESET", Point(80, 300), 45)

    cats = Image(Point(400,300), "cats.png")
    cats.draw(win)

    m = win.getMouse()
    while True:
        if close.isClicked(m):
            break
        if res.isClicked(m):
            cats.undraw()
            cats = Image(Point(400,300), "cats.png")
            cats.draw(win)
        if dark.isClicked(m):
            darken(cats)
        if bright.isClicked(m):
            brighten(cats)
        if blur.isClicked(m):
            blurr(cats)
        if sat.isClicked(m):
            saturate(cats)
        if spec.isClicked(m):
            specialFilter(cats)
        if only.isClicked(m):
            onlyColor(cats)
        m = win.getMouse()

    win.close()
    
if __name__ == "__main__":
    main()
