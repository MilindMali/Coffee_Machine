MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }

}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# TODO  1.print report
# TODO  2.check if report are sufficient
# TODO  3.proces the coin
# TODO  4.check if transaction is successful
# TODO  5.make coffee

is_on=True

def is_resource_sufficient(ordered_ingredients):
    for item in ordered_ingredients:
        if ordered_ingredients[item]>= resources[item]:
            print(f'So sorry !!! There is no enough {item}')
            return False
    return True

def process_coins():
    """Returns total calculated from the inserted coins"""
    print("Please insert the coins: ")
    total = int(input("how many quarters:"))*0.25
    total += int(input("how many dimes:"))*0.10
    total += int(input("how many nickels:"))*0.05
    total += int(input("how many pennies:"))*0.01
    return total

def is_transaction_successful(money_received,drink_cost):
    if money_received>=drink_cost:
        change= round(money_received-drink_cost,2)
        print(f'Here is $ {change} in change')
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry, there is not sufficient money.")
        return False


def make_coffee(drink_name, ordered_ingredients):
    """To deduct the ingredients from resources"""
    for item in ordered_ingredients:
        resources[item]-=ordered_ingredients[item]
    print(f"Please enjoy your {drink_name}")



while is_on:
    choice=input("What would you like? (espresso/latte/cappuccino):")
    if choice== 'off':
        is_on=False
    elif choice== 'report':
        print(f"water :{resources['water']} ml")
        print(f"milk :{resources['milk']} ml")
        print(f"coffee:{resources['coffee']} gm")
        print(f"profit: ${profit}")

    else:
        drink= MENU[choice]
        if is_resource_sufficient(drink['ingredients']):
            payment=process_coins()
            if is_transaction_successful(payment,drink['cost']):
                make_coffee(choice,drink['ingredients'])










