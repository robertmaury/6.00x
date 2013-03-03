def isIn(st1, st2):
    if st1.find(st2) == True or st2.find(st1) == True:
        return True
    else:
        return False

print isIn('b','abc')