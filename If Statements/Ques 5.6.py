# 5-6. Stages of Life: Write an if-elif-else chain that determines a person's stage of life.

# Set a value for a variable called age, and then:

# If the person is less than 2 years old, print a message that the person is a baby.
# If the person is at least 2 but less than 4, print that the person is a toddler.
# If the person is at least 4 but less than 13, print that the person is a kid.
# If the person is at least 13 but less than 20, print that the person is a teenager.
# If the person is at least 20 but less than 65, print that the person is an adult.
# If the person is age 65 or older, print that the person is an elder.

age = 25

if age < 2:
    print("This person is a baby.")
elif age < 4:
    print(" This person is a toddler.")
elif age < 13:
    print("This person is  a kid.")
elif age < 20: 
    print("This person is a teenager.")
elif age < 65: 
    print("This person is an adult")
else:
    print("This person is an elder.")