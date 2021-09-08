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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# Description:
  # Make a coffee maker program that will ask the user what kind of hot drink they want (espresso, latte, cappuccino)
  # Other functions that can be added are a report function and an off function to exit the program
  # If a coffee drink is selected, first ask how much money they have in coins
  # Then determine if there are enough resources to produce the required coffee
    # If enough money and resources are available, then make the coffee
    # Otherwise output an error message

# Initialize a boolean flag that will keep the program running
isOn = True

# While this boolean is still true, run the program
while(isOn):
  # Ask the user what kind of hot drink they want
  selection = input('What drink would you like today? (espresso/latte/cappuccino): ')
  selection = selection.lower()
  # Determine the selection
  # If they input off, the jump out of the loop
  if (selection == 'off'):
    isOn = False
    print('Coffee machine turning off')
  elif (selection == 'report'):
    print(resources)
  elif selection in MENU.keys():
    print(selection)
  else:
    print('Drink not found')