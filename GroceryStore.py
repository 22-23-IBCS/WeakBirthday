class GroceryStore():

    def __init__(self, items):
        self.items = items

        
    def getManager(self, y):
        while x is True:
            print("I am Jerry. Your complaints are dumb. Goodbye.")
            break
            


def main():
    
    product = {"Health Potion" : 5,
            "Mana Potion" : 4,
            "Stamina Potion" : 3,
            "Meat Skewers" : 4,
            "Ale" : 3,
            "Tea" : 1}

    g = GroceryStore(product)

    print("Welcome to The Hidden Spade! Here are our items for selection.")
    print(list(product.keys())) 
    print("If you have complaints, speak to the manager, Jerry.")
    y = input("Press 1 if you would like to speak to the manager.\n")
    if y == 1:
        g.getManager(y)
    else:
        pass

    basket = []
    total = 0
    while True:
        res = input("What would you like to buy? Enter 'stop' if done\n")
        if res == "stop":
            break
        else:
            price = product.get(res)
            total = total + price
            basket.append(res)

    print(basket)
    print("That would be " + str(total) + " coins.")







    

if __name__ == "__main__":
    main()
