# 7-9. No Pastrami: Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 'pastrami' appears in the list at least three times.
# Add a message near the beginning of your program saying the deli has run out of pastrami.
# Use a while loop to remove all occurrences of 'pastrami' from sandwich_orders.
# Make sure no pastrami sandwiches end up in finished_sandwiches.
# Print the completed sandwiches.

# 7-9. No Pastrami

sandwich_orders = [
    "tuna",
    "pastrami",
    "ham",
    "pastrami",
    "veggie",
    "grilled cheese",
    "pastrami",
    "chicken"
]

finished_sandwiches = []

print("Sorry, we have run out of pastrami today.\n ")

# Remove all pastrami orders
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

# Make the remaining sandwiches
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    print(f"I made your {current_sandwich} sandwich.")

    finished_sandwiches.append(current_sandwich)

print("\nThe following sandwiches have been made:")

for sandwich in finished_sandwiches:
    print(f"- {sandwich}")