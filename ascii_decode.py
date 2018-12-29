"""Decode ASCII-encoded messages"""

def decode(coded):
    """Decode a string of ASCII codes"""
    return ''.join(map(chr, map(int, coded.split())))


if __name__ == '__main__':
    print(decode('''
        67 111 109 101 32 105
        110 32 97 32 78 101
        119 32 89 101 97 114
        39 115 32 99 97 112
        32 116 111 32 83 97
        118 101 110 107 111 118
        033
    '''))

    print(decode('''
        77 115 102 112
        117 110 105 108
        104 121
    '''))
