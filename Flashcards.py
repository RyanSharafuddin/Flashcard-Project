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

def word_changer():
    global counter
    if (counter < num_studied - 1):
        counter += 1
        name.set(mappedList[counter][0])
        #word font size - configure later
        if (len(mappedList[counter][0]) >= 9):
            word.config(font = "Verdana 75 bold", height = 8, width = 27)
        else:
            word.config(font = "Verdana 200 bold", height = 3, width = 10)
    else:
        counter = num_studied
        word.config(font = "Verdana 100 bold", height = 6, width = 20)
        name.set("End of videos")

def show_sign():
    global counter
    if (counter <= num_studied - 1):
        play(mappedList[counter][1].rstrip('\n'))

def initialize_name():
    name.set(mappedList[counter][0])
    if (len(mappedList[counter][0]) >= 9):
        word.config(font = "Verdana 75 bold", height = 8, width = 27)
    else:
        word.config(font = "Verdana 200 bold", height = 3, width = 10)

def set_mappedList():
    global mappedList
    global cTracker
    global num_studied
    global counter
    mappedList = []
    for (num,var) in enumerate(cTracker):
        if (cTracker[num].get() == 1):
            mappedList += wholeList[num]
    random.shuffle(mappedList)
    num_studied = len(mappedList)
    counter = 0
    initialize_name()
    return

def all_zeros(tracker):
    for x in tracker:
        if (x.get() == 1):
            return False
    return True

def chosen(button):
    if (all_zeros(cTracker)):
        return
    else:
        set_mappedList()
        button.win.quit()

def choose_units():
    popup = Tkinter.Toplevel()
    prompt = Tkinter.Label(popup,
                           text = "Choose a non-empty subset of units to study:")
    prompt.pack()
    for (num,unit) in enumerate(unit_names):
        check = Tkinter.Checkbutton(master = popup, text = unit, variable = cTracker[num])
        check.pack()
    done = Tkinter.Button(popup, text = "Done", command = lambda: chosen(done))
    done.pack()
    done.win = popup
    popup.focus_set()
    popup.grab_set()
    popup.mainloop()
    popup.destroy()
    
counter = 0
cTracker = [] #list of IntVars to keep track of checkboxes

#'C:\Users\Carrie\Documents\ASL Study App\Word List.txt'
wordFile = open('file.txt', 'r+')
unit_index = -1
wordList = []
unit_names = []
for line in wordFile:
    if ((line[0] == ":")):
        wordList.append([])
        unit_index += 1
        unit_names.append(line[1:])
    else:
        wordList[unit_index].append(line)
wordFile.close()
words_per_unit = []
for unit in wordList:
    words_per_unit.append(len(unit))

#'C:\Users\Carrie\Documents\ASL Study App\Video List.txt'
videoFile = open('vid.txt', 'r+')
unit_index = -1
videoList = []
for line in videoFile:
    if ((line[0] == ":")):
        videoList.append([])
        unit_index += 1
    else:
        videoList[unit_index].append(line)
videoFile.close()
vids_per_unit = []
for unit in videoList:
    vids_per_unit.append(len(unit))


if(not(len(vids_per_unit) == len(words_per_unit))):
    print ("Warning: Unequal numbers of video and word units")
else:
    for i in range(len(words_per_unit)):
        if(not(words_per_unit[i] == vids_per_unit[i])):
            print ("Warning: Unequal numbers of words and videos in unit " + unit_names[i])

#NOTE: This assumes the number of videos is less than or equal to the number of words
unit_index = -1
wholeList = []
for unit in (videoList):
    wholeList.append([])
    unit_index += 1
    for i in range(len(unit)):
        wholeList[unit_index].append((wordList[unit_index][i], videoList[unit_index][i]))

mappedList = []

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
for (num, unit) in enumerate(wholeList):
    cTracker.append(Tkinter.IntVar())
    cTracker[num].set(1)
set_mappedList()

#Macs don't allow you to change the colors of a button, but Windows does.
show = Tkinter.Button(root, text = "Show sign",
                      command = show_sign,
                      font = "Verdana 50", relief = "raised",
                      fg = "green", bg = "blue")
show.pack()
show.place(relheight = .2, relwidth = .4, relx = 0, rely =.8)

change = Tkinter.Button(root, text = "Next",
                        command = word_changer,
                        font = "Verdana 50", relief = "flat",
                        fg = "green", bg = "blue")
change.pack()
change.place(relheight = .2, relwidth = .4, relx = .4, rely = .8)

set_units = Tkinter.Button(root, text = "Set units",
                           font = "Verdana 50", command = choose_units,
                           fg = "green", bg = "blue")
set_units.pack()
set_units.place(relheight = .2, relwidth = .2, relx = .8, rely = .8)

#Call .destroy on a widget to get rid of it.
#Call .pack_forget to remove it temporarily; then call .pack() to restore it


root.mainloop()
#Other Features:
#1) Toggle video/word first during use (use radio buttons)
#2) Be able to use images as well as words on the label
#3) Quiz on units
