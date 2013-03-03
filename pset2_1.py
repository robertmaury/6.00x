def loan(balance, annualInterestRate, monthlyPaymentRate):
    total = 0
    for i in range(12):
        payment = balance * monthlyPaymentRate
        total += payment
        balance -= payment
        balance += balance * (annualInterestRate / 12.0)
        month = i +1
        print 'Month:' + str(month)
        print 'Minimum monthly payment: ' + str(round(payment, 2))
        print 'Remaining balance: ' + str(round(balance, 2))
    print 'Total paid: ' + str(round(total, 2))
    print 'Remaining balance: ' + str(round(balance, 2))


print loan(4213, 0.2, 0.04)