# 6-6. Polling: Use the code from Exercise 6-5 (Rivers) and create a program that stores information about people who took a favorite language poll.

# Make a list of people who should take the favorite programming language poll.
# Loop through the list of people.
# If they have not taken the poll, print a message inviting them to take it.
# Create a dictionary called favorite_languages that stores people's favorite programming languages.
# Check which people have already taken the poll and which people still need to respond.

favourite_languages = {
    "Shruti" : "Python",
    "Saurabh" : "Java",
    "Ally" : 'C++',
    "Aiden" : 'C'
}

people_to_poll = ['Shruti', 'Saurabh', 'Ally', 'Aiden', 'John', 'Shrey']

for person in people_to_poll:
    if person in favourite_languages.keys():
         print(f"Thank you {person} for taking the poll!")
    else:
        print(f"{person}, please take our favorite programming language poll.")