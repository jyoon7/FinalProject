# Design

# Libraries

Apart from the "os" library, the application relies on 3 libraries for its essential functions:

1. Tkinter: for creating a very simple GUI for users to interact with 
2. Pygame.mixer: for basic audio playback functions
3. Mutagen: for accessing ID3 tag information in audio files

# Interface

The interface was created using Tkinter. The main window (player) is first created, and is populated with the rest of the interface from top down.

At the top of the interface is a menu option, giving the user the option to choose a folder or exit the program.

Frames are created to organize specific elements within the player. For example, the first frame is below the menu options containing labels. The second and third frames lie directly beneath the first, and contains two listboxes to display information about songs.

All elements within the GUI are organized using the .pack method.

The listboxes are designed to be populated with information of all the songs. They are designed to expand when the window expands. 

Below the listbox is a string which displays the current song being played (empty when nothing is being played). The functionality is explained below in the Function section.

Below the now playing string is the volume slider, which is connected to the "volume" function.

The bottom of the app contains all the buttons, which are used to control media playback.

# Function

The media playback aspect of the app relies on pygame.mixer.

AFter the directory is chosen, the songs files are appended to a list. Using the global variable "Index", the app is able to navigate through all of the import songs through the media playback buttons.

Using the .bind function, all of the buttons on the bottom are connected with their respective functions 

The updating label uses StringVar(), and is set to the current song title based on the current index.

The play and pause function works using the global Paused variable. Pausing declares "paused" to be true. If the play button detects that the song has been paused, it will resume the song.

# Tag information

The tags of audio files are accessed through the mutagen library.

In the opendir() function, the app asks the user to choose a directory (using the "os" library). To pass the directory name into the ID3 function, m
