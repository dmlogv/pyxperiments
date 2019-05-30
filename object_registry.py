"""Object registry demonstration"""


# My global state
REGISTRY = []


class AbstractBulka:
    """Class will add instances to the global REGISTRY

    Not really abstract :)
    """
    def __init__(self):
        # Add me to the REGISTRY
        REGISTRY.append(self)

    def __del__(self):
        # Remove me from the REGISTRY
        REGISTRY.remove(self)

    def __eq__(self, obj):
        return id(self) == id(obj)
    
    def __repr__(self):
        return f'<{self.__class__.__name__} {id(self)}>'


class Plushka(AbstractBulka):
    pass


class Pirozhok(AbstractBulka):
    def __init__(self, components=None):
        self.components = components or []
        super().__init__()


if __name__ == '__main__':
    # Create some objects
    ab = AbstractBulka()
    p = Plushka()
    pi = Pirozhok(['potato'])

    ab = AbstractBulka()
    ab = AbstractBulka()

    # They are in the REGISTRY! It's awesome!
    print(REGISTRY)

    # Delete the first object
    ab.__del__()
    print(REGISTRY)

    # Delete the second object
    pi.__del__()
    print(REGISTRY)
