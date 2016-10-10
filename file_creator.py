"""Creates a couple of millions text files"""

import os


def generate_files(folder, n):
    """Generate n text files in folder

    Args:
        folder (str): path
        n (int): number of files
    """
    try:
        os.mkdir(folder)
    except FileExistsError:
        pass

    for current in range(n):
        name = '{:0>10d}'.format(current)
        print(name)
        with open(os.path.join(folder, name), 'w') as file:
            file.write(name)


if __name__ == '__main__':
    FOLDER = r'e:\kill'
    MAX = 2_000_000

    generate_files(FOLDER, MAX)
