# 3-10. Every Function: Think of something you could store in a list. 
# For example, you could make a list of mountains, rivers, countries, cities, languages, or anything else you’d like. 
# Write a program that creates a list containing these items and then uses each function introduced in this chapter at least once.

items = ["mountain", "river", "country", "city", "language"]
print("The items in the list are: ", items)
items.append("animal")
print("The items in the list are: ", items)
items.insert(0, "plant")
print("The items in the list are: ", items)
items.remove("country")
print("The items in the list are: ", items)
items.sort()
print("The items in the list are: ", items)
items.sort(reverse=True)
print("The items in the list are: ", items)