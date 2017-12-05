"""Example of hashable class"""

class Hashable:
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        return self.value == other

    def __hash__(self):
        return hash(self.value)

    def __repr__(self):
        return '<Hashable: {}>'.format(self.value)


if __name__ == '__main__':
    # Make just a list
    hashables = [Hashable(1), Hashable(2), Hashable(3), Hashable(1)]
    print(hashables)

    # Hashables can be casted to Set
    print(set(hashables))

    # Use Hashables as a dict keys
    dictables = dict(zip(hashables, [h.value for h in hashables]))
    print(dictables)
