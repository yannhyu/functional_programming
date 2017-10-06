# (1) Inner and outer functions
def outer():
    def inner():
        print('Inner:  ', x)

    print('Outer (before): ', x)
    inner()
    print('Outer (after): ', x)

x = 'global thing'
print('Global (before):', x)
outer()
print('Global (after):', x)