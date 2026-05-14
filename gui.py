import customtkinter as ck
from threading import Thread
from tkinter import filedialog
import yt_dlp
import os


def task_download():
    app.after(
        0,
        d_btn.configure,
        text="⬇ Downloading...",
        text_color="#FFFFFF",
        fg_color="#475569",
        hover_color="#475569",
        state="disabled",
    )

    url = entry.get()
    if not url.startswith(("http://", "https://")):
        app.after(
            0,
            d_btn.configure,
            text="✗ Invalid URL",
            text_color="#ffffff",
            fg_color="#EF4444",
            hover_color="#EF4444",
            state="normal",
        )
        norm_btn()
        return

    folder = path_var.get()
    if folder and folder != get_default_path():
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
                text="✓ Finished!",
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
            text="✗ Try Again",
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
        path_label.configure(text_color="#10B981")


def get_default_path():
    return os.getcwd()


def norm_btn():
    app.after(
        2000,
        d_btn.configure,
        text="⬇ Fetch Content",
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
app.geometry("550x420")

path_var = ck.StringVar(value=f"📁 {get_default_path()}")

main = ck.CTkFrame(app, fg_color="transparent")
main.pack(expand=True, padx=20, pady=20)

title_label = ck.CTkLabel(main, text="PyDload", font=("Roboto", 28, "bold"))
title_label.pack(pady=(10, 5))

subtitle = ck.CTkLabel(
    main,
    text="Download videos from any platform",
    font=("Roboto", 11),
    text_color="gray",
)
subtitle.pack(pady=(0, 25))

url_frame = ck.CTkFrame(main, fg_color="transparent")
url_frame.pack(fill="x", pady=10)

url_label = ck.CTkLabel(url_frame, text="Media URL", font=("Roboto", 12, "bold"))
url_label.pack(anchor="w", padx=5, pady=(0, 5))

entry = ck.CTkEntry(
    url_frame, width=500, height=40, placeholder_text="https://...", font=("Roboto", 12)
)
entry.pack(padx=5)

d_btn = ck.CTkButton(
    main,
    text="⬇ Fetch Content",
    command=download,
    width=220,
    height=45,
    fg_color="#2E75E7",
    hover_color="#1A58DD",
    text_color="#FFFFFF",
    font=("Roboto", 13, "bold"),
    cursor="hand2",
)
d_btn.pack(pady=20)

path_frame = ck.CTkFrame(main, fg_color="#1a1a1a", corner_radius=8)
path_frame.pack(fill="x", pady=(5, 10), padx=5)

path_header = ck.CTkLabel(
    path_frame,
    text="Download Location",
    font=("Roboto", 11, "bold"),
)
path_header.pack(anchor="w", padx=10, pady=(8, 2))

path_label = ck.CTkLabel(
    path_frame,
    textvariable=path_var,
    font=("Roboto", 10),
    text_color="gray",
    wraplength=480,
    anchor="w",
    justify="left",
)
path_label.pack(anchor="w", padx=10, pady=(0, 8))

path_btn = ck.CTkButton(
    main,
    text="📁 Change Folder",
    command=select_path,
    width=140,
    height=32,
    fg_color="#2a2a2a",
    hover_color="#3a3a3a",
    text_color="#FFFFFF",
    font=("Roboto", 11),
    cursor="hand2",
)
path_btn.pack()

app.mainloop()
