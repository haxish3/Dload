# PyDload

A lightweight video downloader using `yt-dlp`, with a simple CustomTkinter GUI. This repository includes a basic GUI, a redesigned interface in `gui.py`.

## Features

- Download videos using a URL
- Select output folder through a folder picker
- Uses a separate thread for downloads to keep the UI responsive
- Simple and clean interface with modern spacing and status feedback

## Requirements

- Python 3.10+
- `yt-dlp`
- `customtkinter`

Install dependencies with:

```bash
pip install -r requirements.txt
```

## Usage

### Run the GUI

```bash
python gui.py
```

### Run the CLI (not now)

```bash
python cli.py
```

## Output path behavior

- If you do not select a path, the downloaded video saves to the current working folder.
- Use the `Select path` button to choose a custom destination.

## Notes

- The app validates the URL and expects `http://` or `https://`.
- Download happens in a background thread so the interface stays responsive.

## License

Use and modify freely.
