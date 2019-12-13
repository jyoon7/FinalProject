import os
import pygame
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askdirectory
from mutagen.id3 import ID3

# Variables
listofsongs = []
albums = []
tags = [] # Tag elements: 0 = title / 1 = performer / 2 = composer
index = 0

# Create main window
player = Tk()
player.title("Classical music player")
pygame.mixer.init()
player.minsize(300,300)



# Tabs
tab_control = ttk.Notebook(player)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab_control.add(tab1, text='Performer')
tab_control.add(tab2, text='Composer')
tab_control.pack(expand=1, fill='both')

# Frame..?
frame1 = Frame(player, relief=RAISED, borderwidth=1)
frame1.pack(fill=BOTH, expand=True)
frame2 = Frame(player, relief=RAISED, borderwidth=1)
frame2.pack(fill=BOTH, expand=True, side=BOTTOM)

# Menus
menubar = Menu(player)
player.config(menu=menubar)

subMenu = Menu(menubar, tearoff=0)

def opendir():
    global directory
    directory = askdirectory()
    os.chdir(directory)

    for files in os.listdir(directory):
        if files.endswith(".mp3"):
            realdir = os.path.realpath(files)
            audio = ID3(realdir)
            tags.append(audio['TIT2'].text[0])
            listofsongs.append(files)

    pygame.mixer.music.load(listofsongs[0])

    
    for x in tags:
        listbox2.insert(0,x)

menubar.add_cascade(label='File', menu=subMenu)
subMenu.add_command(label="Open", command=opendir)
subMenu.add_command(label="Exit", command=player.destroy) 


# Create a list of songs
listbox1 = Listbox(frame1)
listbox1.pack(padx=1, pady=0, side=LEFT)
listbox2 = Listbox(frame1)
listbox2.pack(padx=1, pady=0, side=RIGHT)



# Media buttons
def nextsong(event):
    global index
    index += 1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    print(index)

def prevsong(event):
    global index
    index -= 1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    print(index)

def playsong(event):
    pygame.mixer.music.play()
    print(index)

def stopsong(event):
    pygame.mixer.music.stop()
    print(index)

nextbutton = Button(frame2, text = 'Next')
nextbutton.pack(side = RIGHT)

prev = Button(frame2, text = 'Previous')
prev.pack(side = RIGHT)

play = Button(frame2, text = 'Play')
play.pack(side = RIGHT)

stop = Button(frame2, text = 'Stop')
stop.pack(side = RIGHT)

nextbutton.bind("<Button-1>",nextsong)
prev.bind("<Button-1>",prevsong)
play.bind("<Button-1>",playsong)
stop.bind("<Button-1>",stopsong)


# Other buttons
def booklet(event):
    os.startfile("Booklet.pdf")

openbook = Button(frame2, text = 'Booklet')
openbook.pack(side = LEFT)
openbook.bind("<Button-1>",booklet)

def score(event):
    os.startfile("score.pdf")

openscore = Button(frame2, text = 'Score')
openscore.pack(side = LEFT)
openscore.bind("<Button-1>",score)


player.mainloop()