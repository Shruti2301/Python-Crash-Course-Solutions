# Summing a Million: Make a list of the numbers from one to one million, and then use min() and max() to make sure your list actually starts at one and ends at one million.
# Also, use the sum() function to see how quickly Python can add a million numbers.

numbers = list(range(1, 1000001))
print("The minimum number in the list is: ", min(numbers))
print("The maximum number in the list is: ", max(numbers))
print("The sum of the numbers in the list is: ", sum(numbers))