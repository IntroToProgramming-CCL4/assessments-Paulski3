# A list of places in the world I would like to visit
world = ['Japan', 'Canada', 'Korea', 'Singapore', 'Iceland']
print('\nCurrent list:', world)

# Using sorted() to temporarily sort the list
print('\nTemporary sort:', sorted(world))
print('\nCurrent list:', world)

# Using sorted() with reverse to temporarily sort the list in reverse
print('\nTemporary sort in reverse:', sorted(world, reverse=True))
print('\nCurrent list:', world)

# Reversing the list
world.reverse()
print('\nReversed current list:', world)

# Reversing the list again to go back to its original order
world.reverse()
print('\nBack to Original Current list:', world)

# Sorting the list
world.sort()
print('\nSorted Current list:', world)

# Sorting the list in reverse
world.sort(reverse=True)
print('\nSorted and reversed Current list:', world)
