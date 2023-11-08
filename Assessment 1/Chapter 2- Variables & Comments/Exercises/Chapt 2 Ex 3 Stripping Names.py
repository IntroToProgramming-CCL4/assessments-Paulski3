# A variable with whitespaces and a name
name = "\tSun Tsu\n"

# Using different strips
print("\nOriginal:", name)  # Default
print("Lstrip:", name.lstrip())  # Strips leftside whitespaces
print("Rstrip:", name.rstrip())  # Strips rightside whitespaces
print("\nStrip:", name.strip())  # Strips all whitespaces
