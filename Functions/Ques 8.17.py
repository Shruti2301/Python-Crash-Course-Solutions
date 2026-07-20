# 8-17. Styling Functions: Choose any three programs you wrote for this chapter and make sure they follow the styling guidelines described in PEP 8.
# Review your code and check that you have:
# Used meaningful function and variable names.
# Added appropriate whitespace around operators and after commas.
# Limited line lengths where appropriate.
# Included blank lines between function definitions and other code.
# Written clear and descriptive comments or docstrings where helpful.

def favorite_book(title):
    """Display a message about a favorite book."""
    print(f"One of my favorite books is {title}.")


favorite_book("The Alchemist")
print('\n')

# 8-5. Cities

def describe_city(city_name, country="India"):
    """Display a city and its country."""
    print(f"{city_name} is in {country}.")


describe_city("Bhilai")
describe_city("Bapatwadi")
describe_city("Fort Wayne", "USA")

# 8-12. Sandwiches

def make_sandwich(*toppings):
    """Print the requested sandwich toppings."""

    print("\nMaking a sandwich with:")

    for topping in toppings:
        print(f"- {topping}")

print('\n')

make_sandwich("Cheese")
make_sandwich("Ham", "Cheese")
make_sandwich("Chicken", "Lettuce", "Tomato")