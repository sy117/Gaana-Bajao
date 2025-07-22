import os
import requests
from bs4 import BeautifulSoup
import webbrowser
import re

# set proxy if working in college
# os.environ["HTTPS_PROXY"] = "https://user_name:password@proxy:port"

yt_url = 'https://www.youtube.com'

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
}

def play_video(song_name):
    url = f"https://www.youtube.com/results?search_query={song_name.replace(' ', '+')}"
    print("url = ", url)
    try:
        source_code = requests.get(url, headers=HEADERS, timeout=10)
        plain_text = source_code.text
    except Exception as e:
        print(f"Error fetching YouTube: {e}")
        return

    # Use regex to find video links
    video_ids = re.findall(r'"videoId":"([^"]+)"', plain_text)
    if not video_ids:
        print("No video results found.")
        return
    video_url = f"{yt_url}/watch?v={video_ids[0]}"
    print(f"Opening: {video_url}")
    webbrowser.open(video_url)

def play_audio(song_name):
    url = f'https://gaana.com/search/{song_name.replace(" ", "%20")}'
    try:
        source_code = requests.get(url, headers=HEADERS, timeout=10)
        plain_text = source_code.content
    except Exception as e:
        print(f"Error fetching Gaana: {e}")
        return
    soup = BeautifulSoup(plain_text, "html.parser")
    # Try to find the first song link
    link = soup.find('a', href=re.compile(r'/song/'))
    if not link or not link.get('href'):
        print("No audio results found.")
        return
    audio_url = f"https://gaana.com{link['href']}"
    print(f"Opening: {audio_url}")
    webbrowser.open(audio_url)

if __name__ == "__main__":
    song_type = input('Audio or Video ? : ')
    song = input('Enter Song Name : ')
    song_type = song_type.lower()
    if 'audio' in song_type:
        play_audio(song)
    else:
        play_video(song)
