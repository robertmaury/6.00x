i = 10
odd = 0

while (i > 0):
    number = int(raw_input('Please enter integer: '))
    if odd == 0 and number % 2 == 1:
        greatest = number
        odd = 1
    elif odd == 1 and number > greatest and number % 2 == 1:
        greatest = number
    i = i - 1
if odd == 0:
    print 'No odd integers were entered'
else:
    print 'The largest odd integer entered was ' + str(greatest)
