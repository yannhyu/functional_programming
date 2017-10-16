# Let variables decide how they are treated
# (1) nan monad: not a number
# (2) maybe monad: just or nothing
# (3) list monad: map is an example, 
#     a list ---> a map applied to it ---> new list

def camelcase(s):
    return ''.join([w.capitalize() for w in s.split('_')])

if __name__ == '__main__':
    print(camelcase('some_python_function_name'))

    