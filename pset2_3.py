def loan(balance, annualInterestRate):
    monthly = annualInterestRate / 12.0
    epsilon = 0.01
    high = (balance * (1 + monthly) ** 12) / 12.0
    low = balance / 12.0
    while True:
        guess = (high + low) / 2.0
        owed = balance
        for i in range(12):
            owed -= guess
            owed += owed * (annualInterestRate / 12.0)
        if abs(owed - 0) < epsilon:
            print 'Lowest Payment: ' + str(round(guess, 2))
            break
        elif owed > 0:
            low = guess
        else:
            high = guess


print loan(320000, 0.2)