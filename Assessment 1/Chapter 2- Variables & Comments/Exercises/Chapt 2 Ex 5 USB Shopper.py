budget = 50  # budget given
price = 6  # 1 USB price

# Calculator
USB_bought = (budget // price)  # Calculates possible quantity of USB with given budget
left = budget - (USB_bought * price)  # Calculates the remaining money

# Results
print("You can buy", USB_bought, "USB sticks for", budget, "pounds")
print("Change:", left, "pounds")
