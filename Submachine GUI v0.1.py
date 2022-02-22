import os, time, re, mimetypes, math, threading, tkinter
from tkinter import *
from tkinter import filedialog, colorchooser, ttk
from PIL import Image as i
from PIL import ImageFilter, ImageOps, ImageDraw, ImageTk
import matplotlib
from matplotlib import pyplot as plt
import numpy as np
from tkvideo import tkvideo

master = Tk()
master.title('Submachine GUI v0.1')
master.geometry('1280x720')
master.resizable(False, False)
master.configure(background='#1d1c2c')
master.columnconfigure(0, weight=2)
# icon = PhotoImage(file='./extras/icon.png')
# master.iconphoto(False, icon)

### GUI

## Video Preview

# Video
master.update() # updates window to allow data to be measured
prevsize = (3*master.winfo_width()//4,3*master.winfo_width()//4//16*9)# Preview size - width = 3/4 window size, height measured to 16:9 ratio
print(master.winfo_width())

my_label = Label(master)
my_label.pack()
player = tkvideo("H:/System/Videos/Class Videos/Big 3 Groovin.mp4", my_label, loop = 1, size = prevsize)
player.play()

# Scrubber and controls


## Subtitles


### CODE


master.mainloop()