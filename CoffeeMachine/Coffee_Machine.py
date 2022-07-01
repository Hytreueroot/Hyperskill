class CoffeeMachine:
    def __init__(self, water = 400, milk = 540, coffee_beans = 120, money = 550, disposable_cups = 9):
        self.water = water
        self.milk = milk
        self.coffee_beans = coffee_beans
        self.money = money
        self.disposable_cups = disposable_cups
        
    def buy(self):
        type_of_coffee = input("\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n")
        if type_of_coffee != "back":
            if type_of_coffee == "1" and self.water >= 250 and self.coffee_beans >= 16 and self.disposable_cups >= 1:
                self.water -= 250
                self.coffee_beans -= 16
                self.money += 4
                self.disposable_cups -= 1
                print("I have enough resources, making you a coffee!\n")
                
            elif type_of_coffee == "2" and self.water >= 350 and self.milk >= 75 and self.coffee_beans >= 20 and self.disposable_cups >= 1:
                self.water -= 350
                self.milk -= 75
                self.coffee_beans -= 20
                self.money += 7
                self.disposable_cups -= 1
                print("I have enough resources, making you a coffee!\n")
                
            elif type_of_coffee == "3" and self.water >= 200 and self.milk >= 100 and self.coffee_beans >= 12 and self.disposable_cups >= 1:
                self.water -= 200 
                self.milk -= 100
                self.coffee_beans -= 12
                self.money += 6
                self.disposable_cups -= 1
                print("I have enough resources, making you a coffee!\n")
                
            else:
                print("Sorry, not enough resources\n")
         
        else:
            main()
    
    def fill(self):
        
        print("Write how many ml of water you want to add:")
        add_water = int(input())
        self.water += add_water
        
        print("Write how many ml of milk you want to add: ")
        add_milk = int(input())
        self.milk += add_milk
        
        print("Write how many grams of coffee beans you want to add:")
        add_coffee_beans = int(input())
        self.coffee_beans += add_coffee_beans
        
        print("Write how many disposable cups of coffee you want to add: ")
        add_disposable_cups = int(input())
        self.disposable_cups += add_disposable_cups
        
        

    def take(self):
        print(f"\nI gave you ${self.money}\n")
        self.money = 0

        
    def __str__(self):
        return f"The coffee machine has:\n{self.water} ml of water\n{self.milk} ml of milk\n{self.coffee_beans} g of coffee beans\n{self.disposable_cups} disposable cups\n$ {self.money} of money"


def main():
    while True:
        action = input("Write action (buy, fill, take, remaining, exit):\n")
        if action == "buy":
            x.buy()
        elif action == "fill":
            x.fill()
        elif action == "take":
            x.take()
        elif action == "remaining":
            print(x)
        elif action == "exit":
            exit()
        else:
            continue
        
x = CoffeeMachine()
main()