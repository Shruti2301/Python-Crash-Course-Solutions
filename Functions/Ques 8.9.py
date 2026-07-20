# 8-9. Messages: Make a list containing a series of short text messages.
# Pass the list to a function called show_messages().
# The function should print each text message.

messageslist = [
    '1. We should not give up.',
    '2. If we put our mind to it, we can achieve anything.',
    '3. Love is all around us.',
    '4. Flowers are beautiful.'
]

def show_messages(messages):
    """ Print the list of short text messages."""
    
    for message in messages:
        print(message)
    
show_messages(messageslist)