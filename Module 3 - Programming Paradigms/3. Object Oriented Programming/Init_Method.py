class Recipe():
    def __init__(self, dish, items):
        self.dish = dish
        self.items = items

    def contents(self):
        print("The " + str(self.dish) + " contains: " + str(self.items))

Pizza = Recipe("Pizza", ["Dough", "Cheese", "Tomato Sauce", "Pepperoni"])

print(Pizza.items)

print(Pizza.contents())