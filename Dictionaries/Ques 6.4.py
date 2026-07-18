# 6-4. Glossary 2: Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3.

# Replace your series of print() statements with a loop that runs through the dictionary's keys and values.
# When you are sure that your loop works, add five more Python terms to your glossary.
# Your program should print each word and its meaning.

glossary = {
    "variable": "A container used to store a value in a program.",
    "list": "A collection of items stored in a particular order.",
    "dictionary": "A collection of key-value pairs used to store data.",
    "loop": "A way to repeat a block of code multiple times.",
    "function": "A reusable block of code that performs a specific task.",
    "tuple": "An immutable collection of items stored in order.",
    "class": "A blueprint for creating objects in Python.",
    "module": "A file containing reusable Python code.",
    "string": "A sequence of characters stored as text.",
    "integer": "A whole number used in programming."
}

for word, meaning in glossary.items():
    print(f"\n{word.title()}:")
    print(meaning)