# 8-10. Sending Messages: Start with a copy of your program from Exercise 8-9.
# Write a function called send_messages() that prints each text message and moves each message to a new list called sent_messages.
# Call send_messages() with your list of messages.
# After calling the function, print both lists to make sure the messages were moved correctly.


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

send_message(messageslist)

print("\nOriginal List after sending:")
print(messageslist)

print("\n Sent Messages: ")
print(sent_messages)

