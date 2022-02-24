# Add video file
# Optional audio file
# Subtitle files

import moviepy, os, time, re, mimetypes, threading
import moviepy.editor as mp
import moviepy.video.fx.all as vfx
from PIL import Image, ImageOps
from datetime import datetime
from moviepy.editor import ImageClip

vidfile = '/test/vidfile.mp4'
audiofile = '/test/audio.mp3'
subfile = '/test/subfile.txt'

vc = mp.VideoFileClip(vidfile) # Moviepy video clip

audioclip = mp.AudioFileClip(song)
audioclip = audioclip.set_start(t=0)

# vac = mp.CompositeAudioClip([audioclip]) # Video and audio clip

fv = mp.CompositeVideoClip([vc, finalfr]) # Final video