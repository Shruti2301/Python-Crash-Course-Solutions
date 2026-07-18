# 6-11. Cities: Make a dictionary called cities.

# Use the names of three cities as keys in your dictionary.
# Create a dictionary of information about each city and include:
# The country that the city is in.
# An approximate population.
# One fact about that city.
# Print the name of each city and all the information you have stored about it.

# Dictionary in a Dictionary

cities = {
    "Tokyo": {
        "country": "Japan",
        "population": 14000000,
        "fact": "Tokyo is the capital city of Japan."
    },

    "Paris": {
        "country": "France",
        "population": 2100000,
        "fact": "Paris is famous for the Eiffel Tower."
    },

    "New York": {
        "country": "USA",
        "population": 8800000,
        "fact": "New York City is known as the Big Apple."
    }
}

for city, information in cities.items():
    print(f"\nCity: {city}")
    print(f"Country: {information['country']}")
    print(f"Population: {information['population']}")
    print(f"Fact: {information['fact']}")