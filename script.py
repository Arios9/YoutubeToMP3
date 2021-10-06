from pytube import YouTube
from moviepy.editor import *
import os  
from pathlib import Path

while True:
    try:
        url = str(input("Enter your Link or 0 to exit: "))
        if url == "0": break
        yt = YouTube(url)
        stream = yt.streams.filter(only_audio=True).get_by_itag(140)
        downloadPath = os.path.join(Path.home(), "Downloads")
        stream.download(output_path=downloadPath, filename=yt.title+".mp3")
        print("file downloaded successfully!")
    except:
        print("Error")