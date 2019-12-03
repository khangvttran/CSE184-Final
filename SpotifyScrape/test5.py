import spotScrape

artist = "Radiohead"
song = "Creep"

print("Creep by Radiohead:\n")
print(spotScrape.getDurationWithoutAlbum(artist, song))



artist = "Car Seat Headrest"
song = "Something Soon"

print("something Soon by CSH:\n")
print(spotScrape.getDurationWithoutAlbum(artist, song))