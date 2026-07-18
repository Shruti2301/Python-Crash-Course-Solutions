# 6-7. People: Start with the program you wrote for Exercise 6-1 (Person). 
# Create two new dictionaries representing different people, and store all three dictionaries in a list called people.

# Loop through the list of people.
# Print everything you know about each person.

person1 = {
    "first_name": "Shreya",
    "last_name": "Singh",
    "age": 7,
    "city": "Bhilai"
}

person2 = {
    "first_name": "Smitha",
    "last_name": "Singh",
    "age": 25,
    "city": "Pune"
}

person3 = {
    "first_name": "John",
    "last_name": "Smith",
    "age": 30,
    "city": "New York"
}

people = [person1, person2, person3]

for person in people:
    print(f"\nFirst Name: {person['first_name']}")
    print(f"Last Name: {person['last_name']}")
    print(f"Age: {person['age']}")
    print(f"City: {person['city']}")