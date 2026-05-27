import requests
import os
import time
import random
from tqdm import tqdm
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse, unquote

BASE_URL = input("Link Music: ")
SAVE_FOLDER = input("Folder Name: ")

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
    print(f"[OPEN] {url}")

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
    filename = unquote(filename).strip()
    path = os.path.join(SAVE_FOLDER, filename)

    temp_size = 0

    if os.path.exists(path):
        temp_size = os.path.getsize(path)
    
    headers_range = headers.copy()
    if temp_size > 0:
        headers_range["Range"] = f"bytes={temp_size}-"
        print(f"Resuming {filename} from {temp_size} bytes")
    else:
        print(f"Download {filename}")

    try:
        r = session.get(url, headers=headers_range, stream=True, timeout=10)

        if r.status_code not in (200, 206):
            print("Download Failed")
            return
        
        total_size = int(r.headers.get('content-length', 0)) + temp_size
        mode = "ab" if temp_size > 0 else "wb"

        with open(path, mode) as f, tqdm(
            total=total_size, 
            unit='iB', 
            unit_scale=True, 
            unit_divisor=1024, 
            initial=temp_size, 
            desc=filename
        ) as bar:
            for chunk in r.iter_content(8192):
                if chunk:
                    f.write(chunk)
                    bar.update(len(chunk))
        
        return True

    except Exception as e:
        print("Downloading Error", e)
        return False

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

    success = []
    failed = []

    for i, flac in enumerate(flac_links, start=1):
        print(f"\n[{i}/{len(flac_links)}]")

        result = download(flac)

        if result:
            success.append(flac)
        else:
            failed.append(flac)

        time.sleep(random.uniform(1,2))
    
    print("\n== History ==")
    print(f"Total: {len(flac_links)}")
    print(f"Success: {len(success)}")
    print(f"Failed: {len(failed)}")

    if failed:
        print("\nFailed Files: ")
        for f in failed:
            print("-", os.path.basename(urlparse(f).path))

if __name__ == "__main__":
    main()
