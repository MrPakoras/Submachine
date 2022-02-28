import os, time, re, mimetypes, math, threading, tkinter
from tkinter import *
from tkinter import filedialog, colorchooser, ttk
from PIL import Image as i
from PIL import ImageFilter, ImageOps, ImageDraw, ImageTk
import matplotlib
from matplotlib import pyplot as plt
import numpy as np
from tkvideo import tkvideo

bgcolour = '#1d1c2c'

master = Tk()
master.title('Submachine GUI v0.1')
master.geometry('1280x720')
# master.resizable(False, False)
master.configure(background=bgcolour)
master.columnconfigure(0, weight=2)
# icon = PhotoImage(file='./extras/icon.png')
# master.iconphoto(False, icon)

### GUI

## File selection

topframe = Frame(master, bg=bgcolour)
topframe.grid(row=0, column=0, sticky='w', padx=20, pady=15)

bottomframe = Frame(master, bg=bgcolour)
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

leftsubframe = Frame(topframe, bg=bgcolour) # Frame for video preview and controls
leftsubframe.grid(row=0, column=0, sticky='w')

# Video
bvframe = Frame(leftsubframe, width=448, bg=bgcolour) # browse video frame
bvframe.pack_propagate(0)
bvframe.grid(row=0, column=0, sticky='w')

bvlabel = Label(bvframe, text='Video File:', bg=bgcolour, fg='#d7ceff', font=('Helvetica', 18, 'bold'))
bvlabel.grid(row=0, column=0, sticky='w')

bvaddrvar = StringVar(bvframe)
bvvar = 'Please choose a video file...'
bvaddrvar.set(bvvar)

bvaddrlab = Label(bvframe, textvariable=bvaddrvar, anchor='w', width=40, bg='#1d1c2c', fg='#d7ceff')
bvaddrlab.grid(row=1, column=0, sticky='we')

bvbutton = Button(bvframe, text='Browse', command=lambda:browse('video'), width=9, bg='#1d1c2c', fg='#8d73ff', activebackground='#1d1c2c' , activeforeground='#8d73ff') # Browse video button
# Lambda function so command can be run with parameters
bvbutton.config(state='normal')
bvbutton.grid(row=1, column=1, pady=5)

mvvar = IntVar() # Mute video variable
mvvar.set(0)
mvcheck = Checkbutton(bvframe, text='Mute video', variable=mvvar, bg='#1d1c2c', fg='#8d73ff', activebackground='#1d1c2c' , activeforeground='#8d73ff') # Mute video check button
mvcheck.grid(row=2, column=0, padx=4, sticky='w')


# Breaker
leftsubframe.columnconfigure(1, weight=2)


# Audio
baframe = Frame(leftsubframe, width=448, bg=bgcolour) # Browse audio frame
baframe.pack_propagate(0)
baframe.grid(row=2, column=0)

balabel = Label(baframe, text='Audio File:', bg=bgcolour, fg='#d7ceff', font=('Helvetica', 18, 'bold'))
balabel.grid(row=0, column=0, sticky='w')

baaddrvar = StringVar(baframe)
bavar = 'Please choose an audio file...'
baaddrvar.set(bavar)

baaddrlab = Label(baframe, textvariable=baaddrvar, anchor='w', width=40, bg='#1d1c2c', fg='#d7ceff')
baaddrlab.grid(row=1, column=0, sticky='we')

babutton = Button(baframe, text='Browse', command=lambda:browse('audio'), width=9, bg='#1d1c2c', fg='#8d73ff', activebackground='#1d1c2c' , activeforeground='#8d73ff') # Browse video button
babutton.config(state='normal')
babutton.grid(row=1, column=1, pady=5)

vslider = Scale(baframe, label='Volume', from_=0, to=200, orient=HORIZONTAL, length=350, bg='#8d73ff', fg='#1d1c2c', activebackground='#8d73ff', troughcolor='#d7ceff') # volume slider
vslider.set(100)
vslider.grid(row=2, column=0)


# Breaker
leftsubframe.columnconfigure(3, weight=2)


# Subtitles
subsframe = Frame(leftsubframe, width=448, bg=bgcolour) # Subtitles frame
subsframe.pack_propagate(0)
subsframe.grid(row=4, column=0, sticky='w', pady=10)

subslabel = Label(subsframe, text='Subtitles:', bg=bgcolour, fg='#d7ceff', font=('Helvetica', 18, 'bold'))
subslabel.grid(row=0, column=0, sticky='w')


# def addsub(): # Function to create new subtitles
# 	baaddrvar = StringVar(baframe)
# 	bavar = 'Please choose an audio file...'
# 	baaddrvar.set(bavar)

# 	baaddrlab = Label(baframe, textvariable=baaddrvar, anchor='w', width=40, bg='#1d1c2c', fg='#d7ceff')
# 	baaddrlab.grid(row=1, column=0, sticky='we')

# 	babutton = Button(baframe, text='Browse', command=lambda:browse('audio'), width=9, bg='#1d1c2c', fg='#8d73ff', activebackground='#1d1c2c' , activeforeground='#8d73ff') # Browse video button
# 	babutton.config(state='normal')
# 	babutton.grid(row=1, column=1, pady=5)

subscanvas = Canvas(subsframe, bg='#d7ceff') # Canvas for subtitle buttons
subscanvas.grid(row=1, column=0, sticky='w')

addsubsbutton = Button(subsframe, text='Add', bg='#5a49a4', fg='#d7ceff', activebackground='#5a49a4', activeforeground='#d7ceff') # Add subtitles
addsubsbutton.grid(row=2, column=0, sticky='we')

# Settings
settingslabel = Label(subsframe, text='Settings:', bg=bgcolour, fg='#d7ceff', font=('Helvetica', 14))
settingslabel.grid(row=3, column=0, sticky='w')

# Sub options dropdown
solabel = Label(subsframe, text='Sub Option:', bg=bgcolour, fg='#d7ceff', font=('Helvetica', 14))
solabel.grid(row=4, column=0, sticky='w')

sovar = StringVar()
soddstyle = ttk.Style() # Style options for dropdown
soddstyle.configure('TCombobox', background='#1d1c2c', foreground='#000')

sodd = ttk.Combobox(subsframe, width=15, textvariable=sovar, style='TCombobox')
sodd['values'] = ()
sodd.grid(row=4, column=1)
sodd.state(['disabled','readonly']) # Sets dropdown on non edit mode

# sodd = # Subtitle option dropdown
# sodd.grid(row=4, column=1, sticky='w')









## Video preview and controls
rightsubframe = Frame(topframe, bg=bgcolour) # Frame for video preview and controls
rightsubframe.grid(row=0, column=1)

vidframe = Frame(rightsubframe, bg=bgcolour) # Frame for video
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