# 6-9. Favorite Places: Make a dictionary called favorite_places. Think of three names and use them as keys in your dictionary.

# Store one to three favorite places for each person.
# Loop through the dictionary.
# Print each person's name and their favorite places.

favorite_places = {
    "Shruti": ["Japan", "Switzerland", "Italy"],
    "Smitha": ["Paris", "London", "New York"],
    "John": ["Canada", "Australia", "Brazil"]
}

for name, places in favorite_places.items():
    print(f"\n{name}'s favorite places are:")

    for place in places:
        print(f"- {place}")