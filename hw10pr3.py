# CS5 Black, hw10pr2
# Name: Vicki Moran
# Date: 11/14/2016
# Problem description: Markov Text Generation

import random
import string

def main():
    while True:
        numFiles = input("How many text files will you provide? ")
        try:
            numFiles = int(numFiles)
            break
        except:
            print("Please enter a number.")
    text = ""
    for i in range(numFiles):
        while True:
            fileToRead= input("What is the name of your file? ")
            try:
                inFile = open(fileToRead, "r")
                text += inFile.read()
                break
            except:
                print("Please enter a text file.")
    while True:
        k = input("What should be the order of the Markov process? ")
        try:
            k = int(k)
            break
        except:
            print("Please enter a number.")
    mmodel = markov_model(text, k)
    numwords = int(input("How many words do you want in your generated writing? "))
    generated = gen_from_model(mmodel, numwords)

def markov_model(text, k):
    """accepts a single (potentially large) string of text and returns a k-th order Markov model dictionary based on that text"""
    model = {}
    words = text.split()
    sequences = []
    startTupe = ()
    firstWords = []
    for i in range(k):
        startTupe += ('$',)
    for w in range(len(words) - 1):
        if words[w-1][-1:] in string.punctuation:
            firstWords += [words[w]]
    model[startTupe] = firstWords

    for w in range(len(words)- k):
        initWords = ()
        for index in range(k):
            if words[w + index][-1:] in string.punctuation:
                initWords = ()
                for i in range(index + 1):
                    initWords += ('$',)
            else:
                initWords += (words[w+index],)
        for i in range(k):
            if initWords[k-1][-1:] in string.punctuation:
                break
            elif initWords in sequences:
                break
            else:
                sequences += [initWords]
    for s in sequences:
        followWords = []
        for w in range(len(words)):
            numEqual = 0
            for i in range(1, k+1):
                if s[k-i] == '$':
                    if s[k-i+1] == '$':
                        numEqual += 1
                    elif i > 1 and words[w-i][-1:] in string.punctuation:
                        numEqual += 1
                elif words[w-i] == s[k-i]:
                    numEqual += 1
            if numEqual == k:
                followWords += [words[w]]
        model[s] = followWords
    
    return model




def gen_from_model(mmodel, numwords):
    """determines the order of the Markov model (mmodel) and generates numwords words from it"""
    L = []
    text = ""
    k = len(list(mmodel)[0])
    for i in range(k):
        L += [random.choice(mmodel[('$',) * k])]
    for w in range(k, numwords):
        key = ()
        for i in range(k):
            if L[w-k+i][-1:] in string.punctuation:
                key = ('$',) * (i+1)
            else:
                key += (L[w-k+i],)
        while key not in list(mmodel):
            key = ('$',) + key[:-1]
        L += [random.choice(mmodel[key])]
        
    for index in L:
        text = text + index + ' '
    if text[-1:] != '.':
        text = text[:-1] + '.'
    print(text)
    


if __name__ == "__main__":
    main()


# I used Drake lyrics as my input text and an order of 2

# I Too aim reserved I one know stone, more life More time to get it right It's only me but I'm seeing four shadows in the music Because if I don't say it here then I won't say nothing Could feel my hand getting tired from holding the grudges Two birds, Too reserved like I called ahead for me and my lady Free C5, one stone, I know that day's coming I put it all in the light My demons visit me every night To the most high I'm forever indebted I know that day's coming I put it all in the light My demons visit me every night To the most high I'm forever indebted I know I gotta pay something, Too reserved like I called ahead for me and my lady Free C5, how the fuck we got the boss waiting Ever since the blue basement I found God and I lost patience Between rocks and hard places of all places my my aim is amazing I need to start losing my shit Just to show you niggas who hatin' Too reserved like I called ahead for me and my lady Free C5, Too reserved like I called ahead for me and my lady Free C5, Too reserved like I called ahead for me and my lady Free C5, Too reserved like I called ahead for me and my lady Free C5, Too reserved like I called ahead for me and my lady Free C5, my aim is amazing I need to start losing my shit Just to show you niggas who hatin' more life More time to get it right It's only me but I'm seeing four shadows in the light My demons visit me every night To the most high I'm forever indebted I know that day's coming I put it all in the light My demons visit me every night To the most high I'm forever indebted I know that day's coming I put it all in the light My demons visit me every night To the most high I'm forever indebted I know I gotta pay something, more life More time with family and friends, how the fuck we got the boss waiting Ever since the blue basement I found God and I lost patience Between rocks and hard places of all places I Too know reserved Too how reserved the how Too the reserved more how life the my how aim the Too Too reserved like I called ahead for me and my lady Free C5, my aim is amazing I need to start losing my shit Just to show you niggas who hatin' my aim is amazing I need to start losing my shit Just to show you niggas who hatin' how the fuck we got the boss waiting Ever since the blue basement I found God and I lost patience Between rocks and hard places of all places I how know the more how life the more one life stone, I.
