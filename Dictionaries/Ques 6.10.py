# 6-10. Favorite Numbers: Modify your program from Exercise 6-2 so each person can have more than one favorite number.

# Use a dictionary called favorite_numbers.
# Use people's names as keys.
# Store a list of their favorite numbers as the values.
# Loop through the dictionary.
# Print each person's name and their favorite numbers.

favorite_numbers = {
    "Shruti": [7, 23, 99],
    "Saurabh": [10, 15, 20],
    "Srishti": [5, 12, 30],
    "Snigdha": [3, 8, 25],
    "Ally": [1, 4, 9]
}

for name, numbers in favorite_numbers.items():
    print(f"\n{name}'s favorite numbers are:")

    for number in numbers:
        print(f"- {number}")