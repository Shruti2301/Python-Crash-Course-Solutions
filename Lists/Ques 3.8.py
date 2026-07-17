# 3-8. Seeing the World: Think of at least five places in the world you’d like to visit.
# Store the locations in a list. Make sure the list is not in alphabetical order.
places = ["Paris", "Tokyo", "New York", "London", "Sydney", "Switzerland", "Dubai", "Berlin", "Rome", "Madrid"]
# Print your list in its original order. Don’t worry about printing the list neatly, just print it as a raw Python list.
print("The places I want to visit are: ", places)
# Use sorted() to print your list in alphabetical order without modifying the actual list.
print("The places I want to visit in alphabetical order are: ", sorted(places))
# Show that your list is still in its original order by printing it.
print("The places I want to visit in original order are: ", places)
# Use sorted() to print your list in reverse alphabetical order without changing the order of the original list.
print("The places I want to visit in reverse alphabetical order are: ", sorted(places, reverse=True))
# Show that your list is still in its original order by printing it again.
print("The places I want to visit in original order are: ", places)
# Use reverse() to change the order of your list. Print the list to show that its order has changed.
places.reverse()
print("The places I want to visit in reverse order are: ", places)
# Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
places.reverse()
print("The places I want to visit in original order are: ", places)
# Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
places.sort()
print("The places I want to visit in alphabetical order are: ", places)
# Use sort() to change your list so it’s stored in reverse alphabetical order. Print the list to show that its order has been changed.
places.sort(reverse=True)
print("The places I want to visit in reverse alphabetical order are: ", places)

