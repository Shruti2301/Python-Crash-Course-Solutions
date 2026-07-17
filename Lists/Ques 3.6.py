guests = ["Shruti", "Smitha", "John", "Rose", "Jim"]

for guest in guests:
    print(f"Dear {guest}, you are invited to dinner at my house.")

print("\nI found a bigger dinner table, so now more space is available!")

guests.insert(0, "Raj")
guests.insert(len(guests) // 2, "Rajesh")
guests.append("Aisha")

for guest in guests:
    print(f"Dear {guest}, you are invited to dinner at my house.")