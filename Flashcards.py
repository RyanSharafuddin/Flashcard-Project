import os, sys, subprocess, Tkinter, random

def play(filename):
    """This should work on both Windows and Mac OS"""
    if sys.platform == "win32":
        os.startfile(filename)
    else:
        opener ="open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, filename])

def get_filename(s):
    """This only works on Mac OS; have to look up how to do it on
Windows"""
    return(os.path.expanduser(s))

counter = 0

def word_changer():
    global counter
    if (counter < numVids):
        counter += 1
        name.set(mappedList[counter][0])
        #word font size - configure later
        if (len(mappedList[counter][0]) >= 9):
            word.config(font = "Verdana 75 bold", height = 8, width = 27)
        else:
            word.config(font = "Verdana 200 bold", height = 3, width = 10)
    else:
        word.config(font = "Verdana 100 bold", height = 6, width = 20)
        name.set("End of videos")

def show_sign():
    global counter
    if (counter < numVids):
        play(mappedList[counter][1].rstrip('\n'))
    else:
        word.config(font = "Verdana 100 bold", height = 6, width = 20)
        name.set("End of videos")

#wordList and videoList are currently single lists; eventually make
#them lists of lists corresponding to units
wordFile = open('C:\Users\Carrie\Documents\ASL Study App\Word List.txt', 'r+')
wordList = []
for line in wordFile:
    if (not(line[0] == ":")):
        wordList.append(line)
numWords = len(wordList)

videoFile = open('C:\Users\Carrie\Documents\ASL Study App\Video List.txt', 'r+')
videoList = []
for line in videoFile:
    if (not(line[0] == ":")):
        videoList.append(line)
numVids = len(videoList)
if (not(numVids == numWords)):
    print "Warning: unequal numbers of videos and words"

#List of tuples; eventually a list of lists of tuples for units
#NOTE: This assumes the number of videos is less than or equal to the number of words
mappedList = []
for i in range(len(videoList)):
    mappedList.append((wordList[i], videoList[i]))

random.shuffle(mappedList)




root = Tkinter.Tk()
#Code to add all the widgets and stuff

#NOTE: height and width are in terms of letters, so it's dependent
#on the font size (for text Labels)

#NOTE: I've no idea what fonts and colors are available; look this up
# if you wish. Colors can also be specified in RGB values using this:
# tk_rgb = "#%02x%02x%02x" % (128, 192, 200)
name = Tkinter.StringVar()
word = Tkinter.Label(root, textvariable = name, height = 3, width = 10,
                     font = "Verdana 200 bold", fg = "orange",
                     bg = "black")
word.pack()
name.set(mappedList[counter][0])

#Macs don't allow you to change the colors of a button, but Windows does.
show = Tkinter.Button(root, text = "Show sign",
                      command = show_sign,
                      font = "Verdana 50", relief = "raised",
                      fg = "green", bg = "blue")
show.pack()
show.place(relheight = .2, relwidth = .5, relx = 0, rely =.8)

change = Tkinter.Button(root, text = "Next",
                        command = word_changer,
                        font = "Verdana 50", relief = "flat",
                        fg = "green", bg = "blue")
change.pack()
change.place(relheight = .2, relwidth = .5, relx = .5, rely = .8)

#Call .destroy on a widget to get rid of it.
#Call .pack_forget to remove it temporarily; then call .pack() to restore it


root.mainloop()
#Other Features:
#1) Toggle video/word first during use (use radio buttons)
#2) Have the ability to choose a subset of units to cover (checklist buttons)
#   and change during use
#3) Be able to use images as well as words on the label
#4) Quiz on units
#ASK ABOUT SEEN BEFORE 
