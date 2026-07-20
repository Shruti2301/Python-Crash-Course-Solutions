# 8-5. Cities: Write a function called describe_city() that accepts the name of a city and its country.
# The function should print a simple sentence, such as:
# "Reykjavik is in Iceland."
# Give the parameter for the country a default value.
# Call your function for three different cities, at least one of which is not in the default country.

def describe_city(cityname,country = "India"):
    """Display the city and its country."""
    print(f"\n {cityname} is in {country}")

# City 1
describe_city("Fort Wayne", "USA")

# City 2
describe_city("Bapatwadi")

# City 3
describe_city("Bhilai")