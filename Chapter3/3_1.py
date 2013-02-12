input_int = int(raw_input('Enter an integer: '))
answer = 0
while answer ** 3 < abs(input_int):
    answer = answer + 1
if answer ** 3 != abs(input_int):
    print input_int, 'is not a perfect cube'
else:
    if input_int < 0:
        answer = -answer
    print 'Cube root of ' + str(input_int) + ' is ' + str(answer)
