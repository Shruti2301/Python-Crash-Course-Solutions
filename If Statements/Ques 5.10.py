# 5-10. Checking Usernames: Do the following to create a program that simulates how websites ensure that everyone has a unique username.

# Make a list of five or more usernames called current_users.
# Make another list of five usernames called new_users.
# Make sure one or two of the new usernames are also in the current_users list.
# Loop through the new_users list to check whether each username has already been used.
# If it has been used, print:
# "Sorry, username 'Eric' is already taken. Please enter a new username."
# Otherwise, print:
#"The username 'Eric' is available."

#Note: Make sure your comparison is case insensitive. If "John" is already used, "JOHN" should not be accepted as a new username.

current_users = ['Shruti', 'Smitha', 'John', 'Ally', 'admin']
new_users = ['Shruti', 'Smitha', 'Sarah', 'Aiden', 'Candy']

# A list of lowercase usernames
current_users_lower = []

for user in current_users:
    current_users_lower.append(user.lower())

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print("Sorry! Username {new_user} is already taken. Please enter a new username.")
    else:
        print(f"The Username '{new_user}' is available. ")