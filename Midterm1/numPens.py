def numPens(n):
    """
    n is a non-negative integer

    Returns True if some non-negative integer combination of 5, 8 and 24 equals n
    Otherwise returns False.
    """
    if n % 5 == 0 or n % 8 == 0 or n % 24 == 0:
        return True
    for i in range(n/5):
        for j in range(n/8):
            for k in range(n/24):
                if 5*i + 8*j + 24*k == n:
                    return True
    return False

def testNumPens():
    for i in range(1000):
        print str(i) + ":" + str(numPens(i))

testNumPens()