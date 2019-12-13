import os
from mutagen.id3 import ID3
import pygame
from tkinter import *
from tkinter.filedialog import askdirectory

root = Tk()
root.title("Music Player")
root.minsize(300,300)

listofsongs = []
realnames =[]
index = 0


def directorychooser():
    directory = askdirectory()
    os.chdir(directory)

    for files in os.listdir(directory):
        if files.endswith(".mp3"):
            realdir = os.path.realpath(files)
            audio = ID3(realdir)
            realnames.append(audio['TIT2'].text[0])
            listofsongs.append(files)
    
    print(listofsongs)
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()

directorychooser()
realnames.reverse()

def nextsong(event):
    global index
    index += 1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play    
    print(index)

def prevsong(event):
    global index
    index -= 1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play
    print(index)

def playsong(event):
    pygame.mixer.music.play
    print(index)

def stopsong(event):
    pygame.mixer.music.stop
    print(index)
    


label = Label(root, text="Music player")
label.pack()


listbox = Listbox(root)
listbox.pack()

for items in realnames:
    listbox.insert(0, items)

next = Button(root, text = 'Next')
next.pack()

prev = Button(root, text = 'Previous')
prev.pack()

play = Button(root, text = 'Play')
play.pack()

stop = Button(root, text = 'Stop')
stop.pack()

next.bind("<Button-1>",nextsong)
prev.bind("<Button-1>",prevsong)
play.bind("<Button-1>",playsong)
stop.bind("<Button-1>",stopsong)




# btn = Button(root, text="Select folder", command = directorychooser)

# # btn.grid(column=1, row=0)


root.mainloop()
