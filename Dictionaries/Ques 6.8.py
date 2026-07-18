# 6-8. Pets: Make several dictionaries, where each dictionary represents a different pet.

# In each dictionary, include:
# The kind of animal.
# The owner's name.
# Store these dictionaries in a list called pets.
# Loop through your list.
# As you loop through the list, print everything you know about each pet.

pet1 = {
    "animal": "Dog",
    "owner": "Shruti"
}

pet2 = {
    "animal": "Cat",
    "owner": "Saurabh"
}

pet3 = {
    "animal": "Parrot",
    "owner": "John"
}

pets = [pet1, pet2, pet3]

for pet in pets:
    print(f"\nAnimal: {pet['animal']}")
    print(f"Owner: {pet['owner']}")