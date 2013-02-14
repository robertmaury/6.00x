print 'Please think of a secret number between 0 and 100!'
low = 0
high = 100
while True:
    guess = (high + low) / 2
    print 'Is your secret number ' + str(guess) 
    response = str(raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly."))
    if response == 'h':
        high = guess
    elif response == 'l':
        low = guess
    elif response == 'c':
        print 'Game over. Your secret number was: ' + str(guess)
        break
    else:
        print 'Sorry, I did not understand your input.'
