import time

# Vending Machine Products
products = {
    # Item Code
    '10': {'item': 'pandesal\t',  # Item Name
           'type': {'1': 'original', '2': 'cheese', '3': 'ube', '4': 'nutella'},  # Item Variant
           'price': 1.5,  # Item Cost
           'stock': 20},  # Item Stock
    '20': {'item': 'empanada\t',
           'type': {'1': 'chicken', '2': 'beef'},
           'price': 4.5,
           'stock': 2},
    '30': {'item': 'Sausage waffle',
           'type': {'1': 'original', '2': 'ube', '3': 'chocolate'},
           'price': 5.5,
           'stock': 5},
    '40': {'item': 'hopia\t\t',
           'type': {'1': 'onion', '2': 'mongo', '3': 'nutella', '4': 'ube'},
           'price': 2.5,
           'stock': 8},
    '50': {'item': 'coffee\t\t',
           'type': {'1': 'iced', '2': 'hot'},
           'price': 2,
           'stock': 10},
    '60': {'item': 'tea\t\t\t',
           'type': {'1': 'iced', '2': 'hot'},
           'price': 1,
           'stock': 12},
    '70': {'item': 'choco milk\t',
           'type': {'1': 'cold', '2': 'hot'},
           'price': 2,
           'stock': 6},
    '80': {'item': 'water\t\t',
           'type': {'1': 'normal', '2': 'cold'},
           'price': 1,
           'stock': 18},
}
gap = '\n'  # New Line Variable
line = '========'   # Line Variable


# ---------------USER VENDING MACHINE INTERFACE END-----------------
# Vending Machine Menu
def vend_menu():
    print(line + "<WELCOME TO PAPHILL CAFE>" + line * 3)
    print('CODE\tPRODUCT\t\t\t\tPRICE\t\tSTOCK')    # Table Title Header

    for code, item in products.items():    # For each code and item in the menu
        view_iteminfo = f"{code}\t\t{item['item'].title()}\t\tAED {item['price']:.2f}\t"     # Displays item info
        # Checks if the item stock is empty
        if item['stock'] == 0:  # If item stock is empty
            stock_status = '[OUT OF STOCK]'    # Display [OUT OF STOCK] in Stock column
            print(view_iteminfo + stock_status)     # Combines item info and stock
        else:
            stock_status = f"{item['stock']} Remaining"    # If not then displays amount of stock remaining
            print(view_iteminfo + stock_status)     # Combines item info and stock
    print(line * 7)


# Shows Items Variants
def variant_menu(code):
    selected_item = products[code]  # Stores user selected item info
    print('____' * 6, '\nCODE NO.\tVARIANT')  # Table header
    for code, item in selected_item['type'].items():    # Prints out the selected item variants
        print(f"{code}\t\t\t{item.title()}")
    print('____' * 6)


# A prompt that ask the user to input a valid Variant
def variant_prompt(code):
    variant_info = products[code]['type']  # Selected Variant Dict
    variant_menu(code)   # Variant Menu
    item = {}   # The functions output
    while True:
        user_prompt2 = input('Select your desired variant: ')  # Prompt asking user for variant code
        if user_prompt2 in variant_info:    # If user input is in the variant dict
            item = variant_filter(code, user_prompt2)  # then the output will be the selected variant name
            break
        else:   # Otherwise the program will keep asking till the user gives a valid code
            print("Please input a valid code.")
            continue
    return item     # Variant name is added to the empty variable


# A filter that gets the variant name
def variant_filter(code, prompt2):
    item_variant = products[code]['type']  # Item Variant Info
    s_variant = {}  # Selected Variant Variable
    for number, name in item_variant.items():   # The name of the selected item variant
        if number == prompt2:   # Only the selected variant will be selected
            s_variant = name    # The variable contains the desired item variant
    return s_variant    # Appends the variant name into the empty variable


# A filter to skip the dict in 'type'
def iteminfo_filter(code):
    filtered_info = {}     # Filter output will be {item:x, price:y, stock:z}
    for key, value in products[code].items():   # For key and value in selected item
        if key == 'type':   # If the key is 'type'
            continue    # Skip, do not add the key & value
        else:   # Otherwise if the key is not 'type'
            filtered_info[key] = value     # Add the key and value
    return filtered_info   # The added key and value will be added to the variable filter


# A switch that turns on if stock is available
def stockcheck(code):
    switch = False      # Switch is off
    item = iteminfo_filter(code)['stock']    # Selected item stock
    if item == 0:   # If there is no stock
        print("Item Out of Stock.")     # Print item out of stock
    else:
        switch = True   # Otherwise turn switch on
    return switch


# Item Payment
def item_payment(selecteditem_code):
    item = iteminfo_filter(selecteditem_code)  # A Dict that contains the selected item's name, price, and stock
    var = variant_prompt(selecteditem_code)      # The selected variant name

    print(f"\n{var.title()} {item['item'].strip().title()}"   # Selected Item name
          f" Price: AED {item['price']:.2f}.")  # Selected item price

    price = item['price']   # Selected item price

    while price > 0:    # While the item is not zero payment proceeds
        try:    # If the user input is a number, program proceeds
            pay = float(input(f"Please insert AED {price:.2f}: "))  # Ask user to pay
            if pay < 0:     # If the pay is negative
                print('Invalid payment amount. Please insert money.')   # Ask user to put a valid number
                continue
            elif pay >= price:  # but if the pay is equal or more than the item price
                change = pay - price    # User's change
                print(f"\n{var.title()} {item['item'].strip().title()} has been dispensed! "  # Item dispensed
                      f"AED {change:.2f} has been refunded.\n")   # And the change will be refunded
                products[selecteditem_code]['stock'] -= 1  # The selected product stock gets subtracted
                break   # Payment is done
            else:   # But if the pay is 0 or less than the price
                print("Insufficient payment. Please insert more money.")    # Ask user for more money
                price -= pay    # The given money reduces the price
        except ValueError:  # If the user input is not a number
            print("Invalid payment amount. Please enter a valid number.")   # Asks user to put a valid number


# A method asking if the user wants to keep buying
def continue_buy():
    switch = True   # The whole function output is True

    # Ask user to put a valid input
    while True:
        answer = input('Continue to buy?(y/n): ')       # Asks the user if they would like to continue buying
        if answer.lower() == 'n':   # If the input is N/n
            print('Thank you for your patronage, please come again!', gap * 4)  # Thanked and bids farewell the user
            switch = False  # The whole function output will turn False
            time.sleep(3)   # A 3 seconds time before breaking the loop
            break
        elif answer.lower() == 'y':     # but if the input is Y/y
            print(gap * 2)      # A gap for less compact UI
            switch = False      # The whole function out will turn to False
            break       # Immediately
        else:   # Otherwise if the input is none of the above
            print("Please type 'y' to continue buying or "
                  "'n' when you are finish.")    # Instructs the user what to type
            continue    # Continue the loop till user gives a valid input
    return switch


# -----------------THE STOCK ROOM SECTION END-------------------
# Stock menu
def productStock():
    print('\nCODE\tPRODUCT\t\t\t\tSTOCK')   # Table Header
    for code, product in products.items():  # Accessing the code, product name, and stock remaining
        print(f"{code}\t\t{product['item'].title()}\t\t[{product['stock']}]")   # Displays the information


# A method that ask what product that you want to Stock up
def selecteditem_stock():
    switch = True   # The switch for the loop is on
    while switch:   # while True
        productStock()  # Display the stock menu
        while True:
            selected = input("Input product code[type 'exit' when done]: ")     # Input the product code
            if selected in products:    # If the input is in the product
                amount_stockup(selected)   # Asks how many amount to stock up
            elif selected.lower() == 'exit':    # but if the input is 'exit'
                print(gap * 2)
                switch = False  # The switch for the loop will turn off
                break   # The loop asking what product to stock up will stop
            else:   # Otherwise if the input is not in the menu or not a number
                print('Please put valid input')     # Instruct to put a valid input
                continue    # The loop asking what product to stock up will continue
        return switch


# A method to stock up items
def amount_stockup(code):
    item = products[code]   # Selected item dict
    print(f"{item['item'].title().strip()}\t[{item['stock']}]")     # Item name nad stock info
    stockup = int(input('Amount of stock add: '))   # Input how much amount to add in the item's stock
    while True:
        try:
            stockitem(code, stockup)    # Stocking up the item
            break
        except ValueError:  # Ensures the input is a number
            print('Please put a number')


# Updates stock changes
def stockitem(code, amountadd):
    products[code]['stock'] += amountadd    # Updating the stock
    item = products[code]   # Selected item dict
    if item['stock'] < 0:   # If the stock is below 0
        products[code]['stock'] = 0     # Then it updates the stock to 0 to prevent negative numbers
    print(f"{item['item'].title().strip()}\t[{item['stock']}]!!Updated!!")      # Updated information


# ----------------VENDING MACHINE PROGRAM---------------
# The Vending Machine program
def vend():
    machine = True  # Machine status = ON
    while machine:
        vend_menu()  # Vending Machine Menu
        ContinueToBuyItems = True   # Continue to buy status = ON
        while ContinueToBuyItems:
            user_prompt = input('Select your desired product code: ')   # Inputs users desired product to purchase
            if user_prompt in products:     # If the input is in the menu the user can buy
                while stockcheck(user_prompt):  # This is a gate to check if the selected item has stock left

                    # This function first asks the users selected item variant before payment
                    item_payment(user_prompt)
                    # When the payment is done, the machine dispenses the item and updates the stock
                    break
                # The user then decides if they would like to continue buying
                ContinueToBuyItems = continue_buy()    # If no then the machine says goodbye

            elif user_prompt == 'St0ckR00m':    # If the user inputs the stockroom password
                selecteditem_stock()  # You will then access the room to stock up the products or remove the products
                time.sleep(2)   # A suspense effect to show that the stocks are loading
                ContinueToBuyItems = False  # Goes back to the top of the program
                continue

            elif user_prompt.lower() == 'quit':     # If the input is 'quit' the whole machine restarts and shuts down
                machine = False
                ContinueToBuyItems = False
                continue

            else:   # If the input is invalid
                print('Please give a valid code')   # Then the machine asks the user to give a valid code
                continue


# Final Vending Machine
vend()
