# Chapt 3 Ex 4 program
names = ['Phillip', 'EmJay', 'Julia', 'Conching', 'Juvy', 'Perlito']

for name in names:
    print("Join me to dinner", name)

# Chapt 3 Ex 5 program
print("\n!" + names[1], "Cant make to dinner!\n")  # Guest who cant make it

# Modifying the list
remove = names.pop(1)  # Removing the guest that cant make it
new = names.insert(1, 'Katkat ')  # Inserting new guest into the list

for name in names:
    print("Join me to dinner", name)  # New invitation for the new modified list
