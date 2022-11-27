import sys
import os
import requests
from bs4 import BeautifulSoup
import re

if len(sys.argv)>=2:
    singerID=sys.argv[1]
else: 
    print("SingerID is needed")
    print(len(sys.argv))
    exit(1)
count=1
 
while count>0 :  
    url ='https://www.mp3indirdur.mobi/'+str(singerID)+'-'+str(count)+'-sanatci-sarkilari-cem-karaca-indir.html'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    table = soup.find_all("li") #, attrs={"class": "sayiRenk"}
    songs=[]
    songID=[]
    liste=[]
    for item in table:
        if item.find("span") is not None:
            atag=item.find("a", href=True)
            songs += [atag.text]
            songID += [atag['href'][1:][:atag['href'][1:].index("-")]] 
    for index, (song, id) in enumerate(zip(songs,songID)):
        liste.append((song+".mp3", id))
#   print("Downloading ...\n")
    for (song, id) in liste:
        print(song)
        response = requests.get("https://cdn103.mp3indirdur.info/indir.asp?ID="+ id +"&cdn=cdn103&linkKontrol=0", allow_redirects=True)
        if response.status_code == 200:
             with open(song, 'wb') as f:
                f.write(response.content)
    if soup.find("li", {"id": "sonrakiSayfa"}) is not None:
         count += 1
    else: 
         count=0

