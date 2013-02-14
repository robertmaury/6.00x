number = long(raw_input('Please enter a number: '))
root = int(raw_input("Please input which root you'd like: "))
epsilon = 0.0000000001
guess = number / 2.0
count = 0
while abs(guess ** root - number) >= epsilon:
    guess = guess - (((guess ** root) - number) / (root * guess ** (root - 1)))
    count += 1
    print guess
print count
print 'The ' + str(root) + ' root of ' + str(number) + ' is about ' + str(guess)
