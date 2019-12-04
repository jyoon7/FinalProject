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

btn = Button(root, text="Select folder", command = directorychooser)

btn.grid(column=3, row=1)


root.mainloop()