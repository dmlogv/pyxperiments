"""Example of Bubble sorting method"""

import random


def random_list(n: int):
    """Returns a list of n random int -> list"""
    randoms = [random.randint(0, n) for _ in range(n)]
    return randoms


def print_list(loop: int, step: int, l: list):
    """Prints list with iteration step count"""
    print(f'loop {loop}, step {step}, {str(l)}')


def bubble_sort(l):
    """Bubble sorting algorithm implemetation"""
    loop = 0

    while True:
        swapped = False
        loop += 1
        for i in range(0, len(l) - 1):
            if l[i] > l[i + 1]:
                # Swap incorrectly placed elements
                l[i], l[i + 1] = l[i + 1], l[i]
                swapped = True

            print_list(loop, i, l)

        if not swapped:
            break

    return l


if __name__ == '__main__':
    bubble_sort(random_list(20))
