from monads import camelcase

class Just:
    def __init__(self, value):
        self._value = value

    def bind(self, func):
        try:
            return Just(func(self._value))
        except:
            return Nothing()

    def __repr__(self):
        return self._value


class Nothing:
    def bind(self, func):
        return Nothing()

    def __repr__(self):
        return "Nothing"


if __name__ == '__main__':
    print(Just('some_python_function_name_maybe').bind(camelcase))
    print(Nothing().bind(camelcase))
    print(Just(11).bind(camelcase))