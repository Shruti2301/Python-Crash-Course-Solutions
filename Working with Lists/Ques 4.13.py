# 4-13. Buffet  

# Store five foods in a tuple
foods = ("Pizza", "Burger", "Pasta", "Salad", "Soup")

print("The restaurant offers the following foods:")
for food in foods:
    print(food)

# The following line would cause an error because tuples cannot be changed
# foods[0] = "Sushi"

# The restaurant updates its menu
foods = ("Pizza", "Burger", "Sushi", "Tacos", "Soup")

print("\nThe restaurant has updated its menu:")
for food in foods:
    print(food)