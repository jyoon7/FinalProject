import os
from mutagen.id3 import ID3
import pygame
from pygame import mixer
from tkinter import *
from tkinter.filedialog import askdirectory

root = Tk()
root.title("test")
root.minsize(300,300)
mixer.init()

song = []
title = []
artist = []

index = 0



directory = askdirectory()
os.chdir(directory)

for files in os.listdir(directory):
    x = 0
    if files.endswith(".mp3"):
        realdir = os.path.realpath(files)
        audio = ID3(realdir)
        
        song.append(files)
        title.append(audio['TIT2'].text[0])
        artist.append(audio['TPE1'].text[0])
        # listofsongs.append(audio['TPE3'].text[0])
        x += 1

print(song[0])
print(title[0])
print(artist[0])



label = Label(root, text="Music player")
label.pack()


listbox = Listbox(root)
listbox.pack()

# realnames.reverse()
# for items in realnames:
#     listbox.insert(0, items)
# realnames.reverse()





root.mainloop()
