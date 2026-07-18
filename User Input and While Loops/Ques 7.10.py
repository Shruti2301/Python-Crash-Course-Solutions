# 7-10. Dream Vacation: Write a program that polls users about their dream vacation.

# Write a prompt similar to:
# "If you could visit one place in the world, where would you go?"
# Include a block of code that prints the results of the poll.
# You can use a while loop to allow multiple people to respond.

responses = {}

polling_active = True

while polling_active:
    name = input("\n What is your name? ")
    vacation = input("\n If you could visit one place in the world, where would you go? - ")
    
    responses[name] = vacation
    
    repeat = input("\n Would you like another person to respond? (yes/no) - ")
    
    if repeat == 'no':
        polling_active = False

print("\nDream Vacation Poll Results")
for name, vacation in responses.items():
    print(f"{name} would like to visit {vacation}.")
    
        
    