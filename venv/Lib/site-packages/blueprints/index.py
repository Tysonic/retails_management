from edge import Edge
from vertex import Vertex


class Index(object):

    def __init__(self, index, db):
        self._index = index
        self._db = db

    def name(self):
        return self._index.getIndexName()

    def put(self, key, value, element):
        self._index.put(key, value, element._element)

    def get(self, key, value):
        iterator = self._index.get(key, value).iterator()
        while iterator.hasNext():
            element = iterator.next()
            class_name = element.getClass().getName()
            if 'Vertex' in class_name:
                yield Vertex(element, self._db)
            else:
                yield Edge(element, self._db)

    def count(self, key, value):
        return self._index.count(key, value)

    def remove(self, key, value, element):
        self._index.remove(key, value, element._element)
