'''
    Beverage class is object refering to a beverage, its ingredients, have
    functions to set ingredients and run a make function.
    Make_beverage run by starting a thread which is recreated at end of it
    to be used on next make instance
    Default delay of 2 sec is set
'''
import time
import threading


class Beverage:
    def __init__(self, name, ingredients):
        self.name = ""
        self.ingredients = []
        self.makingTime = 2  # assuming all take 1 sec as mentioned in problem statement
        self.set_name(name)
        self.set_ingredients(ingredients)
        self.running = False
        self.thread = threading.Thread(target=self.make_beverage, name=name)

    def set_name(self, name):
        self.name = name

    def set_ingredients(self, ingredients):
        for key, val in ingredients.items():
            self.ingredients.append((key, val))

    def make_beverage(self):
        self.running = True
        time.sleep(self.makingTime)
        print("{} is prepared ".format(self.name))
        # after thread is done,  create a new one for that beverage
        self.thread = threading.Thread(target=self.make_beverage, name=self.name)
        self.running = False


