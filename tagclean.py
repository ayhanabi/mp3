# Removes "www.mp3indirdur.com" text from mp3 id3 tags.

import os
from mutagen.easyid3 import EasyID3
for x in os.listdir():
    if x.endswith(".mp3"):
        tags = EasyID3(x)
        try: 
            title = tags['title'][0]
            if title.find("|")>0:
                tags['title'] =  title[:title.find(" |")]
        except:
            tags['artist']=[""]
        tags.save()
