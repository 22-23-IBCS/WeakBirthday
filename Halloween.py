import random

class House():

    def __init__(self, generosity):
        self.generosity = generosity

    def getGenerosity(self):
        x = random.randint(1, 10)
        return x

def randPath(m, num):
    p = []
    while (len(p) < num):
        p = []
        x = random.randint(0,4)
        y = random.randint(0,4)
        p.append(m[x][y])
        pVal = m[x][y]

        for i in range(num - 1):
            neighbors = [[x+1, y],[x-1,y],[x,y + 1],[x,y - 1]]
            bad = []
            for n in neighbors:
                if n[0] > 4 or n[0] < 0:
                    bad.append(n)
                elif n[1] > 4 or n[1] < 0:
                    bad.append(n)
                if n in p:
                    bad.append(n)
            for b in bad:
                neighbors.remove(b)

            if len(neighbors) == 0:
                break

            randNeigh = random.choice(neighbors)
            p.append(randNeigh)
            x = randNeigh[0]
            y = randNeigh[1]
            pVal = pVal + m[x][y]

            
        return pVal, p


def greedyPath(m, num):
    bestHouses = []
    houses = []
    for i in range(len(bestHouses)):
        for j in range(5):
            houses.qppend([m[i][j], [i, j]])
    maxHval = 0
    maxHcoord = [0,0]

    for h in houses:
        if h[0] >= maxHval:
            maxHval = h[0]
            maxHcoord = h[1]
    bestHouses.append(houses.pop(maxHcoord))
        

        
    for i in range(num - 1):
        return pVal, p
    
def main():
    m = [[],[],[],[],[]]
    for l in m:
        for i in range(5):
            h = House(0)
            l.append(h.getGenerosity())

    for i in range(5):
        print(m[0][i], m[1][i], m[2][i], m[3][i], m[4][i])

    num = int(input("How many houses?\n"))

    #gen, p = greedyPath(m, num)

    pVal, p = randPath(m, num)

    total = 0
    for i in range(5):
        for j in range(5):
            total = total + m[i][j]

    average  = total/25

    pVal, p = randPath(m, num)
    while (average > pVal/num):
        pVal, p = randPath(m, num)

    print(p)
    print("the average value in the path is: " + str(pVal/num))
    print("the average value in the neighborhood is " + str(average))
        

    
if __name__ == "__main__":
    main()
