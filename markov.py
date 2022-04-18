'''
Links:
1) https://dev.to/catmcgeecode/get-your-first-dev-job-by-building-these-projects-2-markov-chain-lyrics-generator-1kib
2) https://realpython.com/lyricize-a-flask-app-to-create-lyrics-using-markov-chains/
3) https://bookdown.org/probability/beta/markov-chains.html (use this to study markov chains)
'''

# from random import choice
import random
import sys

import getLyrics

ErrorsFound = 0

def generateModel(text, order):
    model = {}
    for i in range(0, len(text) - order):
        fragment = text[i : i + order]
        nextLetter = text[i + order]
        if fragment not in model:
            model[fragment] = {}
        if nextLetter not in model[fragment]:
            model[fragment][nextLetter] = 1
        else:
            model[fragment][nextLetter] += 1
    # print("model : ", model)
    return model

def getNextCharacter(model, fragment):
    letters = []
    try:
        for letter in model[fragment].keys():
            for times in range(0, model[fragment][letter]):
                letters.append(letter)
        return random.choice(letters)
    except KeyError:
        print("fragment : ", fragment)
        global ErrorsFound 
        ErrorsFound += 1
    # print(letters)
    return chr(random.randrange(26) + ord('a'))         # safety net // shouldn't reach here if sample size is big enough

def generateText(text, order, length):
    model = generateModel(text, order)
    currentFragment = text[0 : order]
    output = ""
    for i in range (0, length - order):
        newCharacter = getNextCharacter(model, currentFragment)
        output += newCharacter
        currentFragment = currentFragment[1 : ] + newCharacter
    if(ErrorsFound) :
        print("Errors Found : ", ErrorsFound)
    print(output)

# text = "some sample text"     # need more sample size

text = open('lyrics.txt', 'r').read()

# print(text)

# text = "Almost heaven, West Virginia Blue Ridge Mountains, Shenandoah River Life is old there, older than the trees Younger than the mountains, growin' like a breeze Country roads, take me home To the place I belong West Virginia, mountain mama Take me home, country roads All my memories gather 'round her Miner's lady, stranger to blue water Dark and dusty, painted on the sky Misty taste of moonshine, teardrop in my eye Country roads, take me home To the place I belong West Virginia, mountain mama Take me home, country roads I hear her voice in the mornin' hour, she calls me The radio reminds me of my home far away Drivin' down the road, I get a feelin' That I should've been home yesterday, yesterday Country roads, take me home To the place I belong West Virginia, mountain mama Take me home, country roads Country roads, take me home To the place I belong West Virginia, mountain mama Take me home, country roads Take me home, (down) country roads Take me home, (down) country roads"

# text = "So I look in your direction\r\nBut you pay me no attention, do you\r\nI know you don't listen to me\r\n'Cause you say you see straight through me, don't you"


# Letters = getNextCharacter(generateModel(text, 2), "so")
# print(Letters)


if __name__ == "__main__":
    # generateText(text, int(sys.argv[1]), int(sys.argv[2]))
    # pass
    getLyrics.main()
    generateText(text, 10, 400)
