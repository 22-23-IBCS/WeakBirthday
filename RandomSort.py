import random

def main():

    L = [1, 4, 3, 2]

    while True:
        #sort with Random sort
        F = []
        U = []
        maxPos = len(L) - 1
        for i in range(len(L)):
            randomPos = random.randint(0, maxPos)
            F.append(L[randomPos])
            U.append(randomPos)
            print(F)


        isSorted = True
        for i in range(len(L) - 1):
            if F[i] > F[i+1]:
                isSorted = False

        if isSorted:
            break
        

if __name__ == "__main__":
    main()
