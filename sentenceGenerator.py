from random import choice

words = {
    'STARGATE': {
        'names': ['Jack O\'neal', 'Danel Jackson', 'Samantha Carter', 'Teal\'c', 'Gorge Hammond', 'The shevron guy'],
        'verbs': ['shot', 'searched', 'scanned', 'explored', 'blew up', 'talked to', 'ate', 'looked at', 'charted'],
        'nouns': ['the gate', 'Earth', 'a death glider', 'the locals', 'the technology', 'the local food', 'a P-90'],
    }
}

def generateSentence(wordSelection):
    output = ''
    output += choice(wordSelection['names']) + ' '
    output += choice(wordSelection['verbs']) + ' '
    output += choice(wordSelection['nouns'])
    output += '.'
    return(output)

while True:
    userInput = input('Select words: ').upper()

    if userInput == 'END':
        break
    if userInput != '':
        selectionExists = False
        for i in words:
            if userInput == i:
                selectionExists = True
                break
        if selectionExists:
            userSelection = userInput
        else: 
            print('Sorry! That isn\'t a word selection. Try one of these:')
            for i in words:
                print('\t' + i)
            print('END')
            continue

    print(generateSentence(words[userSelection.upper()]))
    