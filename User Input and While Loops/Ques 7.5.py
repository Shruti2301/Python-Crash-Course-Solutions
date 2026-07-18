# 7-5. Movie Tickets: A movie theater charges different ticket prices based on a person's age.

# Write a program that asks the user for their age and then tells them the cost of their movie ticket.

# Rules:
# If a person is under 3 years old, the ticket is free.
# If a person is between 3 and 12 years old, the ticket costs $10.
# If a person is over 12 years old, the ticket costs $15.

age = input("How old are you?")

age = int(age)

if age < 3:
    print("Your ticket is free")
elif age <= 12:
    print('Your ticket costs $10')
else:
    print('Your ticket costs $15')