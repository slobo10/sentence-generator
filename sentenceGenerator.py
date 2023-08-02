from random import choice, random

words = {
    'STARGATE': {
        'names': ['Jack O\'neal', 'Danel Jackson', 'Samantha Carter', 'Teal\'c', 'Gorge Hammond', 'The shevron guy'],
        'adverbs': ['crazyly', 'carelessly', 'violently'],
        'verbs': ['shot', 'searched', 'scanned', 'explored', 'blew up', 'talked to', 'ate', 'looked at', 'charted'],
        'ajectives': ['evil', 'crazy', 'Go\'al\'uld infested', 'cool'],
        'nouns': [['the', 'gate'], ['', 'Earth'], ['a', 'death glider'], ['the', 'locals'], ['the', 'technology'], ['the', 'local food'], ['a', 'P-90']],
    },
    'KERBAL SPACE PROGRAM': {
        'names': ['Jebediah Kerman', 'Valentina Kerman', 'Bob Kerman', 'Bill Kerman'],
        'adverbs': ['crazyly', 'carefuly', 'forcefully'],
        'verbs': ['piloted', 'egineered', 'crashed', 'refueled', 'orbited around', 'threw into space', 'experimented on', 'blew up', 'set fire to', 'destoyed'],
        'ajectives': ['crazy', 'unsafe', 'noninspected', 'rusty', 'freezing', 'floating'],
        'nouns': [['', 'Kerbin'], ['', 'Duna'], ['an', 'orbiter rocket'], ['a', 'spaceplane'], ['a', 'building'], ['', 'Kerbal Space Program'], ['the', 'vehicle assembly building'], ['the', 'space plane hanger']],
    }
}
conjunctions = [', and', ', or', ', so', ', but']
prepositions = ['behind', 'on', 'inside of', 'under', 'next to']

def generateSentence(wordSelection):
    output = ''
    while True:
        output += choice(wordSelection['names']) + ' '
        if (random() < 1/4):
            output += choice(wordSelection['adverbs']) + ' '
        output += choice(wordSelection['verbs']) + ' '
        noun = choice(wordSelection['nouns'])
        output += noun[0]
        if (noun[0] != ''):
            output += ' '
        if (random() < 1/2):
            output += choice(wordSelection['ajectives']) + ' '
        output += noun[1]
        if (random() < 1/3):
            noun = choice(wordSelection['nouns'])
            output += ' ' + choice(prepositions) 
            if (noun[0] != ''):
                output += ' '
            output += noun[0] + ' '
            if (random() < 1/2):
                output += choice(wordSelection['ajectives']) + ' '
            output += noun[1]
        if (random() > 1/2):
            break
        output += choice(conjunctions) + ' '
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
            print('\tEnter for last words')
            print('\tEND to end')
            continue

    print(generateSentence(words[userSelection.upper()]))
    