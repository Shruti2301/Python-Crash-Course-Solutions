# 6-12. Extensions: We are now working with examples that are complex enough that they could be expanded in lots of different ways.

# Choose one of the programs you wrote in this chapter and extend it.

# For example:

# Add more information to your dictionaries.
# Add more features.
# Make your program more interactive.
# Add more data and display it in a useful way.


cities = {
    "Tokyo": {
        "country": "Japan",
        "population": 14000000,
        "language": "Japanese",
        "fact": "Tokyo is the capital city of Japan."
    },

    "Paris": {
        "country": "France",
        "population": 2100000,
        "language": "French",
        "fact": "Paris is famous for the Eiffel Tower."
    },

    "New York": {
        "country": "USA",
        "population": 8800000,
        "language": "English",
        "fact": "New York City is known as the Big Apple."
    }
}

for city, information in cities.items():
    print(f"\nCity: {city}")
    print(f"Country: {information['country']}")
    print(f"Population: {information['population']}")
    print(f"Main Language: {information['language']}")
    print(f"Interesting Fact: {information['fact']}")