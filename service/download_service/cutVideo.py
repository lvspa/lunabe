from moviepy import *
import os

#arquivo teste!
def cutFrame():
    cut = VideoFileClip('Remember Me (Full Version) - d4vd  ｜ Arcane Season 2 [rTVRGEEczhU].mp4').subclipped(0, 9)
    os.chdir('/home/Alexandre/Vídeos/recortes_lunabe/')
    cut.write_videofile('Remember Me (Full Version) - d4vd  ｜ Arcane Season 2 [rTVRGEEczhU].mp4', fps=30)


