# Function with a default size and message
def make_shirt(size='large', message='I love Python'):
    print('Shirt size is', size, 'and the message displayed on it is', message + '.')


# Make a large shirt and a medium shirt with the default message
make_shirt()
make_shirt('medium')

# A shirt of any size with a different message.
make_shirt('small', 'Coding is Fun')