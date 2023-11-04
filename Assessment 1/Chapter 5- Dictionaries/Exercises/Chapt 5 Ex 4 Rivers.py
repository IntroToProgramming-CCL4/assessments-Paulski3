#
rivers = {'nile': 'egypt', 'yangtze': 'china', 'missouri': 'united state'}

for key, value in rivers.items():
    print('The', key.title(), 'runs through', value.title())

print('\nRivers:')
for key in rivers.keys():
    print('-' + key.title())

print('\nCountries:')
for value in rivers.values():
    print('-' + value.title())
