import pylab
import random
import collections

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordList: list of strings
    wordList = []
    temp = []
    for line in inFile:
        temp.append(line.strip().lower())
    for word in temp:
        tempWord = []
        if len(word) <= 5 and len(word) >= 5:
            wordList.append(word)
    print "  ", len(wordList), "words loaded."
    return wordList

def tileSet():
    alpha = { None:0,'a':9, 'b':2, 'c':2, 'd':4, 'e':12, 'f':2, 'g':3, 'h':2, 'i':9, 'j':1,
             'k':1, 'l':4, 'm':2, 'n':6, 'o':8, 'p':2, 'q':1, 'r':6, 's':4, 't':6, 'u':4, 'v':2,
             'w':2, 'x':1, 'y':2, 'z':1 }
    tileSet = []
    for letter in alpha:
        for i in range(alpha[letter]):
            tileSet.append(letter)
    return tileSet

def drawHand(tiles):
    hand = []
    for i in range(7):
        letter = random.choice(tiles)
        tiles.remove(letter)
        hand.append(letter)
    return hand

def wordTrue(word, hand):
    for letter in word:
        if letter not in hand:
            return False
    return True

def wordTest(hand):
    count = 0
    for word in wordList:
        if wordTrue(word, hand[:]):
            count += 1
            #print word, hand
    return count

def sampleTest(trialSize, numTrials):
    library = []
    tiles = tileSet()
    for i in range(numTrials):
        avg = []
        for j in range(trialSize):
            hand = drawHand(tiles[:])
            avg.append(wordTest(hand))
        library.append(sum(avg)/float(trialSize))
    pylab.hist(library,bins=20)
    pylab.show()
    return stdDev(library)

def stdDev(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    return (tot/len(X))**0.5

def test(wordList):
    count = 0
    tiles = tileSet()
    while True:
        hand = drawHand(tiles[:])
        if wordTest(hand):
            break
        else:
            count += 1
    print count, hand

if __name__ == '__main__':
    wordList = loadWords()
    #print wordTest(tileSet(), wordList)
    #test(wordList)
    print sampleTest(20, 50 )
    #for i in range(20):
    #    print drawHand(tileSet())

