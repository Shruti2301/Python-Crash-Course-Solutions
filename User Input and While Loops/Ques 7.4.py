# 7-4. Pizza Toppings: Write a program that prompts the user to enter a series of pizza toppings until they enter a 'quit' value.

# Each time the user enters a topping, print a message saying you’ll add that topping to their pizza.
# When they enter "quit", stop asking for toppings.

prompt = "\n Enter a pizza topping you would like to add"
prompt += "\n Enter 'quit' when you are finished - "

while True:
    topping = input(prompt)
    
    if topping == 'quit':
        break
    else:
        print(f" Adding {topping} to your pizza.")
    