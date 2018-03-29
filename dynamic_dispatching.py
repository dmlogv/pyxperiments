"""Example of classes without real methods nor fields"""

import logging


logging.basicConfig(level=logging.INFO)


class ClassWithoutMethods:
    """Class with dynamically dispatched methods"""
    def __getattr__(self, item):
        def dispatcher(*args, **kwargs):
            logging.info('Method `%s` called with args: `%s` and kwargs: `%s`', item, args, kwargs)
        return dispatcher


class ClassWithoutFields:
    """Class with dynamically dispatched fields"""
    dbd = 33

    def __getattr__(self, item):
        if item == 'a':
            return 10
        if 'b' in item:
            return 100
        else:
            return '50'


if __name__ == '__main__':
    cwm = ClassWithoutMethods()
    cwm.callme()
    cwm.call_yet_another(123, 123, mc=443, ml=998)
    a = cwm.buusdf

    cwf = ClassWithoutFields()
    print(cwf.a)
    print(cwf.dbd)
    print(cwf.df)
        
