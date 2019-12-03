import spotScrape

artist = "Radiohead"
song = "Creep"

print("Creep by Radiohead:\n")
print(spotScrape.getDurationWithoutAlbum(artist, song))



artist = "rihanna"
song = "SOS"

print("SOS by Rihanna:\n")
print(spotScrape.getDurationWithoutAlbum(artist, song))