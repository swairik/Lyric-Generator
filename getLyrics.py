import urllib.request
import re
from time import sleep
import random

def main():
    artistName = input('Enter the name of the artist : ')

    originalLyrics = open('lyrics.txt', 'w')

    url = f'https://www.azlyrics.com/c/{artistName}.html'
    artistHtml = urllib.request.urlopen(url)
    artistHtmlStr = str(artistHtml.read())

    links = re.findall('href="([^"]+)"', artistHtmlStr)

    # print(links)

    songLinks = []

    for link in links:
        if f'lyrics/{artistName}' in link:
            link = link.replace("..", "")
            link = "https://www.azlyrics.com/" + link
            songLinks.append(link)

    # print(songLinks)

    for songLink in songLinks:
        songHtml = urllib.request.urlopen(songLink)
        songHtmlStr = str(songHtml.read()) 

        #Split the HTML string twice so that we only get the lyrics
        split = songHtmlStr.split('content by any third-party lyrics provider is prohibited by our licensing agreement. Sorry about that. -->',1)
        split_html = split[1]
        split = split_html.split('</div>', 1)
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
        
        sleep(random.randint(2, 10))

    originalLyrics.close() # We close the file because we no longer have to write anything to it


if __name__ == "__main__":
    main()