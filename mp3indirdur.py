#!/usr/bin/env python3
#
#. Downloader for Top 100 Turkish Hit Songs from mp3indirdur.mobi website.
#
# mp3indirdur.py  by ayhanabi
# http://github/ayhanabi/mp3indirdur
# 
# pls. give credit if you modify/distribute/extend etc.
#
#  Last Update: May 19,2022


import os
import requests
from bs4 import BeautifulSoup
import re

url = 'https://www.mp3indirdur.mobi/hit-mp3ler.asp'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
table = soup.find("div", attrs={"class": "ortaSolBlokIcerik"})
table_data  = table.ul.find_all("li")
print("Collecting Song Ids ...")
songs={}
for index, table in enumerate(table_data):
   if index ==0: continue
   try:
      songkod = re.compile(r'\d+')
      adres=table.a['href']
      out=songkod.search(adres)
   except: continue
   songs[out.group()]= f"{index:03d} - "+ str(table.a.contents[0])+'.mp3'
print("Downloading ...\n")
for songId in songs:
        print(f"{songs[songId]}")
        response = requests.get("https://cdn103.mp3indirdur.info/indir.asp?ID="+ songId +"&cdn=cdn103&linkKontrol=0", allow_redirects=True)
        downloaded_file = response.content
        if response.status_code == 200:
            with open(songs[songId], 'wb') as f:
                 f.write(response.content)
            
