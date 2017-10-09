import time

def factorial(n):
    return 1 if n==0 else n*factorial(n-1)

def timer_with_param(units='s'):
    def timer(func):
        def inner(arg):
            t0 = time.time()
            func(arg)
            t1 = time.time()
            diff = t1 - t0
            if units == 'ms':
                diff *= 1000
            return diff
        return inner
    return timer

timed_factorial = timer_with_param(units='ms')(factorial)
print(timed_factorial(500))