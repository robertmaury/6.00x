def loan(balance, annualInterestRate):
    payment = 10
    while True:
        total = 0
        owed = balance
        for i in range(12):
            total += payment
            owed -= payment
            owed += owed * (annualInterestRate / 12.0)
        if owed <= 0:
            print 'Lowest Payment: ' + str(payment)
            break
        else:
            payment += 10


print loan(3329, 0.2)