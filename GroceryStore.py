class GroceryStore():

    def __init__(self, items):
        self.items = items

        
    def getManager(self, y):
        if y == str(1):
            print("I am Jerry. Your complaints are dumb. Goodbye.")

        
def main():
    
    product = {"Health Potion" : 5,
            "Mana Potion" : 4,
            "Stamina Potion" : 3,
            "Meat Skewers" : 4,
            "Bread" : 2,
            "Grilled Fish" : 5,
            "Spellbook" : 20,
            "Spare Clothes" : 30,
            "Ale" : 3,
            "Tea" : 1}

    g = GroceryStore(product)

    print("Welcome to The Hidden Spade! Here are our items for selection.")
    print(list(product.keys())) 
    print("If you have complaints, speak to the manager, Jerry.")
    y = input("Press 1 if you would like to speak to the manager.\n")
    g.getManager(y)


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
