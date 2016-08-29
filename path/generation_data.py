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
        vertex = Vertex(position)
        self.graph.insert_vertex(vertex)


    def generate_edge(self):
        pass