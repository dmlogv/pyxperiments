"""Set-based diff"""


class DbObject:
    """Example of hashable object"""
    def __init__(self, db, schema, name):
        self.db = db
        self.schema = schema
        self.name = name

    def __eq__(self, other):
        return hash(self) == hash(other)

    def __hash__(self):
        return hash((self.db, self.schema, self.name))

    def __repr__(self):
        return f'<DbObject db="{self.db}", schema="{self.schema}", name="{self.name}">'


if __name__ == '__main__':
    expected = set([
        DbObject('portal', 'dbo', 'alice'),
        DbObject('portal', 'dbo', 'bob'),
        DbObject('portal', 'dbo', 'chris'),
        DbObject('portal', 'dbo', 'derek')
        ])

    actual = set([
        DbObject('portal', 'dbo', 'alice'),
        DbObject('portal', 'dbo', 'bobs'),
        DbObject('portal', 'dbo', 'chris')
        ])

    print('-', expected - actual)
    print('+', actual - expected)
