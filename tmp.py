def insertNewlines(text, lineLength):
    """
    Given text and a desired line length, wrap the text as a typewriter would.
    Insert a newline character ("\n") after each word that reaches or exceeds
    the desired line length.

    text: a string containing the text to wrap.
    line_length: the number of characters to include on a line before wrapping
        the next word.
    returns: a string, with newline characters inserted appropriately. 
    """
    wordList = text.split(' ')
    def newLine(wordList, lineLength, text):
        if len(text) >= lineLength:
            return text
        text += wordList[0] + ' '
        return newLine(wordList[1:], lineLength, text)
    if len(text) <= lineLength:
        return text
    else:
        line = newLine(wordList, lineLength, '')
        return line + '\n' + insertNewlines(text[len(line):], lineLength)
    
print insertNewlines('Random text to wrap again.', 5)