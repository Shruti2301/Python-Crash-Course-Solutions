# 6-3. Glossary: A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let's call it a glossary.

# Think of five programming words you have learned in the previous chapters.
# Use these words as keys in a glossary dictionary.
# Store their meanings as values.
# Print each word and its meaning neatly.

glossary = {
    "variable": "A container used to store a value in a program.",
    "list": "A collection of items stored in a particular order.",
    "dictionary": "A collection of key-value pairs used to store data.",
    "loop": "A way to repeat a block of code multiple times.",
    "function": "A reusable block of code that performs a specific task."
}

print(f"Variable: {glossary['variable']}")
print(f"List: {glossary['list']}")
print(f"Dictionary: {glossary['dictionary']}")
print(f"Loop: {glossary['loop']}")
print(f"Function: {glossary['function']}")