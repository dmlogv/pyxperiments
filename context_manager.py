"""Custom Context manager"""

class Catcher:
    """Context manager implementing exception catching"""
    def __enter__(self):
        print('--- Context start ---')

        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type or exc_value or traceback:
            print(f'Exception occured: \n'
                  f'    exc_type: "{exc_type}"\n'
                  f'    exc_value: "{exc_value}"\n'
                  f'    traceback: "{traceback}"')

        print('--- Context end ---')

        return True


if __name__ == '__main__':
    with Catcher() as c:
        print(c)
        print(1)

    with Catcher() as c:
        print(c)
        print(1/0)
