# 6-5. Rivers: Make a dictionary containing three major rivers and the country each river runs through.

# Use the name of a river as the key.
# Use the name of a country as the value.
# Print a sentence about each river, such as:
# "The Nile runs through Egypt."
# Use a loop to print the name of each river included in the dictionary.
# Use another loop to print the name of each country included in the dictionary.

rivers = {
    "Nile": "Egypt",
    "Amazon": "Brazil",
    "Ganges": "India"
}

# Print sentence about each river
for river, country in rivers.items():
    print(f'The {river} runs through the {country}')

print("\n Rivers included in the dictionary : ")

# Print each river name
for river in rivers.keys():
    print(river)


print("\n Countries included in the dictionary : ")
# Print each country name
for country in rivers.values():
    print(country)