from monads import camelcase

class List:
    def __init__(self, values):
        self._values = values
    def bind(self, func):
        return List([func(value) for value in self._values])
    def __repr__(self):
        return str(self._values)

print(List(['some_text', 'other_text']).bind(camelcase))