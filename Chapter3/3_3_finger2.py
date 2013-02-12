x = -125
epsilon = 0.01
numGuesses = 0
low = -abs(x)
high = max(1.0, x)
ans = (high + low)/2.0
while abs(ans**3 - x) <= epsilon:
    print 'low =', low, 'high =', high, 'ans =', ans
    numGuesses += 1
    if abs(ans**3) < abs(x):
        low = ans
    else:
        high = ans
    ans = (high + low)/2.0
print 'numGuesses =', numGuesses
print ans, 'is close to the cube root of', x