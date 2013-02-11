x = 2
y = 2
z = 2

if ((x > y and y > z) or (y % 2 == 0 and z % 2 == 0)) and x % 2 == 1:
    print 'X is greatest'
elif (y > z or z % 2 == 0) and y % 2 == 1:
    print 'Y is greatest'
elif z % 2 == 1:
    print 'Z is greatest'
else:
    print 'All numbers are even'