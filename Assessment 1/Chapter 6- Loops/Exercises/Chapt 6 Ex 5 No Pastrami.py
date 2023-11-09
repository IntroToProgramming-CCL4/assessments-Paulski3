# Using the list from Chapt 6 Ex 4 and adding 3 pastrami
sandwich_orders = ['bacon', 'pastrami', 'chicken', 'pastrami', 'beef', 'egg', 'pastrami', 'tuna']
finished_sandwiches = []

# Announcing outage of pastrami
print('\nUnfortunately, we have run out of pastrami.\n')

# Removing pastrami in the orders
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

# Loop that announces the order of sandwiches been made
for sandwich in sandwich_orders:
    print('Your', sandwich, 'sandwich, has been made!')
    finished_sandwiches.append(sandwich)    # Moving the order sandwiches to a finished sandwich list

# A list showing the finished sandwiches
print("\nSandwiches that was made:")
for sandwich in finished_sandwiches:
    print('-' + sandwich.title(), 'sandwich.')
