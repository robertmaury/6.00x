s = str(raw_input('Please enter a string of numbers, comma delimited: '))
summation = 0
for i in range(0, len(s) - 1):
    number = s[i]
    while True:
        if s[i + 1] == ',':
            i = i + 2
            summation = summation + float(number)
            break
        else:
            i = i + 1
            number = number + s[i]
print 'The sum of your values is ' + str(summation)
