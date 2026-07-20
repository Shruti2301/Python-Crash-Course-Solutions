# 8-12. Sandwiches: Write a function that accepts a list of items a person wants on a sandwich.
# The function should have one parameter that collects as many sandwich toppings as the function call provides.
# The function should print a summary of the sandwich that is being ordered.
# Call the function three times, using a different number of arguments each time.

def make_sandwich(*toppings):
    """ Print the requested toppings for the sandwich. """
    print("\n Make a sandwich with the following toppings :")
    
    for topping in toppings:
        print(f"-{topping}")
        
# Variant 1
make_sandwich("Cheese")

# Variant 2
make_sandwich("Pepperoni", "Cheese", "Ham")

# Variant 3
make_sandwich("Chicken", "Lettuce", "Tomato", "Cheese")