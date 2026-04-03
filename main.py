import requests
import os
import time
import random
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

BASE_URL = input("Link Music: ")
SAVE_FOLDER = "Downloads"

os.makedirs(SAVE_FOLDER, exist_ok=True)
session = requests.Session()
headers = {
    "User-Agent": "Mozilla/5.0"
}

def get_details_links(url):
    print(f"Scanning {url}")

    music_links = set()

    try:
        res = session.get(url, headers=headers)
        if res.status_code != 200:
            print("Can't Access")
            return None
        
        soup = BeautifulSoup(res.text, "html.parser")

        rows = soup.find_all("td", class_="clickable-row")

        for row in rows:
            for a in row.find_all("a"):
                href = a.get("href")

                if href:
                    full_url = urljoin(url, href)
                    music_links.add(full_url)
                
    except Exception as e:
        print("Error:",e)

    return list(music_links)

def get_flac_link(url):
    print(f"Opening {url}")

    try:
        res = session.get(url, headers=headers)
        if res.status_code != 200:
            print("Can't Access")
            return None
        
        soup = BeautifulSoup(res.text, "html.parser")

        for a in soup.find_all("a"):
            href = a.get("href")

            if href and ".flac" in href:
                return urljoin(url, href)
        
    except Exception as e:
        print("Error:", e)

    return None


def download(url):
    filename = os.path.basename(urlparse(url).path)
    path = os.path.join(SAVE_FOLDER, filename)

    if os.path.exists(path):
        print(f"Skipping {filename}")
        return
    
    print(f"Down {filename}")

    try:
        r = session.get(url, headers=headers, stream=True)

        if r.status_code != 200:
            print("Gagal download")
            return
        
        with open(path, "wb") as f:
            for chunk in r.iter_content(1024):
                if chunk:
                    f.write(chunk)

    except Exception as e:
        print("Downloading Error", e)

def main():
    detail_links = get_details_links(BASE_URL) or []

    print(f"\nTotal pages: {len(detail_links)}\n")

    flac_links = set()

    for link in detail_links:
        flac = get_flac_link(link)

        if flac:
            print("[FLAC]", flac)
            flac_links.add(flac)

        time.sleep(random.uniform(1, 2))
    
    print(f"\nTotal FLAC: {len(flac_links)}\n")

    for flac in flac_links:
        download(flac)
        time.sleep(random.uniform(1,2))

if __name__ == "__main__":
    main()
