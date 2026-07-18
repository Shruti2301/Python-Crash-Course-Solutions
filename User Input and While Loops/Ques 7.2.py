# 7-2. Restaurant Seating: Write a program that asks the user how many people are in their dinner group.

# If the answer is more than 8, print a message saying:
# "You'll have to wait for a table."
# Otherwise, print a message saying:
# "Your table is ready."

people = input("How many people are there in your dinner group?")

people = int(people)

if people > 8 :
    print("You will have to wait for a table.")
else:
    print("Your table is ready.")