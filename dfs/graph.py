from vertex import Vertex
from edge import Edge

class Graph:

    def __init__(self):
        self.list_vertex = []
        self.list_edge = []

    def insert_vertex(self, vertex):
        if(isinstance(vertex, Vertex) and vertex not in self.list_vertex):
            self.list_vertex.append(vertex)

    def insert_edge(self, edge):
        if edge is not None and isinstance(edge, Edge):
            self.list_edge.append(edge)

    def get_list_vertex(self):
        return self.list_vertex

    def get_list_edge(self):
        return self.list_edge
