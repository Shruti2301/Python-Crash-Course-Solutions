# 8-4. Large Shirts: Modify the make_shirt() function so that shirts are large by default with a message that reads:
# I love Python
# Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.

def make_shirt(size = 'Large',text = 'I love Python'):
    """ Display information about the T-Shirt """
    print(f"\n T-shirt size: {size} ")
    print(f"\n Text: {text}")


# Large shirt with the default message
make_shirt()

# Medium shirt with the default message
make_shirt(size="Medium")

# Small shirt with a custom message
make_shirt(size="Small", text="There is nothing to lose.")