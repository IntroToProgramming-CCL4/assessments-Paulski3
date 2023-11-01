# A variable with whitespaces and a name
name = "\tSun Tsu\n"

# Using different strips
print("Original:", name)  # Default
print("Lstrip:", name.lstrip())  # Strips leftside whitespaces
print("Rstrip:", name.rstrip())  # Strips rightside whitespaces
print("Strip:", name.strip())  # Strips all whitespaces
