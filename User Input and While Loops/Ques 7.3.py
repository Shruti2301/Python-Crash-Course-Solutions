# 7-3. Multiples of Ten: Ask the user for a number, and then report whether the number is a multiple of 10.

# Use the input() function to get a number from the user.
# Convert the input to an integer.
# Use an if statement to check whether the number is divisible by 10.
# Print a message telling the user whether the number is a multiple of 10.

number = input("Enter a number : ")
number = int(number)

if number % 10 == 0: 
    print(f"{number} is a multiple of 10")
else:
    print(f"{number} is not a multiple of 10")
    