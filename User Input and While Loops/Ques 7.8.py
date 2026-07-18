# 7-8. Deli: Make a list called sandwich_orders and fill it with the names of various sandwiches.

# Then make an empty list called finished_sandwiches.
# Loop through the list of sandwich orders.
# As each sandwich is made, print a message such as:
# "I made your tuna sandwich."
# Move each sandwich to the list of finished sandwiches.
# After all the sandwiches have been made, print a message listing each sandwich that was made.

sandwich_orders = [
    "tuna",
    "ham",
    "veggie",
    "grilled cheese",
    "chicken"
]

finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    print(f"I made your {current_sandwich} sandwich.")

    finished_sandwiches.append(current_sandwich)

print("\nThe following sandwiches have been made:")

for sandwich in finished_sandwiches:
    print(f"- {sandwich}")