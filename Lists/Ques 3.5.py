# 3-5. Changing Guest List: You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. 
# You’ll have to think of someone else to invite.
# Start with your program from Exercise 3-4. Add a print() call at the end of your program stating the name of the guest who can’t make it.
# Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
# Print a second set of invitation messages, one for each person who is still in your list.

guests = ["Shruti", "Smitha", "John", "Rose", "Jim"]
print(f"Dear {guests[0]}, you are invited to a dinner at my house.")
print(f"Sorry {guests[1]}, you can't make it to the dinner.")
guests[1] = "Raj"
print(f"Dear {guests[1]}, you are invited to a dinner at my house.")
print(f"Dear {guests[2]}, you are invited to a dinner at my house.")
print(f"Dear {guests[3]}, you are invited to a dinner at my house.")
print(f"Dear {guests[4]}, you are invited to a dinner at my house.")