# 3-7. Shrinking Guest List

guests = ["Raj", "Shruti", "Smitha", "Rajesh", "John", "Rose", "Jim", "Aisha"]

# Invite everyone
for guest in guests:
    print(f"Dear {guest}, you are invited to dinner at my house.")

print("\nUnfortunately, my new dinner table won't arrive in time.")
print("I can invite only two people for dinner.\n")

# Remove guests until only two remain
while len(guests) > 2:
    removed_guest = guests.pop()
    print(f"Sorry {removed_guest}, I can't invite you to dinner.")

# Invite the remaining two guests
print()
for guest in guests:
    print(f"Dear {guest}, you're still invited to dinner!")

# Remove the last two guests
del guests[0]
del guests[0]

# Print the empty list
print("\nGuest list:", guests)