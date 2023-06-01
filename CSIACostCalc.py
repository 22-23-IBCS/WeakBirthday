from graphics import *


def CostCalc():
    win = GraphWin("CostCalc", 1000, 800)
    win.setBackground("white")

    budget = 10000
    B = Text(Point(500, 650), "Budget: $10000")
    B.setSize(20)
    B.draw(win)

    C = {
        'Nosecone': 18.2,
        'Egg Protector': 9.41,
        'BT-70 Bodytube': 14.42,
        'BT-80 Bodytube': 14.42,
        'Motor Retainer': 10.1,
        'Motormount Tube': 10.06,
        'Balsa Sheet': 4.17,
        'Basswood sheet': 4.03,
        'Altimeter Bay': 3.89,
        'Transition Part': 12.53,
        'Carbon Fiber Rods': 15.89
    }

    x = 50
    y = 50
    entries = []
    for word, value in C.items():
        text = Text(Point(100, y), f"{word}: ${value}")
        text.setSize(16)
        text.draw(win)
        E = Entry(Point(250, x), 10)
        E.draw(win)
        entries.append(E)
        x = x + 50
        y = y + 50

    total = 0
    p = 0
    totalT = Text(Point(500, 700), f"Total Cost: ${total:.2f}")
    totalT.setSize(20)
    totalT.draw(win)
    percent = Text(Point(500, 750), f"Percentage of Budget Used: {p:.2f}")
    percent.setSize(20)
    percent.draw(win)

    while True:
        partCost = 0
        percentage = 0
        for entry, value in zip(entries, C.values()):
            num = entry.getText()
            if num:
                num = float(num)
                partCost = partCost + num * value
                percentage = percentage + (partCost/budget) * 100
                
        totalT.setText(f"Total Cost: ${partCost:.2f}")
        percent.setText(f"Percentage of Budget Used: {percentage:.2f}%")


def main():
    CostCalc()


if __name__ == "__main__":
    main()
