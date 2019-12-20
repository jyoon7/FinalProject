import os
from mutagen.id3 import ID3
import pygame
from pygame import mixer
from tkinter import *
from tkinter.filedialog import askdirectory

root = Tk()
root.title("test")
root.minsize(300,300)

song = []
title = []
artist = []

index = 0

frame = Frame(root)
frame.pack()


box = Listbox(frame, width=20, height=20, font=("Helvetica", 12))
box.pack(side="left", fill="y")

scrollbar = Scrollbar(frame, orient="vertical")
scrollbar.config(command=box.yview)
scrollbar.pack(side="right", fill="y")

box.config(yscrollcommand=scrollbar.set)


directory = askdirectory()
os.chdir(directory)
for files in os.listdir(directory):
    if files.endswith(".mp3"):
        realdir = os.path.realpath(files)
        audio = ID3(realdir)
        
        song.append(files)
        title.append(audio['TIT2'].text[0])
        artist.append(audio['TPE1'].text[0])
        # listofsongs.append(audio['TPE3'].text[0])

# print(song[0])
# print(title[0])
# print(artist[0])


for x in song:
    box.insert(0,x)

# realnames.reverse()
# for items in realnames:
#     listbox.insert(0, items)
# realnames.reverse()





root.mainloop()
