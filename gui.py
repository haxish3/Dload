import customtkinter as ck
from threading import Thread
import yt_dlp


def task_download():
    url = entry.get()
    if not url.startswith("https://"):
        return
    opts = {"format": "best", "quiet": True}

    try:
        with yt_dlp.YoutubeDL(opts) as dl:
            dl.download([url])
    except yt_dlp.utils.DownloadError as e:
        print(f"Error: {e}")


def download():
    Thread(target=task_download).start()


app = ck.CTk()

app.title("PyDload v1.0")
app.geometry("500x350")

main = ck.CTkFrame(app, fg_color="transparent")
main.pack(expand=True)

title_label = ck.CTkLabel(main, text="PyDload", font=("Roboto", 24, "bold"))
title_label.pack(padx=10, pady=(30, 20))

d_label = ck.CTkLabel(main, text="Paste Media URL:", font=("Roboto", 12))
d_label.pack(padx=10, pady=(10, 0))

entry = ck.CTkEntry(main, width=350, placeholder_text="https://...")
entry.pack(padx=30, pady=10)

d_btn = ck.CTkButton(
    master=main,
    text="Fetch Content",
    command=download,
    width=200,
    height=40,
    fg_color="green",
    hover_color="darkgreen",
    cursor="hand2",
)
d_btn.pack(padx=10, pady=20)

app.mainloop()
