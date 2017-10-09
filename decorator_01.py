import time

def factorial(n):
    return 1 if n==0 else n*factorial(n-1)

def timer(func):
    def inner(arg):
        t0 = time.time()
        func(arg)
        t1 = time.time()
        return t1-t0

    return inner

timed_fac = timer(factorial)
res = timed_fac(50)
print(res)