# Creating a dictionary
glossary = {'variables': 'Containers for storing data values.',
            'constants': 'Variable whose values do not change.',
            'keywords': 'Reserved words in Python.',
            'strings': 'Sequences of characters surrounded by quotes.',
            'dictionary': 'A collection of key-value pairs.'}

# Printing the glossary
print('Glossary')

key = 'variables'
print('\n' + key.title() + ':', '\n', glossary[key])
key = 'constants'
print('\n' + key.title() + ':', '\n', glossary[key])
key = 'keywords'
print('\n' + key.title() + ':', '\n', glossary[key])
key = 'strings'
print('\n' + key.title() + ':', '\n', glossary[key])
key = 'dictionary'
print('\n' + key.title() + ':', '\n', glossary[key])