input_int = int(raw_input('Please enter integer: '))
root = 0
toggle = 0
while root < abs(input_int):
    power = 0
    while power <= 6:
        if root ** power == input_int:
            print str(root) + ' to the power of ' + str(power) + ' equals ' + str(input_int)
            toggle = 1
        power = power + 1
    root = root + 1
if toggle == 0:
    print 'There are no intger root below 6 for ' + str(input_int)
    