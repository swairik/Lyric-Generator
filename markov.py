import random

import getLyrics

ErrorsFound = 0

def generateModel(text, order):
    model = {}
    for i in range(0, len(text) - order):
        fragment = ''.join(text[i : i + order])
        nextWord = text[i + order]
        if fragment not in model:
            model[fragment] = {}
        if nextWord not in model[fragment]:
            model[fragment][nextWord] = 1
        else:
            model[fragment][nextWord] += 1
    # print("model : ", model)
    # print(model)
    return model

def getNextCharacter(model, fragment):
    words = []
    try:
        for word in model[fragment].keys():
            for times in range(0, model[fragment][word]):
                words.append(word)
        return random.choice(words)
    except KeyError:
        # print("fragment : ", fragment)
        global ErrorsFound 
        ErrorsFound += 1
    # print(words)
    return chr(random.randrange(26) + ord('a'))         # safety net // shouldn't reach here if sample size is big enough

def generateText(text, order, length):
    model = generateModel(text, order)
    currentFragment = text[0 : order]
    output = []
    for i in range (0, length - order):
        newWord = getNextCharacter(model, ''.join(currentFragment))
        output.append(newWord)
        currentFragment.append(newWord)
        currentFragment = currentFragment[1:]
    if(ErrorsFound) :
        print("Errors Found : ", ErrorsFound)
    print(' '.join(output))

text = open('lyrics.txt', 'r').read()

text = text.split()

if __name__ == "__main__":
    getLyrics.main()

    generateText(text, 1, 400)
