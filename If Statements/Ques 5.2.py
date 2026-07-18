
# 5-2. More Conditional Tests

# Tests for equality and inequality with strings
name = "Shruti"

print("Is name == 'Shruti'? I predict True.")
print(name == "Shruti")

print("\nIs name != 'John'? I predict True.")
print(name != "John")

# Tests using the lower() method
city = "PUNE"

print("\nIs city.lower() == 'pune'? I predict True.")
print(city.lower() == "pune")

print("\nIs city.lower() == 'mumbai'? I predict False.")
print(city.lower() == "mumbai")

# Numerical tests
age = 22

print("\nIs age == 22? I predict True.")
print(age == 22)

print("\nIs age != 18? I predict True.")
print(age != 18)

print("\nIs age > 20? I predict True.")
print(age > 20)

print("\nIs age < 20? I predict False.")
print(age < 20)

print("\nIs age >= 22? I predict True.")
print(age >= 22)

print("\nIs age <= 21? I predict False.")
print(age <= 21)

# Tests using the and operator
print("\nIs age > 18 and age < 30? I predict True.")
print(age > 18 and age < 30)

print("\nIs age > 25 and age < 30? I predict False.")
print(age > 25 and age < 30)

# Tests using the or operator
print("\nIs age < 18 or age == 22? I predict True.")
print(age < 18 or age == 22)

print("\nIs age < 18 or age > 30? I predict False.")
print(age < 18 or age > 30)

# Test whether an item is in a list
fruits = ["apple", "banana", "orange"]

print("\nIs 'apple' in fruits? I predict True.")
print("apple" in fruits)

print("\nIs 'grape' in fruits? I predict False.")
print("grape" in fruits)

# Test whether an item is not in a list
print("\nIs 'grape' not in fruits? I predict True.")
print("grape" not in fruits)

print("\nIs 'banana' not in fruits? I predict False.")
print("banana" not in fruits)