#!/usr/bin/env python3
#
#. Downloader for Hit Songs from mp3indirdur.mobi website.
#
# downloadsong.py  by ayhanabi
# http://github/ayhanabi/mp3indirdur
# 
# pls. give credit if you modify/distribute/extend etc.
#
#  Last Update: Nov 11,2022


import os
import requests
from bs4 import BeautifulSoup
import re

url = 'https://www.mp3indirdur.mobi'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
table = soup.find_all("ul", attrs={"class": "ortaMp3lerListesi"})[3]
songs=[]
songID=[]
liste=[]
kod = re.compile(r'(\d+)')
for item in table.findAll("li"):
    songs +=  [item.text[item.text.index(' ')+1:item.text.index('(')-1]+'.mp3']
    songID += [item.a['href'][1:item.a['href'].index('-')]]
for index, (song, id) in enumerate(zip(songs,songID)):
    liste.append((f"{index+1:03d} - " + song, id))
print("Downloading ...\n")
for (song, id) in liste:
        print(song)
        response = requests.get("https://cdn103.mp3indirdur.info/indir.asp?ID="+ id +"&cdn=cdn103&linkKontrol=0", allow_redirects=True)
        downloaded_file = response.content
        if response.status_code == 200:
            with open(song, 'wb') as f:
                 f.write(response.content)
