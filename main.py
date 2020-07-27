import coffeeMachine
import json
import time
# initial setting beverage+ingredient is taken from json file
with open('input.json') as json_file:
    data = json.load(json_file)


vendingMachine = coffeeMachine.CoffeeMachine()
vendingMachine.set_outlets(data["machine"]["outlets"]["count_n"])
vendingMachine.add_ingredients(data["machine"]["total_items_quantity"])
vendingMachine.add_beverages(data["machine"]["beverages"])

# vendingMachine.set_debug_mode(True)  # uncomment to see request comment and process comments


# Test cases :
vendingMachine.make_beverage("hot_tea")  # make tea, possible so after 2 sec, prepared
vendingMachine.make_beverage("hot_coffee")  # possible so after 2 sec, prepared
vendingMachine.make_beverage("black_tea")  # comment of missing ingredient instantly displayed
vendingMachine.make_beverage("green_tea")  # comment of missngi ingredient instantly displayed
vendingMachine.make_beverage("hot_coffee")  # comment of missng ingredient instantly displayed

vendingMachine.add_new_ingredient("green_mixture", 100) # adding new ingredient for green tea
vendingMachine.refill_ingredient("sugar_syrup", 100) # adding missing for green tea


print("Waiting 2 seconds for previous order to complete")
time.sleep(2)

vendingMachine.make_beverage("green_tea") # now green tea can be made.
vendingMachine.make_beverage("green_tea") # will not process as green tea thread already in use.

print("Waiting 3 seconds for previous order to complete")
time.sleep(3)

vendingMachine.make_beverage("green_tea") # now green tea can be made as prev green tea is made.
