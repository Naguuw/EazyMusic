# 🎵 KHinsider FLAC Downloader

A specialized Python script designed to scrape and download high-quality FLAC music files specifically from KHinsider.

## ✨ Features

- **KHinsider Optimized**: Specifically tailored to parse the structure of KHinsider's music directory.
- **Automatic Scanning**: Scans the provided KHinsider album/game link for all available music tracks.
- **FLAC Detection**: Automatically identifies and extracts direct links to `.flac` files.
- **Resume Capability**: Supports resuming interrupted downloads using HTTP Range requests, so you don't have to start from zero if the connection drops.
- **Smart Folder Management**: Automatically creates a designated folder for your downloads.
- **Anti-Ban Mechanism**: Implements random sleep intervals between requests to mimic human behavior and avoid IP blocks.
- **Detailed Summary**: Provides a final report of successful and failed downloads.

## 🚀 Getting Started

### Prerequisites

Make sure you have Python 3.x installed. You will need the following libraries:
- `requests`
- `beautifulsoup4`

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Naguuw/EazyMusic.git
   ```

2. **Install dependencies:**
   ```bash
   pip install requests beautifulsoup4 tqdm
   ```

### Usage

Run the script using Python:
```bash
python main.py
```


**Input required:**
- `Link Music`: The KHinsider URL of the music page you want to download.
- `Folder Name`: The name of the folder where you want to save the FLAC files.

## 🛠️ Technical Details

- **Target Site**: KHinsider
- **Language**: Python 3
- **Key Logic**: Uses `BeautifulSoup` for HTML parsing and `requests.Session` for persistent connections.

## 📝 License

This project is for personal use and educational purposes. Please use it responsibly.

