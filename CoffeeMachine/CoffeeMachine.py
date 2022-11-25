class CoffeeMachine:

    # types of coffee available
    coffee = {"1": {"name": "espresso", "ingredients": {"water": 250, "milk": 0, "coffee beans": 16, "price": 4}},
              "2": {"name": "latte", "ingredients": {"water": 350, "milk": 75, "coffee beans": 20, "price": 7}},
              "3": {"name": "cappuccino", "ingredients": {"water": 200, "milk": 100, "coffee beans": 12, "price": 6}}}

    def __init__(self, water=0, milk=0, beans=0, cups=0, money=0):
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cups = cups
        self.money = money

    def __str__(self):
        return f"The coffee machine has:\n" \
               f"{self.water} ml of water\n" \
               f"{self.milk} ml of milk\n" \
               f"{self.beans} g of coffee beans\n" \
               f"{self.cups} disposable cups\n" \
               f"{self.money} of money"

    # checks if enough ingredients and removes them from stock
    def buy(self):
        print(f"\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        option = input()
        if option == "back":
            return
        required_ingredient = ""

        if self.water < self.coffee[option]["ingredients"]["water"]:
            required_ingredient = "water"
        elif self.milk < self.coffee[option]["ingredients"]["milk"]:
            required_ingredient = "milk"
        elif self.beans < self.coffee[option]["ingredients"]["beans"]:
            required_ingredient = "beans"
        elif self.cups < self.coffee[option]["ingredients"]["cups"]:
            required_ingredient = "cups"

        if required_ingredient != "":
            print(f"Sorry, not enough {required_ingredient}!")
        else:
            self.water -= self.coffee[option]["ingredients"]["water"]
            self.milk  -= self.coffee[option]["ingredients"]["milk"]
            self.beans -= self.coffee[option]["ingredients"]["coffee beans"]
            self.cups  -= 1
            self.money += self.coffee[option]["ingredients"]["price"]
            print("I have enough resources, making you a coffee!\n")

    # adds entered ingredients to stock
    def fill(self):
        print("\nWrite how many ml of water you want to add:")
        self.water += int(input())
        print("Write how many ml of milk you want to add:")
        self.milk += int(input())
        print("Write how many grams of coffee beans you want to add:")
        self.beans += int(input())
        print("Write how many disposable cups you want to add:")
        self.cups += int(input())
        print()

    # withdraws all money from machine
    def take(self):
        print(f"\nI gave you ${self.money}\n")
        self.money = 0

    # menu of options
    @staticmethod
    def start():
        while True:
            action = input("Write action (buy, fill, take, remaining, exit):\n")
            if action == "buy":
                machine.buy()
            elif action == "fill":
                machine.fill()
            elif action == "take":
                machine.take()
            elif action == "remaining":
                print(machine)
            elif action == "exit":
                break


if __name__ == '__main__':
    machine = CoffeeMachine(400, 540, 120, 9, 550)
    machine.start()
