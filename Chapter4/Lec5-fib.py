def fib(x, counter):
    """assumes x an int >= 0
       returns Fibonacci of x"""
    assert type(x) == int and x >= 0
    if x == 0 or x == 1:
        return 1
    else:
        return ((fib(x-1, counter) + fib(x-2, counter)), counter + 1)
    
result, counter = (fib(5,0))
print result
print counter