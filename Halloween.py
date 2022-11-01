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
    coords = []
    for i in range(5):
        for j in range(5):
            houses.append(m[i][j])
            coords.append([i,j])

    for i in range(25):
        maxHval = 0
        maxHcoord = [0,0]
        for pos in range(len(houses)):
            if houses[pos] > maxHval:
                maxHval = houses[pos]
                maxHcoord = coords[pos]
        bestHouses.append(maxHcoord)
        houses.remove(maxHval)
        coords.remove(maxHcoord)

    for i in range(len(bestHouses)):
        p = []
        start = bestHouses[i]
        x = bestHouses[0][0]
        y = bestHouses[0][1]
        pVal = m[x][y]
        
            
        for i in range(num - 1):
            neighbors = [[x+1, y],[x-1, y],[x, y + 1],[x, y - 1]]
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
            
            toBreak = False
            for h in bestHouses:
                if toBreak:
                    break
                for n in neighbors:
                    if n == h:
                        nextHouse = n
                        toBreak = True
                        break
            p.append(nextHouse)
            x = nextHouse[0]
            y = nextHouse[1]
            pVal = pVal + m[x][y]


        return pVal, p
    return 0, [[0,0]]


def main():
    m = [[],[],[],[],[]]
    for l in m:
        for i in range(5):
            h = House(0)
            l.append(h.getGenerosity())

    for i in range(5):
        print(m[0][i], m[1][i], m[2][i], m[3][i], m[4][i])

    num = int(input("How many houses?\n"))

    pVal, p = greedyPath(m, num)

    #pVal, p = randPath(m, num)

    total = 0
    for i in range(5):
        for j in range(5):
            total = total + m[i][j]

    average  = total/25

    '''pVal, p = randPath(m, num)
    while (average > pVal/num):
        pVal, p = randPath(m, num)

    print(p)
    print("the average value in the path is: " + str(pVal/num))
    print("the average value in the neighborhood is " + str(average))'''
        

    
if __name__ == "__main__":
    main()
