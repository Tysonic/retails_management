from jnius import autoclass

from element import Element
from vertex import Vertex

Direction = autoclass('com.tinkerpop.blueprints.Direction')


class Edge(Element):

    EDGE = autoclass('com.tinkerpop.blueprints.Edge')

    def delete(self):
        self._db.removeEdge(self._element)

    def label(self):
        return self._element.getLabel()

    def start(self):
        return Vertex(self._element.getVertex(Direction.OUT), self._db)

    def end(self):
        return Vertex(self._element.getVertex(Direction.IN), self._db)

    def data(self):
        data = dict(id=self.id())
        for key in self.keys():
            data[key] = self[key]
        data['start'] = self.start.id()
        data['end'] = self.end.id()
        return data
