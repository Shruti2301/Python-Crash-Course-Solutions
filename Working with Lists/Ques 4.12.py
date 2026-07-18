# More Loops: All Versions of foods.py
# Make a copy of foods.py and name it foods2.py.
# In foods2.py, add a line that prints the message The third item in the list is [insert the third item in the list].
# Add a line that prints the last three items in the list.
# Make a copy of foods.py and name it foods3.py.
# In foods3.py, add a line that prints the message The first three items in the list are: and then use a slice to print the first three items from that program’s list.
# Make a copy of foods.py and name it foods4.py.
# In foods4.py, add a line that prints the message Three items from the middle of the list are: and then use a slice to print three items from the middle of the list.
# Make a copy of foods.py and name it foods5.py.
# In foods5.py, add a line that prints the message The last three items in the list are: and then use a slice to print the last three items from the list.

foods = ["pizza", "hamburger", "salad", "pasta", "sushi"]
print("The third item in the list is: ", foods[2])
print("The last three items in the list are: ", foods[-3:])
print("The first three items in the list are: ", foods[:3])
print("Three items from the middle of the list are: ", foods[1:4])
print("The last three items in the list are: ", foods[-3:])