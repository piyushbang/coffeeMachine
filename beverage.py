'''
    Beverage class is object refering to a beverage, its ingredients, have
    functions to set ingredients and run a make beverage function.

    Default delay of 2 sec is set
'''
import time


class Beverage:
    def __init__(self, name, ingredients):
        self.name = ""
        self.ingredients = []
        self.makingTime = 2  # assuming all take 1 sec as mentioned in problem statement
        self.set_name(name)
        self.set_ingredients(ingredients)
        self.running = False

    def set_name(self, name):
        self.name = name

    def set_ingredients(self, ingredients):
        for key, val in ingredients.items():
            self.ingredients.append((key, val))

    def make_beverage(self):
        time.sleep(self.makingTime)
        print("{} is prepared ".format(self.name))
        



