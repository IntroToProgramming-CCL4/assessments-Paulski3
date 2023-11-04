# A list of dictionaries
pets = [{'animal type': 'rabbit', 'name': 'sunshine', 'owner': 'paul', 'chews': 'wires'},
        {'animal type': 'dog', 'name': 'rocky', 'owner': 'roxanne', 'chews': 'slippers'},
        {'animal type': 'hamster', 'name': 'pierre', 'owner': 'andrei', 'chews': 'wood'}]

# Display pet information
for pet in pets:
    print('\n' + pet['name'].title(), 'pet information:')
    for key, value in pet.items():
        print(key + ':', value)
