from random import *
import math

def CentralTendencies(x, y ,z):
    avg = (x+y+z)/3

    if x < y:
        if y < z:
            median = y
        else:
            if x < z:
                median = z
            else:
                median = x
    else:
        if x < z:
            median = x
        else:
            if y < z:
                median = z
            else:
                median = y
    return avg, median


def randPrime():
    x = randint(1, 100)
    if x % 2 == 0:
        return "True"
    elif x % 3 == 0:
        return "True"
    elif x % 5 == 0:
        return "True"
    else:
        return "False"

def ExtremaFinder():
    L = []
    for i in range(10):
        x = randint(1, 50)
        L.append(x)
    mini = L[0]
    for i in range(len(L)):
        if L[i] <= mini:
            mini = L[i]
    maxi = L[0]
    for i in range(len(L)):
        if L[i] >= maxi:
            maxi = L[i]
    ran = maxi - mini
    return maxi, mini, ran

def PolarCoordinate(p):
    x = p[0]
    y = p[1]
    h = math.sqrt(x*x + y*y)
    angle = math.asin(y/h)
    return [h, angle]

def ScrabbleScore(name):
    name = name.lower()
    score = 0
    for char in name:
        if char in ["a", "e", "i", "o", "u", "l", "n", "s", "t", "r"]:
            score = score + 1
        elif char in ["d", "g"]:
            score = score + 2
        elif char in ["b", "c", "m", "p"]:
            score = score + 3
        elif char in ["f", "h", "v", "w", "y"]:
            score = score + 4
        elif char in ["k"]:
            score = score + 5
        elif char in ["j", "x"]:
            score = score + 8
        elif char in ["q", "z"]:
            score = score + 10
            
    return score
    

def main():
    print(CentralTendencies(3, 5, 6))
    
    print(randPrime())

    print(ExtremaFinder())

    print(PolarCoordinate([0, 1]))

    name = input("Please enter a name: ")
    print(ScrabbleScore(name))

    
    
if __name__ == "__main__":
    main()
