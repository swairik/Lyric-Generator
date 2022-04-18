# import requests

# url = "https://shazam.p.rapidapi.com/auto-complete"

# querystring = {"term":"kiss the","locale":"en-US"}

# headers = {
#     'x-rapidapi-host': "shazam.p.rapidapi.com",
#     'x-rapidapi-key': "SIGN-UP-FOR-KEY"
#     }

# response = requests.request("GET", url, headers=headers, params=querystring)

# print(response.text)

import urllib.request
import re
from time import sleep
import random

def main():
    originalLyrics = open('lyrics.txt', 'w')
    url = "https://www.azlyrics.com/c/coldplay.html"
    artistHtml = urllib.request.urlopen(url)
    artistHtmlStr = str(artistHtml.read())

    links = re.findall('href="([^"]+)"', artistHtmlStr)

    # print(links)

    songLinks = []

    for x in links:
        if "lyrics/coldplay" in x:
            x = x.replace("..", "")
            x = "https://www.azlyrics.com/" + x
            songLinks.append(x)

    # print(songLinks)

    for x in songLinks:
        songHtml = urllib.request.urlopen(x)
        songHtmlStr = str(songHtml.read()) 
        #Split the HTML string twice so that we only get the lyrics
        split = songHtmlStr.split('content by any third-party lyrics provider is prohibited by our licensing agreement. Sorry about that. -->',1)
        split_html = split[1]
        split = split_html.split('</div>',1)
        lyrics = split[0]
        #Replace the HTML of the lyrics we don't want
        lyrics = lyrics.replace('<br>', '\n')
        lyrics = lyrics.replace('\\', '')
        lyrics = lyrics.replace('\nn', '\n')
        lyrics = lyrics.replace('<i>', '')
        lyrics = lyrics.replace('</i>', '')
        lyrics = lyrics.replace('[Chorus]', '')
        lyrics = lyrics.replace('[Chorus:]', '')
        originalLyrics.write(lyrics)
        sleep (random.randint(2, 10))
    originalLyrics.close() #We close the file because we no longer have to write anything to it


if __name__ == "__main__":
    main()