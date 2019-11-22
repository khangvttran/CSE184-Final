import spotScrape

artist = "Radiohead"
album = "Pablo Honey"
song = "Creep"

print("The duration of Creep is " + str(spotScrape.getDuration(artist, album, song)))