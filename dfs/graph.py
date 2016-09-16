from vertex import Vertex
from edge import Edge
import numpy as np

class Graph:

    def __init__(self, list_ver=[], list_edg=[]):
        #self.dict_vertex = {}
        self.list_vertex = list_ver
        self.list_previsit = []
        self.list_edge = list_edg
        self.states_node = []
        self.pos_actual_vertex = 0
        #es la lista de las prioridades de las posiciones
        #self.list_privilege = ['N', 'S', 'E', 'W']
        self.j = 1

    def insert_vertex(self, new_vertex, come_back):
        vertex = None
        if(isinstance(new_vertex, Vertex) and new_vertex not in self.list_vertex):
            size_list_vertex = len(self.list_vertex)
            if(size_list_vertex > 0):
                if come_back:
                    pos_previsit = self.list_previsit[self.pos_actual_vertex]
                    vertex = self.list_vertex[pos_previsit]
                    self.pos_actual_vertex = pos_previsit
                else:
                    new_vertex.position = size_list_vertex
                    self.list_vertex.append(new_vertex)
                    self.list_previsit.append(self.pos_actual_vertex)
                    pre_visit_vertex = self.list_vertex[self.pos_actual_vertex]
                    self.pos_actual_vertex = size_list_vertex
                    direction_new_vertex = new_vertex.get_direction()
                    pre_visit_vertex.mark(direction_new_vertex)
                    edge = Edge(pre_visit_vertex, new_vertex, direction_new_vertex)
                    self.list_edge.append(edge)
                    vertex = new_vertex
            else:
                new_vertex.position = size_list_vertex
                self.list_vertex.append(new_vertex)
                self.list_previsit.append(0)
                vertex = new_vertex
        return vertex

    def insert_edge(self, edge):
        if edge is not None and isinstance(edge, Edge):
            self.list_edge.append(edge)

    def get_list_vertex(self):
        return self.list_vertex

    def get_list_edge(self):
        return self.list_edge

    def get_size_list_vertex(self):
        return len(self.list_vertex)

    def get_vertex(self, position):
        vertex = None
        if position >= 0 and position < self.get_size_list_vertex():
            vertex = self.list_vertex[position]
        return vertex

    def get_size_list_edge(self):
        return len(self.list_edge)

    def get_connected_vertexs(self, vertex):
        list = []
        for i in range(0, len(self.list_edge)):
            [v1, v2] = self.list_edge[i].get_vertexs()
            if(v1 == vertex):
                list.append(self.list_vertex.index(v2))
            elif(v2 == vertex):
                list.append(self.list_vertex.index(v1))

        return list

    def print_list(self, list):
        for item in list:
            print item

    def __str__(self):
        print 'list_edge: ', self.list_edge
        return str(self.list_vertex)

