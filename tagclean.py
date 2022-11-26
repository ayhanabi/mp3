# Removes "www.mp3indirdur.com" text from mp3 id3 tags.

import os
from mutagen.easyid3 import EasyID3
for x in os.listdir():
    if x.endswith(".mp3"):
        tags = EasyID3(x)
        tags['title'] =  [x[x.find("-")+2:x.find(".mp3")]]
        tags['artist'] = tags['albumartist']=[x[:x.find('-')-1]]
        print(x)
        tags.save()

