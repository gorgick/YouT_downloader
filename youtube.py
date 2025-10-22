from pytubefix import YouTube
from pytubefix.cli import on_progress

if __name__ == '__main__':
    url = "https://www.youtube.com/watch?v=J0Aq44Pze-w"

    yt = YouTube(url, on_progress_callback=on_progress)
    print(yt.title)

    ys = yt.streams.get_highest_resolution()
    ys.download()
