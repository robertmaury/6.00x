
import string

def storySplit(story):
    tempStory = ''
    punc = string.punctuation
    for letter in story.lower():
        if letter in punc:
            tempStory += ' '
        else:
            tempStory += letter
    print tempStory
    return tempStory.split()

print storySplit("Hello. I love you. Won't you tell me your name")

