# 8-14. Cars: Write a function that stores information about a car in a dictionary.
# The function should always receive: A manufacturer and A model name
# It should then accept an arbitrary number of keyword arguments.
# Call the function with the required information and two other name-value pairs, such as a color or an optional feature.
# Your function should work for a call like this:

def make_car(manufacturer, model, **carinfo):
    """ Build a dictionary containing information about a car. """
    
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model
    
    return car_info

# Create a Car Dictionary
car = make_car(
    "Subaru",
    "Outback",
    color = "Blue",
    tow_package = True
)

print(car)
