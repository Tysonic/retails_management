from contextlib import contextmanager

from jnius import autoclass

from edge import Edge
from vertex import Vertex
from index import Index


name_to_class = {
    'tinker': 'com.tinkerpop.blueprints.impls.tg.TinkerGraph',
    'neo4j': 'com.tinkerpop.blueprints.impls.neo4j.Neo4jGraph',
    'orientdb': 'com.tinkerpop.blueprints.impls.orient.OrientGraph',
}


ZERO = '0'


class IndexAPI(object):

    def __init__(self, db):
        self._db = db

    def create(self, name, klass, *parameters):
        return Index(self._db.createIndex(name, klass, *parameters), self._db)

    def get(self, name, klass):
        index = self._db.getIndex(name, klass)
        if index:
            return Index(index, self._db)
        else:
            return None

    def all(self):
        iterator = self._db.getIndices().iterator()
        while iterator.hasNext():
            yield Index(iterator.next(), self._db)

    def delete(self, name):
        self._db.dropIndex(name)


class Graph(object):

    VERTEX = Vertex.VERTEX
    EDGE = Edge.EDGE

    def __init__(self, name, path):
        klass = autoclass(name_to_class[name])
        self._db = klass(path)
        self.index = IndexAPI(self._db)

    def transaction(self):
        conclusion = autoclass('com.tinkerpop.blueprints.TransactionalGraph$Conclusion')
        try:
            yield True
            self._db.stopTransaction(conclusion.SUCCESS)
        finally:
            self._db.stopTransaction(conclusion.FAILURE)
    transaction = contextmanager(transaction)

    def create_vertex(self):
        return Vertex(self._db.addVertex(ZERO), self._db)

    def vertices(self):
        iterator = self._db.getVertices().iterator()
        while iterator.hasNext():
            yield Vertex(iterator.next(), self._db)

    def create_edge(self, start, label, end):
        edge = self._db.addEdge(
            ZERO,
            start._element,
            end._element,
            label
        )
        return Edge(edge, self._db)

    def edges(self):
        iterator = self._db.getEdges().iterator()
        while iterator.hasNext():
            yield Edge(iterator.next(), self._db)

    def close(self):
        self._db.shutdown()

    def edge(self, id):
        return Edge(self._db.getEdge(id), self._db)

    def vertex(self, id):
        return Vertex(self._db.getVertex(id), self._db)
