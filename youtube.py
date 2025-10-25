from pytubefix import YouTube
from pytubefix.cli import on_progress

import tkinter as tk
from tkinter import filedialog


def download_video(url, output_path):
    try:
        yt = YouTube(url, on_progress_callback=on_progress)
        print(yt.title)
        ys = yt.streams.get_highest_resolution()
        ys.download(output_path=output_path)
        print('Downloaded')
    except Exception as e:
        print(e)


def open_file_dialog():
    folder = filedialog.askdirectory()
    if folder:
        print(f"Selected folder {folder}")
    return folder


if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()
    video_url = input("Enter a youtube-video url: ")
    save_dir = open_file_dialog()
    if save_dir:
        print("Started download")
        download_video(video_url, save_dir)
    else:
        print("Select a directory for folder")
