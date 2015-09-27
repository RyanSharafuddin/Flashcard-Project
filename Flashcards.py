import os, sys, subprocess, Tkinter

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


l = "~/Desktop/Non School Code/Python Stuff/Name.mp4"

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
name.set("Name")

#Macs don't allow you to change the colors of a button, but Windows does.
show = Tkinter.Button(root, text = "Show sign",
                      command = lambda: play(get_filename(l)),
                      font = "Verdana 50", relief = "raised",
                      fg = "green", bg = "blue")
show.pack()
show.place(relheight = .2, relwidth = .5, relx = 0, rely =.8)
# I've no idea why the button has that annoying rectangle thing. Maybe
#it doesn't on Windows??

#Make your own class that extends button with a filepath that you can
#change for the show button.
change = Tkinter.Button(root, text = "Next",
                        command = lambda: name.set("Changed!"),
                        font = "Verdana 50", relief = "flat",
                        fg = "green", bg = "blue")
change.pack()
change.place(relheight = .2, relwidth = .5, relx = .5, rely = .8)

#Call .destroy on a widget to get rid of it.


root.mainloop()






#Other Features:
#1) Toggle video/word first during use (use radio buttons)
#2) Have the ability to choose a subset of units to cover (checklist buttons)
#   and change during use
#3) Be able to use images as well as words on the label
#4) Quiz on units
#ASK ABOUT SEEN BEFORE 
