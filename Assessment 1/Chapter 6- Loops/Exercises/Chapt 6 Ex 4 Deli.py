# List of sandwich order and an empty list
sandwich_orders = ['bacon', 'chicken', 'beef', 'egg', 'tuna']
finished_sandwiches = []

# Loop that announces the order of sandwiches been made
for sandwich in sandwich_orders:
    print('Your', sandwich, 'sandwich, has been made!')
    finished_sandwiches.append(sandwich)    # Moving the order sandwiches to a finished sandwich list

# A list showing the finished sandwiches
print("\nSandwiches that was made:")
for sandwich in finished_sandwiches:
    print('-' + sandwich.title(), 'sandwich.')
