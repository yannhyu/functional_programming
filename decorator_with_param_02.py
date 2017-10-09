import time

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

@timer_with_param(units='ms')
def factorial(n):
    return 1 if n==0 else n*factorial(n-1)


print(factorial(300))