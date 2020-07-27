'''
    CoffeeMachine class has all function a machine operator and user should use to add, set ingredient
    And to make a beverage.

    Make beverage checks all cases of available resources and return appropriate comments if not.
    it runs a thread for corresponding outlet and after completion show prepared beverage.

    When a request is made first a empty outlet is searched, it is assigned.
    if all resources are met, make bevrage req is made by assigning a outlet an a thread.

    if not, no make beverage function (with delay) is called.

    The thread is freed after completion of make_beverage function by a boolean variable made false.

'''
import beverage
import threading


class CoffeeMachine:
    def __init__(self):
        self.outlets = 3
        self.ingredients = {}
        self.beverages = {}
        self.debug = False
        self.outletInUse = []

    def set_debug_mode(self, flag):
        self.debug = flag

    def set_outlets(self, n):
        self.outlets = n
        for i in range(n):
            self.outletInUse.append(False)

    def add_ingredients(self, ingredients):
        self.ingredients = ingredients

    # add new ingredient
    def add_new_ingredient(self, name, quantity=0):
        self.ingredients[name] = quantity

    # refill a ingredient
    def refill_ingredient(self, ingredient_name, quantity):
        if ingredient_name in self.ingredients:
            self.ingredients[ingredient_name] = self.ingredients[ingredient_name] + quantity
        else:
            print("Add ingredient first in possible ingredient")

    # add new beverage
    def add_new_beverage(self, name, ingredients):
        if name in self.beverages:
            print("Beverage already cab be in vending machine")
        else:
            self.beverages[name] = beverage.Beverage(name, ingredients)

    def add_beverages(self, beverages):
        for key, val in beverages.items():

            self.beverages[key] = beverage.Beverage(key, val)

    def __check_quantity(self, beverage_name):
        _beverage = self.beverages[beverage_name]
        for items in _beverage.ingredients:
            if items[0] not in self.ingredients or items[1] > self.ingredients[items[0]]:
                return False
        return True

    def __check_free_outlet(self):
        for i in range(len(self.outletInUse)):
            if not self.outletInUse[i]:
                return i
        return -1

    def __find_missing(self, beverage_name):
        _beverage = self.beverages[beverage_name]
        less_quantity = []
        missing = []
        for items in _beverage.ingredients:
            if items[0] not in self.ingredients:
                missing.append(items[0])
            elif items[1] > self.ingredients[items[0]]:
                less_quantity.append(items[0])
        return missing, less_quantity

    def __take_ingredient(self, beverage_name):
        _beverage = self.beverages[beverage_name]
        for items in _beverage.ingredients:
            self.ingredients[items[0]] = self.ingredients[items[0]] - items[1]

    def __assign_outlet(self, index, beverage_name):
        self.outletInUse[index] = True
        thread = threading.Thread(target=self.__make_beverage, args=(beverage_name, index))
        thread.start()

    def make_beverage(self, beverage_name):
        if self.debug:
            print("request for {} made".format(beverage_name))

        if beverage_name in self.beverages:
            if self.__check_quantity(beverage_name):
                self.__take_ingredient(beverage_name)
                index_outlet = self.__check_free_outlet()
                if index_outlet >= 0:
                    print("{} outlet assigned to {}".format(index_outlet, beverage_name))
                    self.outletInUse[index_outlet] = True
                    self.__assign_outlet(index_outlet, beverage_name)
                else:
                    print("All outlet busy")
            else:
                missing, less_quantity = self.__find_missing(beverage_name)
                print("{} cannot be made as ".format(beverage_name), end = '')
                if len(missing) > 0:
                    print("{}  missing, ".format(missing), end='')
                if len(less_quantity) > 0:
                    print("{}  not sufficient.".format(less_quantity))

        else:
            print("I can't make it!, add beverage and its ingredients first!")

    def __make_beverage(self, beverage_name, index):
        self.beverages[beverage_name].make_beverage()
        self.outletInUse[index] = False
        if self.debug:
            print("{} outlet freed from {}".format(index, beverage_name))
