# A loop determining the ticket cost depending on users age
while True:
    age = input('\nInput your age("quit" to stop): ')
    if age == 'quit':
        break
    age = int(age)

    if age < 0:
        print('Age Error')
    elif 0 < age < 3:
        print('Your ticket is free')
    elif 3 <= age <= 12:
        print('Your ticket cost $10')
    else:
        print('Your ticket cost $15')
