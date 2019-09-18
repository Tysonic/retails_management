from java import to_java
from java import from_java


class Element(object):

    def __init__(self, element, db):
        self._element = element
        self._db = db

    def id(self):
        if hasattr(self._element.getId(), 'toString'):
            return self._element.getId().toString()
        return str(self._element.getId())

    def __getitem__(self, key):
        return from_java(self._element.getProperty(key))

    def __setitem__(self, key, value):
        value = to_java(value)
        self._element.setProperty(key, value)

    def keys(self):
        keys = []
        iterator = self._element.getPropertyKeys().iterator()
        while iterator.hasNext():
            keys.append(iterator.next())
        return keys

    def __eq__(self, other):
        return self.id() == other.id()

    def __repr__(self):
        return '<%s %s %s>' % (type(self).__name__, self.id(), id(self))
