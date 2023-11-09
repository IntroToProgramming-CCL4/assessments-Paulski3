# Age variable
age = 18

# Stage of life
if age < 0:
    print('\nYou are unborn')
elif 0 <= age < 2:
    print('\nYou are a baby')
elif 2 <= age < 4:
    print('\nYou are a toddler')
elif 4 <= age < 13:
    print('\nYou are a kid')
elif 13 <= age < 20:
    print('\nYou are a teenager')
elif 20 <= age < 65:
    print('\nYou are an adult')
else:
    print('\nYou are an elder')
