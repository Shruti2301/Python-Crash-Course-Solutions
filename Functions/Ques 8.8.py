# 8-8. User Albums: Start with your program from Exercise 8-7.

# Write a while loop that allows users to enter an artist and an album title.
# Call your make_album() function with the user's input.
# Print the dictionary that is created.
# Be sure to include a quit value in the loop so the user can stop entering information.

def make_album(artist, title, numberofsongs = None):
    """ Builds a dictionary describing as music album. """
    album = {
        'artist': artist,
        'title' : title
    }
    
    if numberofsongs: 
        album['songs'] = numberofsongs
    
    return album


while True:
    print('\n Enter Album Information -')
    print("\n Enter 'quit' to Quit")
    
    artist = input('\n Enter Artist Name: ')
    if artist == 'quit':
        break
    
    title = input('\n Enter Album Title: ')
    if title == 'quit':
        break
    
    
    album1 = make_album(artist,title)
    print(album1)
    

album1 = make_album("Taylor Swift", "1989")
album2 = make_album("Ed Sheeran", "Divide")
album3 = make_album('Bruno Mars', 'The Romantic', 11)

print(album1)
print(album2)
print(album3)