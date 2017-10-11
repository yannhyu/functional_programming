# One argument per function
# add(1,2,3) ---> add(1)(2)(3)
from functools import partial

# (1) Simple example
def add(a, b, c):
    return a + b + c

print(add(10, 100, 1000))
add_10 = partial(add, 10)
add_10_100 = partial(add_10, 100)
print(add_10_100(1000))

# (2) currying
from inspect import signature

def curry(func):
    def inner(arg):
        # Exactly one argument, no need to curry
        if len(signature(func).parameters) == 1:
            return func(arg)    # no need for curry
        return curry(partial(func, arg))
    return inner

@curry
def curry_add(a, b, c):
    return a + b + c

print(curry_add(1)(2)(3))