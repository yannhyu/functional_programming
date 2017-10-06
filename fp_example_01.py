l_factorial = lambda n: 1 if n == 0 else n*l_factorial(n-1)

assert(l_factorial(3) == 6)