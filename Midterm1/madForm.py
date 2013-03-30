def generateForm(story, listOfAdjs, listOfNouns, listOfVerbs):
    ''' 
    story: a string containing sentences
    listOfAdjs: a list of valid adjectives
    listOfNouns: a list of valid nouns
    listOfVerbs: a list of valid verbs

    For each word in story that is in one of the lists,
    * replace it with the string '[ADJ]' if the word is in listOfAdjs
    * replace it with the string '[VERB]' if the word is in listOfVerbs
    * replace it with the string '[NOUN]' if the word is in listOfNouns

    returns: string, A Mad-Libs form of the story. 
    '''
    listStory = story.split(' ')
    madForm = ''
    for word in listStory:
        if word in listOfAdjs:
            madForm += '[ADJ]' + ' '
        elif word in listOfNouns:
            madForm += '[NOUN]' + ' '
        elif word in listOfVerbs:
            madForm += '[VERB]' + ' '
        else:
            madForm +=  word + ' '
    return madForm

def generateTemplates(madLibsForm):
    """ 
    madLibsForm: string, in a Mad-Lib form. See output of `generateForm`

    returns: a list of '[ADJ]', '[VERB]', and '[NOUN]' strings, in
    the order they appear in the madLibsForm.             
    """
    listForm = madLibsForm.split(' ')
    madTemplate = []
    for word in listForm:
        if word == '[ADJ]' or word == '[VERB]' or word == '[NOUN]':
            madTemplate.append(word)
    return madTemplate

def verifyWord(userWord, madTemplate, listOfAdjs, listOfNouns, listOfVerbs):
    """ 
    userWord: a string, the word the user inputted
    madTemplate: string, the type of word the user was supposed to input
    listOfAdjs: a list of valid adjectives
    listOfNouns: a list of valid nouns
    listOfVerbs: a list of valid verbs):

    returns: Boolean, whether or not the word is valid
    """
    if madTemplate == '[ADJ]':
        return userWord in listOfAdjs
    elif madTemplate == '[VERB]':
        return userWord in listOfVerbs
    elif madTemplate == '[NOUN]':
        return userWord in listOfNouns
    else:
        return False

def selfTest():
    story = "It is hard to write correct programs during a test!"
    listOfAdjs = ["correct"]    # a small list of adjectives
    listOfNouns = ["test"]      # a small list of nouns
    listOfVerbs = ["write"]     # a small list of verbs
    form = generateForm(story, listOfAdjs, listOfNouns, listOfVerbs)
    
    newStory = generateStoryFromFormAndWords(form, ["write","correct","test"] )
    return story == newStory

#story = 'At the creepy thrift store I found a pair of plaid pants that looked like something your grandpa might wear'
#listOfAdjs = ['creepy', 'plaid']
#listOfNouns = ['store', 'pants', 'something', 'grandpa']
#listOfVerbs = ['found', 'looked']
#print verifyWord('found','[NOUN]',listOfAdjs, listOfNouns, listOfVerbs)