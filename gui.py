import customtkinter as ck
from threading import Thread
from tkinter import filedialog
import yt_dlp


def task_download():
    app.after(
        0,
        d_btn.configure,
        text="Downloading...",
        text_color="#1A1A1A",
        fg_color="#475569",
        hover_color="#475569",
        state="disabled",
    )

    url = entry.get()
    if not url.startswith(("http://", "https://")):
        app.after(
            0,
            d_btn.configure,
            text="Invalid URL",
            text_color="#ffffff",
            fg_color="#EF4444",
            hover_color="#EF4444",
            state="normal",
        )
        norm_btn()

        return

    folder = path_var.get()
    if folder:
        opts = {
            "format": "best",
            "quiet": True,
            "outtmpl": f"{folder}/%(title)s.%(ext)s",
        }
    else:
        opts = {"format": "best", "quiet": True}

    try:
        with yt_dlp.YoutubeDL(opts) as dl:
            dl.download([url])
            app.after(
                0,
                d_btn.configure,
                text="Finished!",
                text_color="#ffffff",
                fg_color="#10B981",
                hover_color="#10B981",
                state="normal",
            )
            norm_btn()
    except yt_dlp.utils.DownloadError:
        app.after(
            0,
            d_btn.configure,
            text="Try Again",
            text_color="#ffffff",
            fg_color="#EF4444",
            hover_color="#EF4444",
            state="normal",
        )
        norm_btn()


def select_path():
    path_name = filedialog.askdirectory()
    if path_name:
        path_var.set(path_name)


def norm_btn():
    app.after(
        2000,
        d_btn.configure,
        text="Fetch Content",
        text_color="#FFFFFF",
        fg_color="#2E75E7",
        hover_color="#1A58DD",
        state="normal",
    )
    app.after(2000, to_clear)


def download():
    Thread(target=task_download).start()


def to_clear():
    entry.delete(0, "end")


app = ck.CTk()
app.title("PyDload v1.0")
app.geometry("500x350")

path_var = ck.StringVar()

main = ck.CTkFrame(app, fg_color="transparent")
main.pack(expand=True)

title_label = ck.CTkLabel(main, text="PyDload", font=("Roboto", 24, "bold"))
title_label.pack(padx=10, pady=(30, 20))

d_label = ck.CTkLabel(main, text="Paste Media URL:", font=("Roboto", 12))
d_label.pack(padx=10, pady=(10, 0))

entry = ck.CTkEntry(main, width=350, placeholder_text="https://...")
entry.pack(padx=30, pady=(10, 0))

d_btn = ck.CTkButton(
    main,
    text="Fetch Content",
    command=download,
    width=200,
    height=40,
    fg_color="#2E75E7",
    hover_color="#1A58DD",
    text_color="#FFFFFF",
    cursor="hand2",
)
d_btn.pack(padx=10, pady=20)

path_label = ck.CTkLabel(
    main, textvariable=path_var, font=("Roboto", 10), wraplength=400
)
path_label.pack(padx=10, pady=(5, 0))
path_btn = ck.CTkButton(
    main,
    text="Select Path",
    command=select_path,
    width=100,
    height=20,
    fg_color="#2E75E7",
    hover_color="#1A58DD",
    text_color="#FFFFFF",
    cursor="hand2",
)
path_btn.pack(padx=5)

app.mainloop()
