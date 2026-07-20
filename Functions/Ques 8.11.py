# 8-11. Archived Messages: Start with your work from Exercise 8-10.
# Call the function send_messages() with a copy of the list of messages.
# After the function call, print both the original list and the list of sent messages.
# Make sure the original list of messages is still available after sending the messages.
# Hint: You can make a copy of a list using slicing:


messageslist = [
    '1. We should not give up.',
    '2. If we put our mind to it, we can achieve anything.',
    '3. Love is all around us.',
    '4. Flowers are beautiful.'
]

sent_messages = []

def send_message(messages):
    """ Prints each text message and moves each message to a new list called sent_messages."""
    while messages: 
        poppedmsg = messages.pop()
        print(f"Moved Messages: {poppedmsg}")
        sent_messages.append(poppedmsg)
    
print("\n Original List:")
print(messageslist)

# Make a copy of original list
messages_copy = messages[:]

send_message(messageslist)

print("\nOriginal List after sending:")
print(messageslist)

print("\n Sent Messages: ")
print(sent_messages)

