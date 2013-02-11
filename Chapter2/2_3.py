var_x = 2
var_y = 2
var_z = 2

if ((var_x > var_y and var_y > var_z) or (var_y % 2 == 0 and var_z % 2 == 0)) and var_x % 2 == 1:
    print 'X is greatest'
elif (var_y > var_z or var_z % 2 == 0) and var_y % 2 == 1:
    print 'Y is greatest'
elif var_z % 2 == 1:
    print 'Z is greatest'
else:
    print 'All numbers are even'
