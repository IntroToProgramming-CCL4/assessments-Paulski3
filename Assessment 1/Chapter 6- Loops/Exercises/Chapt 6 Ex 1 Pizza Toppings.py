# A loop asking the user for toppings
while True:
    toppings = input("\nInput your topping(Enter 'quit' when finished): ")
    if toppings != "quit":
        print("Adding", toppings, "to your pizza.")
    else:
        break
