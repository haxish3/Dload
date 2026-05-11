from threading import Thread
import yt_dlp


def download(url, opts):

    with yt_dlp.YoutubeDL(opts) as ydl:
        ydl.download([url])


retry = False

while True:
    url = input(f"{'Tente novamente: ' if retry else 'url: '}")
    if url == "quit":
        break

    ydl_opts = {"format": "best", "quiet": True}

    try:
        Thread(target=download, args=(url, ydl_opts)).start()
        print("Cole outra url se quiser!")
        
    except yt_dlp.utils.DownloadError:
        print(f"'{url}' nao e uma url valida")
        retry = True
