# (1) Inner and outer functions
def outer():
    def inner():
        nonlocal x    # Refer to one level up (Python 3 only)
        x = 'inner thing'
        print('Inner:  ', x)

    x = 'outer thing'
    print('Outer (before): ', x)
    inner()
    print('Outer (after): ', x)

x = 'global thing'
print('Global (before):', x)
outer()
print('Global (after):', x)