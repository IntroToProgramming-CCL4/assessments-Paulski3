# Variables
budget = 50  # Budget given
price = 6  # Price of 1 USB

# Calculator
USB_bought = (budget // price)  # Calculates possible quantity of USB with given budget
left = budget - (USB_bought * price)  # Calculates the remaining money

# Results
print("\nYou can buy", USB_bought, "USB sticks for", budget, "pounds")
print("Change:", left, "pounds")
