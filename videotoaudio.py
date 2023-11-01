from moviepy.editor import *
import subprocess

# videoclip = VideoFileClip("speech.mp4")
audio=AudioFileClip("4mins.mp4")
newsound = audio.subclip("00:00:00","00:03:40")   
newsound.write_audiofile("example.wav", 44100, 2, 2000,"pcm_s32le")

subprocess.run(["python", "speechtotext.py"])
# audioclip = videoclip.audio
# audioclip.write(("example.wav", 44100, 2, 2000,"pcm_s32le"))