l_factorial = lambda n: 1 if n == 0 else n*l_factorial(n-1)

assert(l_factorial(3) == 6)

# Timing implementations

# (1) The procedural way going line by line
import time

t0 = time.time()
l_factorial(900)
t1 = time.time()
print('Took: %.5f s' % (t1-t0))

# (2) The functional way with a wrapper function
def timer(fnc, arg):
    t0 = time.time()
    fnc(arg)
    t1 = time.time()
    return t1-t0

print('Took: %.5f s' % timer(l_factorial, 888))

# (3) Fully functional way with lambda wrapper function
l_timestamp = lambda fnc, arg: (time.time(), fnc(arg), time.time())
l_diff = lambda t0, retval, t1: t1-t0
l_timer = lambda fnc, arg: l_diff(*l_timestamp(fnc, arg))

print('Took: %.5f s' % l_timer(l_factorial, 777))
