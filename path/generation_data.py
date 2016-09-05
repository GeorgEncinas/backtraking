import numpy as np
from dfs.vertex import Vertex
from dfs.edge import Edge
from dfs.graph import Graph

class Generator_Data():

    def __init__(self):
        self.graph = Graph()

    def generate_node(self, data):
        time = data["time"]
        distance = data["distance"]
        #obtiene las coordenadas del centro del auto
        position = data["position"]
        #los angulos de los posibles caminos a los que se puede desplazar
        angles = data["angles"]
        #direccion del que esta viniendo el auto
        direction = data["direction"]
        vertex = Vertex(position)

        self.graph.insert_vertex(vertex, direction, angles)
        #obtiene el angulo de la direccion al cual se tiene que mover el auto
        angle_movement = self.graph.dfs(vertex, angles)
        return angle_movement

    def generate_edge(self):
        pass