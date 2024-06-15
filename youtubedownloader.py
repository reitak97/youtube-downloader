from pytube import YouTube
import tkinter as tk
from tkinter import filedialog


def download_video(url,savepath):
    try:
        yt = YouTube(url)
        streams =yt.streams.filter(progressive=True, file_extension='mp4')
        highest_res_stream = streams.get_highest_resolution()
        highest_res_stream.download(output_path=savepath)
        print('Downloaded Successfully')
    
    except Exception as e:
        print(e)


url = "https://www.youtube.com/watch?v=UueWuIMTte0&list=RDUueWuIMTte0&start_radio=1&ab_channel=lunar"
save_path = "C:/Users/Reita/Downloads"
download_video(url,save_path)
