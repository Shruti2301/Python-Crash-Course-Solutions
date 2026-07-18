# Code Review : Choose three  of the programs you have written  in this chapter and modify each one to comply with PEP 8

# 4-15. Code Review
# Three programs rewritten to comply with PEP 8.

# ---------------------------------------
# Program 1: Guest List
# ---------------------------------------

guests = ["Shruti", "Smitha", "John"]

print("Guest List:")
for guest in guests:
    print(f"Dear {guest}, you are invited to dinner at my house.")

print()

# ---------------------------------------
# Program 2: Seeing the World
# ---------------------------------------

places = ["Japan", "Switzerland", "New Zealand", "Canada", "Norway"]

print("Original list:")
print(places)

print("\nTemporarily sorted:")
print(sorted(places))

print("\nOriginal list:")
print(places)

print("\nReverse alphabetical order:")
print(sorted(places, reverse=True))

print("\nOriginal list:")
print(places)

places.reverse()
print("\nReversed list:")
print(places)

places.reverse()
print("\nBack to original:")
print(places)

places.sort()
print("\nSorted alphabetically:")
print(places)

places.sort(reverse=True)
print("\nSorted in reverse alphabetical order:")
print(places)

print()

# ---------------------------------------
# Program 3: Buffet
# ---------------------------------------

foods = ("Pizza", "Burger", "Pasta", "Salad", "Soup")

print("The restaurant offers:")
for food in foods:
    print(food)

foods = ("Pizza", "Burger", "Sushi", "Tacos", "Soup")

print("\nThe restaurant has updated its menu:")
for food in foods:
    print(food)