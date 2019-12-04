import os
import pygame
from tkinter import *
from tkinter.filedialog import askdirectory

root = Tk()
root.title("Music Player")
root.minsize(300,300)

listofsongs = []

def directorychooser():
    directory = askdirectory()
    os.chdir(directory)

    for files in os.listdir(directory):
        if files.endswith(".mp3"):
            listofsongs.append(files)
    
    print(listofsongs)
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(listofsongs[0])
    pygame.mixer.music.play()

directorychooser()


label = Label(root, text="Music player")
label.pack()


listbox = Listbox(root)
listbox.pack()

for items in listofsongs:
    listbox.insert(0, items)

next = Button(root, text = 'Next')
next.pack()

prev = Button(root, text = 'Previous')
prev.pack()

stop = Button(root, text = 'Stop')
stop.pack()


# btn = Button(root, text="Select folder", command = directorychooser)

# # btn.grid(column=1, row=0)


root.mainloop()
