from vertex import Vertex
from edge import Edge
import numpy as np

class Graph:

    def __init__(self, list_ver=[], list_edg=[]):
        self.list_vertex = list_ver
        self.list_edge = list_edg
        self.j = 1

    def insert_vertex(self, vertex):
        if(isinstance(vertex, Vertex) and vertex not in self.list_vertex):
            size_list_vertex = len(self.list_vertex)
            if(size_list_vertex > 0):
                vertex_1 = self.list_vertex[size_list_vertex - 1]
                self.list_vertex.append(vertex)
                edge = Edge(vertex_1, vertex)
                self.list_edge.append(edge)
            else:
                self.list_vertex.append(vertex)

    def insert_edge(self, edge):
        if edge is not None and isinstance(edge, Edge):
            self.list_edge.append(edge)

    def get_list_vertex(self):
        return self.list_vertex

    def get_list_edge(self):
        return self.list_edge

    def dfs(self, orig, dest):
        if(len(self.list_vertex) > 0 and len(self.list_edge) > 0):
            self.look(orig, [], dest)

    def look(self, vertex, stack, dest):
        if(not vertex.get_state(0)):
            vertex.set_state(0)
            vertex.set_pre_visit(self.j)
            stack.append(vertex)
            if(vertex is not dest):
                list_conn_vertex = self.get_connected_vertexs(vertex)
                #print list_conn_vertex
                pos = self.list_vertex.index(vertex)
                #print pos
                if(len(list_conn_vertex) == 0):
                    self.j += 1
                    self.list_vertex[pos].set_post_visit(self.j)
                    stack.pop()
                else:
                    for i in range(0, len(list_conn_vertex)):
                        self.j += 1
                        self.look(self.list_vertex[list_conn_vertex[i]], stack, dest)
                self.j += 1
                self.list_vertex[pos].set_post_visit(self.j)
            else:
                print "end"
                self.print_list(stack)
        #print "imprimiendo"
        #self.print_list(self.list_vertex)

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

