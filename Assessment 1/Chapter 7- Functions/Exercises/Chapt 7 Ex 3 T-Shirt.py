# Funtion that accepts size and message
def make_shirt(size, message):
    print('Shirt size is', size, 'and the message displayed on it is', message + '.')


make_shirt('medium', 'Live Love Laugh')  # Calling the function using positional argument
make_shirt(message='Slaying life', size='large')    # Calling the funtion using keywords argument
