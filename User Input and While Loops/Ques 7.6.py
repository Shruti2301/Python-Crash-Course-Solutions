# 7-6. Three Exits: Write a version of the Pizza Toppings program from Exercise 7-4 that does the following:

# Use a while loop with a condition to control when the loop stops.
# Allow the user to enter pizza toppings.
# Stop the program when the user enters "quit".
# Print a message each time a topping is added.

# Try using:
# A conditional test in the while statement.
# An active variable (flag) to control the loop.
# A break statement.

prompt = "\n Enter a pizza topping you will like to add"
prompt += "\n Enter 'quit' when you are finished - "

while True:
    topping = input(prompt)
    
    if topping == 'quit':
        break
    else:
        print(f" Adding {topping} to your Pizza")