# 🎵 FLAC Music Downloader

A lightweight Python script to scrape and download high-quality FLAC music files from a given music directory link.

## ✨ Features

- **Automatic Scanning**: Scans the provided base URL for all available music detail pages.
- **FLAC Detection**: Automatically identifies and extracts direct links to `.flac` files.
- **Resume Capability**: Supports resuming interrupted downloads using HTTP Range requests, preventing redundant data usage.
- **Smart Folder Management**: Automatically creates a designated folder to store your downloaded music.
- **Anti-Ban Mechanism**: Implements random sleep intervals between requests to avoid being blocked by the server.
- **Detailed Summary**: Provides a final report of successful and failed downloads.

## 🚀 Getting Started

### Prerequisites

Make sure you have Python 3.x installed on your system. You will also need the `requests` and `beautifulsoup4` libraries.

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Naguuw/EazyMusic.git
   ```

2. **Install dependencies:**
   ```bash
   pip install requests beautifulsoup4
   ```

### Usage

Run the script using Python:
```bash
bash python main.py
```

**Input required during execution:**
- `Link Music`: The URL of the music directory you want to scan.
- `Folder Name`: The name of the folder where the FLAC files will be saved.

## 🛠️ Technical Details

- **Language**: Python 3
- **Libraries used**: 
  - `requests`: For handling HTTP requests and session management.
  - `BeautifulSoup4`: For parsing HTML content.
  - `os`, `time`, `random`: For system operations and request throttling.
  - `urllib.parse`: For URL manipulation and decoding.

## 📝 License

This project is for educational purposes. Please use it responsibly.

