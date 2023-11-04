# Creating a dictionary
glossary = {'variables': 'Containers for storing data values.',
            'constants': 'Variable whose values do not change.',
            'keywords': 'Reserved words in Python.',
            'strings': 'Sequences of characters surrounded by quotes.',
            'dictionary': 'A collection of key-value pairs.',
            'comment': 'A note in a program that the Python interpreter ignores.',
            'key': 'The first item in a key-value pair in a dictionary.',
            'value': 'An item associated with a key in a dictionary.',
            'loop': 'Work through a collection of items, one at a time.',
            'list': 'A collection of items in a particular order.'}

# Printing the glossary
print('Glossary')
for key, value in glossary.items():
    print('\n' + key.title() + ':', '\n', value)