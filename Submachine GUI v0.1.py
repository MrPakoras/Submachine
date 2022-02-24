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
# master.resizable(False, False)
master.configure(background='#1d1c2c')
master.columnconfigure(0, weight=2)
# icon = PhotoImage(file='./extras/icon.png')
# master.iconphoto(False, icon)

### GUI

## File selection

topframe = Frame(master)
topframe.grid(row=0, column=0)

bottomframe = Frame(master)
bottomframe.grid(row=1, column=0)

## Browse for file function
def browse(type):
	global filename
	filename = filedialog.askopenfilename(initialdir = "/", title = "Select a File")

	if len(filename) != 0:
		if len(filename) >= 45:
			avar = filename[:45]+'...'
		else:
			avar = filename
		addrvar.set(avar)

		if mimetypes.guess_type(filename)[0].startswith(type):
			mvar = ':)'
			messvar.set(mvar)
			startbutton.config(state='normal')
			previewbutton.config(state='normal')

		else:
			startbutton.config(state='disabled')
			mvar = f'Error. Please choose an {type} file.'
			messvar.set(mvar)


## Address bar and browse button

leftsubframe = Frame(topframe) # Frame for video preview and controls
leftsubframe.grid(row=0, column=0)

# Browse Video
bvframe = Frame(leftsubframe, width=448, bg='#1d1c2c')
bvframe.pack_propagate(0)
bvframe.grid(row=0, column=0)

bvaddrvar = StringVar(bvframe)
bvvar = 'Please choose a video file...'
bvaddrvar.set(bvvar)

bvaddrlab = Label(bvframe, textvariable=bvaddrvar, anchor='w', width=40, bg='#1d1c2c', fg='#d7ceff')
bvaddrlab.grid(row=0, column=0, sticky='we')

bvbutton = Button(bvframe, text='Browse', command=lambda:browse('video'), width=9, bg='#1d1c2c', fg='#8d73ff', activebackground='#1d1c2c' , activeforeground='#8d73ff') # Browse video button
bvbutton.config(state='normal')
bvbutton.grid(row=0, column=1, pady=4)

# Browse Audio
baframe = Frame(leftsubframe, width=448, bg='#1d1c2c')
baframe.pack_propagate(0)
baframe.grid(row=1, column=0)

baaddrvar = StringVar(baframe)
bavar = 'Please choose an audio file...'
baaddrvar.set(bavar)

baaddrlab = Label(baframe, textvariable=baaddrvar, anchor='w', width=40, bg='#1d1c2c', fg='#d7ceff')
baaddrlab.grid(row=0, column=0, sticky='we')

babutton = Button(baframe, text='Browse', command=lambda:browse('audio'), width=9, bg='#1d1c2c', fg='#8d73ff', activebackground='#1d1c2c' , activeforeground='#8d73ff') # Browse video button
babutton.config(state='normal')
babutton.grid(row=0, column=1, pady=4)



## Video preview and controls
rightsubframe = Frame(topframe) # Frame for video preview and controls
rightsubframe.grid(row=0, column=1)

vidframe = Frame(rightsubframe) # Frame for video
vidframe.grid(row=0, column=0)

## Video Preview

# Video
# master.update() # updates window to allow data to be measured
# prevsize = (3*master.winfo_width()//4,3*master.winfo_width()//4//16*9)# Preview size - width = 3/4 window size, height measured to 16:9 ratio
# print(master.winfo_width())

# my_label = Label(master)
# my_label.pack()
# player = tkvideo("H:/System/Videos/Class Videos/Big 3 Groovin.mp4", my_label, loop = 1, size = prevsize)
# player.play()

# Scrubber and controls


## Subtitles


### CODE


master.mainloop()