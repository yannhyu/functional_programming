l_factorial = lambda n: 1 if n == 0 else n*l_factorial(n-1)

def chain_mul(*what):
    """
    Takes a list of (function, argument) tuples. 
    Calls each function with its argument, multiplies up the 
    return values, and returns the total. 
    """ 
    total = 1
    for (func, arg) in what:
        total *= func(arg)
    return total

res = chain_mul(
    (l_factorial, 2),
    (l_factorial, 3))
print(res)