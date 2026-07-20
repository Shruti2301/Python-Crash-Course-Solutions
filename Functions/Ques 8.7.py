# 8-7. Album: Write a function called make_album() that builds a dictionary describing a music album.
# The function should take in: An artist's name and An album title
# The function should return a dictionary containing these two pieces of information.
# Use the function to make three dictionaries representing different albums. 
# Print each return value to show that the dictionaries are storing the album information correctly.
# Add an optional parameter to store the number of songs on an album. 
# If the calling line includes a number of songs, add that value to the dictionary. 
# Make at least one new function call that includes the number of songs.

def make_album(artist, title, numberofsongs = None):
    """ Builds a dictionary describing as music album. """
    album = {
        'artist': artist,
        'title' : title
    }
    
    if numberofsongs: 
        album['songs'] = numberofsongs
    
    return album


album1 = make_album("Taylor Swift", "1989")
album2 = make_album("Ed Sheeran", "Divide")
album3 = make_album('Bruno Mars', 'The Romantic', 11)

print(album1)
print(album2)
print(album3)