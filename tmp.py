import random

def flu():
    flu = False
    for i in range(3):
        sample = random.random()
        if sample < .1 and flu == False:
            flu = True
        elif sample < .1 and flu == True:
            return False
        else:
            pass
    return True if flu == True else False

def testFlu(numTrials):
    count = 0
    for i in range(numTrials):
        if flu():
            count +=1
    return count / float(numTrials)

def devFlu(numTrials, numSamples):
    results = []
    for i in range(numTrials):
        results.append(testFlu(numSamples))
    return sum(results)/float(numTrials)

print devFlu(1000,1000)