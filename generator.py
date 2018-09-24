"""Example of custom generator"""

import os
import re


class FileLister:
    """Find files matching with a given RE"""
    def __init__(self, folder=r'.', mask=r'.'):
        self.folder = folder
        self.mask = mask
        self._mask_re = re.compile(mask)

        self._list = os.listdir(self.folder)

    def __iter__(self):
        for f in self._list:
            if self._mask_re.match(f):
                yield f


if __name__ == '__main__':
    for f in FileLister(r'.', r'.*\.gif'):
        print(f)
