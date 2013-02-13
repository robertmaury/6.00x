s = str(raw_input('Please enter a string of numbers, comma delimited: '))
summation = 0
number = ''
for i in range(0, len(s)):
    if s[i] == ',':
        summation += float(number)
        number = ''
    else:
        number = number + s[i]
summation += float(number)
print 'The sum of your values is ' + str(summation)
