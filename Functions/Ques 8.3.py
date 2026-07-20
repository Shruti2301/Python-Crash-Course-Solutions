# 8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt.

# The function should print a sentence summarizing the size of the shirt and the message printed on it.
# Call the function once using positional arguments.
# Call the function a second time using keyword arguments.

def make_shirt(size,text):
    """ Display information about the T-Shirt """
    print(f"\n T-shirt size: {size} ")
    print(f"\n Text: {text}")

# Positional Arguments
make_shirt(16,"I am a winner")

# Keyword Arguments
make_shirt(size = 20, text = "There is nothing to lose.")