import numpy as np
from dfs.vertex import Vertex
from dfs.edge import Edge
from dfs.graph import Graph

class Generator_Data():

    def __init__(self):
        self.graph = Graph()
        self.come_back = False

    def generate_node(self, data):
        '''
        data_sensor = data["distance_sensor"]
        time = data["time"]
        end = data["end"]'''
        data_sensor = data[0]
        end = data[1]
        if not end:
            vertex = Vertex(data_sensor)
            vertex = self.graph.insert_vertex(vertex, self.come_back)
            #obtiene la direccion a la cual se tiene que mover el auto y la posicion a la que tiene que volver si no existe camino
            direction_movement = self.dfs(vertex)
        else:
            direction_movement = None
        return direction_movement

    def dfs(self, vertex):
        direction_movement = None
        size_list_vertex = self.graph.get_size_list_vertex()
        if (size_list_vertex >= 1):
            direction_movement = vertex.get_direction_movement()
            self.come_back = direction_movement is None
            if self.come_back:
                direction_movement = vertex.get_opposite(vertex.direction)
        return direction_movement

    '''
    def look(self, vertex_1, vertex_2):
        direction_movement = vertex_2.get_direction_movement()
        #compare direction_movement if None -> retro, else to follow
        position = None
        if (direction_movement is None):
            direction_movement = vertex_2.get_opposite_direction(vertex_2.get_direction)
            position = vertex_1.get_position()

            if (vertex_1 is not vertex_2):
                list_conn_vertex = self.get_connected_vertexs(vertex_1)
                # print list_conn_vertex
                pos = self.list_vertex.index(vertex_1)
                # print pos
                if (len(list_conn_vertex) == 0):
                    self.j += 1
                    self.list_vertex[pos].set_post_visit(self.j)
                    stack.pop()
                else:
                    for i in range(0, len(list_conn_vertex)):
                        self.j += 1
                        self.look(self.list_vertex[list_conn_vertex[i]], stack, vertex_2)
                self.j += 1
                self.list_vertex[pos].set_post_visit(self.j)
            else:
                print "end"
                self.print_list(stack)
                # print "imprimiendo"
                # self.print_list(self.list_vertex)
        return direction_movement, position'''
