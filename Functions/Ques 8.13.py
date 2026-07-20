# 8-13. User Profile: Start with a copy of user_profile.py from the book.
# Build a profile of yourself by calling build_profile(), using your first and last names and three other key-value pairs that describe you.

def build_profile(firstname, lastname, **user_info):
    """ Build a dictionary consisting everything we know about a user. """
    
    user_info["first_name"] = firstname
    user_info["last_name"] = lastname
    
    return user_info

# Build a profile
user_profile = build_profile(
    "Shruti",
    "Mandaokar",
    location = "California",
    field = "Computer Science",
    hobby = "Music"
)

print(user_profile)