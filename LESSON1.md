year = int(input("Enter the year: "))
genre = input("Enter the genre: ")
album = input("Enter the album: ")
title = input("Enter the title: ")
artist = input("Enter the artist: ")

print("*******************************")
print("SONG DETAILS")
print("*******************************")
print("Year Released: " + str(year))
print("Genre: " + genre)
print("Album: " + album)
print("Title: \"" + title + "\"")
print("Artist: " + artist)



char1, char2 = input("Enter two characters separated by a space: ").split()
larger_char = max(char1, char2)
print("*******************************")
print(f"The character with the larger value is: {larger_char}")
print("*******************************")

char1 = input("enter chracter: ")
asii = ord(char1)
print("*******************************")
print(f"The asii value of {char1} is {asii}.")
