# Dictionary of rivers and its countries
rivers = {'nile': 'egypt', 'yangtze': 'china', 'missouri': 'united state'}

# Loop of rivers information
for key, value in rivers.items():
    print('The', key.title(), 'runs through', value.title())

# Loop to print the name of each river included in the dictionary.
print('\nRivers:')
for key in rivers.keys():
    print('-' + key.title())

# Loop to print the name of each country included in the dictionary.
print('\nCountries:')
for value in rivers.values():
    print('-' + value.title())
