from graph import Graph
from vertex import Vertex
from edge import Edge

v1 = Vertex(("x", "y"), "data_sensor")
v2 = Vertex(("x1", "y1"), "data_sensor1")
edge = Edge(v1, v2)
print edge
print v1 == v2
graph = Graph()
graph.insert_vertex(v1)
graph.insert_edge(edge)
print graph.get_list_vertex()
print graph.get_list_edge()