from graph import Graph
from vertex import Vertex
from edge import Edge

v1 = Vertex(("x1", "y1"), "data_sensor1")
v2 = Vertex(("x2", "y2"), "data_sensor2")
v3 = Vertex(("x3", "y3"), "data_sensor3")
v4 = Vertex(("x4", "y4"), "data_sensor4")
v5 = Vertex(("x5", "y5"), "data_sensor5")
v6 = Vertex(("x6", "y6"), "data_sensor6")
edge1 = Edge(v1, v2)
edge2 = Edge(v1, v3)
edge3 = Edge(v2, v3)
edge4 = Edge(v1, v4)
edge5 = Edge(v2, v5)
edge6 = Edge(v4, v5)
edge7 = Edge(v4, v6)
print v6 == v6
list_vertex = [v1,v2,v3,v4, v5, v6]
graph = Graph(list_vertex, [edge1, edge2, edge3, edge4, edge5, edge6, edge7])

#graph.insert_vertex(v1)
#graph.insert_edge(edge)
#print graph.get_list_vertex()
#print graph.get_list_edge()
graph.dfs(v3, v6)