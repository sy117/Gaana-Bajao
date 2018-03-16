import os
import requests
from bs4 import BeautifulSoup
import webbrowser

# set proxy if working in college
os.environ["HTTPS_PROXY"] = "https://ipg_2014117:suNIL121@192.168.1.107:3128"

yt_url = 'https://www.youtube.com'


def play_video(song_name):
    url = "https://www.youtube.com/results?search_query="
    tmp = song_name.replace(' ', '+')
    url = url + tmp
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'html.parser')

    url_list = []
    for link in soup.findAll('a', {'dir': "ltr"}):
        href = link.get('href')
        if '/watch?' in href:
            url_list.append(href)
    webbrowser.open(yt_url + url_list[0])


def play_audio(song_name):
    song_name = song_name.replace(' ', '%20')
    url = 'https://gaana.com/search/{}'.format(song_name)
    source_code = requests.get(url)
    plain_text = source_code.content
    soup = BeautifulSoup(plain_text, "html.parser")
    links = soup.find_all('a', {'class': 'rt_arw'})
    webbrowser.open(links[0]['href'])


song_type = input('Audio or Video ? : ')
song = input('Enter Song Name : ')
song_type = song_type.lower()
if 'audio' in song_type:
    play_audio(song)
else:
    play_video(song)
