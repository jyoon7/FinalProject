import os
import pygame
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askdirectory
from mutagen.id3 import ID3

# Variables
songs = []
title = []
composer = [] 
# performer = []
index = 0


# Create main window
player = Tk()
player.title("Classical music player")
pygame.mixer.init()
# player.minsize(300,300)


# Labels
frame = Frame(player)
frame.pack()
lblComposer = Label(frame, text="Composer")
lblComposer.pack(side=LEFT)
lblPiece = Label(frame, text="Piece")
lblPiece.pack(side=RIGHT)


# Frame
frame1 = Frame(player)
frame1.pack(fill=BOTH, expand=True)
frame2 = Frame(player)
frame2.pack(fill=BOTH, expand=True, side=BOTTOM)

# Displays currently playing song
v = StringVar()
nowplaying = Label(player, textvariable=v, width=50)
nowplaying.pack()


# Menus
menubar = Menu(player)
player.config(menu=menubar)

subMenu = Menu(menubar, tearoff=0)

def opendir(): # Choose folder with songs
    global directory
    directory = askdirectory()
    os.chdir(directory)

    for files in os.listdir(directory):
        if files.endswith(".mp3"):
            realdir = os.path.realpath(files)
            audio = ID3(realdir)
            # Append ID3 tag information into the respective lists
            title.append(audio['TIT2'].text[0]) 
            composer.append(audio['TPE1'].text[0])
            songs.append(files)

    pygame.mixer.music.load(songs[0])
    
    
    for x in title: # insert ID3 lists into the listbox
        listbox2.insert(0,x)
    for x in composer:
        listbox1.insert(0,x)


menubar.add_cascade(label='File', menu=subMenu)
subMenu.add_command(label="Open", command=opendir)
subMenu.add_command(label="Exit", command=player.destroy) 


# Create a list of songs
listbox1 = Listbox(frame1)
listbox1.pack(expand=True, fill=BOTH, side=LEFT)
listbox2 = Listbox(frame1)
listbox2.pack(expand=True, fill=BOTH, side=RIGHT)



# Update labels
def updatelabel(): # updates currently playing song
    global index
    v.set(title[index])

# Define and pack media buttons
def nextsong(event):
    global index
    index += 1
    pygame.mixer.music.load(songs[index])
    pygame.mixer.music.play()
    updatelabel()

def prevsong(event):
    global index
    index -= 1
    pygame.mixer.music.load(songs[index])
    pygame.mixer.music.play()
    updatelabel()

def playsong(event):
    global paused
    if paused:
        pygame.mixer.music.unpause()
        paused = FALSE

    else:
        pygame.mixer.music.play()
        paused = 0
    updatelabel()


def pausesong(event):
    global paused
    pygame.mixer.music.pause()
    paused = TRUE

def stopsong(event):
    pygame.mixer.music.stop()
    v.set("")

def volume(val):
    volume = int(val) / 100
    pygame.mixer.music.set_volume(volume)

# Insert buttons into window
nextbutton = Button(frame2, text = 'Next')
nextbutton.pack(side = RIGHT)

prev = Button(frame2, text = 'Previous')
prev.pack(side = RIGHT)

play = Button(frame2, text = 'Play')
play.pack(side = RIGHT)

pause = Button(frame2, text = 'Pause') 
pause.pack(side = RIGHT)

stop = Button(frame2, text = 'Stop')
stop.pack(side = RIGHT)

nextbutton.bind("<Button-1>",nextsong)
prev.bind("<Button-1>",prevsong)
play.bind("<Button-1>",playsong)
pause.bind("<Button-1>",pausesong)
stop.bind("<Button-1>",stopsong)

scale = Scale(player, from_=0, to=100, orient=HORIZONTAL, command=volume)
scale.set(70)
pygame.mixer.music.set_volume(70)
scale.pack()


# Other buttons
def booklet(event): # Opens the album booklet
    os.startfile("Booklet.pdf")

openbook = Button(frame2, text = 'Booklet')
openbook.pack(side = LEFT)
openbook.bind("<Button-1>",booklet)

def score(event): # Opens the score
    os.startfile("score.pdf")

openscore = Button(frame2, text = 'Score')
openscore.pack(side = LEFT)
openscore.bind("<Button-1>",score)


player.mainloop()