# IBCS Python Coding Quiz
# Name: Felix Y.

# Read the questions below carefully. Each question describes a
# method that you will need to define with code. In order to demonstrate
# that your method works and test your code, you will need to 'un-comment'
# the method call in the main() method
from random import *

# 1. Given a list of integers, the method returns True if there are
# at least two numbers in the list that are the maximum values out of
# everything else in the list. If there is only one maximum, the method
# should return false.
def twoMax(L):
    maximum = L[0]
    for i in range(len(L)):
        if L[i] >= maximum:
            maximum = L[i]
    for i in range(len(L)):
        if maximum - L[i] == 0:
            return True
        else:
            return False            
     
        


# 2. Given a random integer between 1-15 (inclusive), the method asks
# the user to input an integer between 1-15. If the user's number is
# greater than the random number, the method should print "lower". If
# the user was less than the random number, the method should print "higher".
# If the user got it right, the method should print "You got it!" and stop.
# The user gets to guess 3 times before the method stops otherwise.
def threeGuessGame():
    x = randint(1, 15)
    y = int(input("Please enter a number between 1 and 15."))
    z = 2
    while True:
        if x < y:
            print("Lower")
            z = z - 1
            y = int(input("Please enter a number between 1 and 15."))
        if x > y:
            print("Higher")
            z = z - 1
            y = int(input("Please enter a number between 1 and 15."))
        if x == y:
            print("You got it!")
            break
        if z <= 0:
            print("You failed.")
            break


def main():
    L = [1, 2, 4, 8, 9, 5, 7, 2, 9, 3]
    e = [1, 8, 5, 8, 4, 7, 2, 9, 3]
    q = [1, 1, 1, 1]
    print(twoMax(L))
    print(twoMax(e))
    print(twoMax(q))

    threeGuessGame()


if __name__ == "__main__":
    main()
