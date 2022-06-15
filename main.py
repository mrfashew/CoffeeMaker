from data import MENU, resources

# TODO 1: Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
coffee_command = input("What would you like? (espresso/latte/cappuccino): ")

rem_water = resources["water"]
rem_milk = resources["milk"]
rem_coffee = resources["coffee"]
money = 0


def coffee_machine(command):
    if command in MENU:
        drink_to_make = MENU[command]
        print(f"That will be: ${drink_to_make['cost']}.")
        return drink_to_make
    elif command == "report":
        print(f"Water: {rem_water}ml")
        print(f"Milk: {rem_milk}ml")
        print(f"Coffee: {rem_coffee}g")
        print(f"Money: ${money}")

# TODO 4: Check resources sufficient?


def check_resources(recipe, water, milk, coffee):
    global money, rem_water, rem_milk, rem_coffee
    water_required = recipe["ingredients"]["water"]
    milk_required = recipe["ingredients"]["milk"]
    coffee_required = recipe["ingredients"]["coffee"]
    cost = recipe["cost"]
    if amount_paid >= cost:
        return_change = round(amount_paid - cost, 2)
        money += cost
        if return_change > 0:
            print(f"Here is ${return_change} in change.")
        if water >= water_required:
            if milk >= milk_required:
                if coffee >= coffee_required:
                    rem_water -= water_required
                    rem_milk -= milk_required
                    rem_coffee -= coffee_required
                    print(f"Here is your {coffee_command}!")
                    return rem_water, rem_milk, rem_coffee
                else:
                    print("Sorry there's not enough coffee.")
            else:
                print("Sorry there's not enough milk.")
        else:
            print("Sorry there's not enough water.")
    else:
        print("Sorry that's not enough money. Money refunded.")


process = coffee_machine(coffee_command)
print("Please insert coins.")
quarters = int(input("How many quarters?: "))
dimes = int(input("How many dimes?: "))
nickels = int(input("How many nickels?: "))
pennies = int(input("How many pennies?: "))

amount_paid = round((quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01), 2)

check_resources(process, rem_water, rem_milk, rem_coffee)
coffee_command = input("What would you like? (espresso/latte/cappuccino): ")
coffee_machine(coffee_command)


# TODO 2: Turn off the Coffee Machine by entering “off” to the prompt.

# TODO 3: Print report.






# TODO 5: Process coins.

# TODO 6: Check transaction successful?

# TODO 7: Make Coffee
