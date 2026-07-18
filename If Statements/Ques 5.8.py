# 5-8. Hello Admin: Make a list of five or more usernames, including the name 'admin'. Imagine you are writing code that will print a greeting to each user after they log in.

# Loop through the list.
# If the username is 'admin', print a special greeting:
# "Hello admin, would you like to see a status report?"
# Otherwise, print a generic greeting:
# "Hello Eric, thank you for logging in again."

usernames = ["admin", "Shruti", "Smitha", "John", " Ally" ]

for username in usernames:
    if username == "admin":
        print("Hello Admin, would you like to see a status report?")
    else:
        print(f"Hello {username}, thank you for logging in again.")