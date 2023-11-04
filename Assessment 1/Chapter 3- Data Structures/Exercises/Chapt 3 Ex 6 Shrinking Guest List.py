# Chapt 3 Ex 4-5 program
names = ['Phillip', 'EmJay', 'Julia', 'Conching', 'Juvy', 'Perlito']
for name in names:
    print("Join me to dinner", name)

print("\n", names[1], "Cant make to dinner\n")

remove = names.pop(1)
new = names.insert(1, 'Katkat ')

for name in names:
    print("Join me to dinner", name)

# Chapt 3 Ex 6 program
print("\nDue to unexpected circumstances, only two guests can be invited to dinner\n")    # Announcement

# Deleting names till there is only 2 remaining
while len(names) > 2:
    delete = names.pop()
    print("Im sorry", delete, "I cant invite you to dinner.")   # A message for deleted names

print(' ')  # Whitespace

# A message for names that are still invited
for name in names:
    print("Fortunately, you are still invited", name)

# Emptying the list
del names[:]

print('\nCurrent list:', names)
