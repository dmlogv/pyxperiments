"""Serialize object to XML using `lxml`. Need `lxml` (surprise!)"""

from lxml import etree
from lxml.builder import E


class XmlSerializer:
    """Serializis Universalis"""
    @staticmethod
    def dumps(obj):
        """Dump XML of obj"""
        root = getattr(E, obj.__class__.__name__)(
            *[getattr(E, k)(str(v)) for k, v in vars(obj).items()]
            )

        return root


class Serializable:
    """Class with dynamic properties"""
    def __init__(self, name, **kwargs):
        self.name = name
        for k, v in kwargs.items():
            setattr(self, k, v)

    def __repr__(self):
        fields = ' '.join(f'{k, v}' for k, v in vars(self))
        return (f'<{self.__class__.__name__} '
                f'{fields}>')


if __name__ == '__main__':    
    # Create some instances
    test0 = Serializable('Gotcha', mahrab=True, kahlem=False, agon='Sap')
    test1 = Serializable('Garas', mahrab=False, agon='Sap')
    test2 = Serializable('Astam', nar='Tash', nei=False)

    # Look at XMLs
    print(etree.tostring(XmlSerializer.dumps(test0)))
    print(etree.tostring(XmlSerializer.dumps(test1)))
    print(etree.tostring(XmlSerializer.dumps(test2)))
