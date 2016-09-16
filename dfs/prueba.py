from graph import Graph
from vertex import Vertex
from edge import Edge
from path.generation_data import Generator_Data

list_data = [
    [[[True, False, False],'N'], False],
    [[[False, True, False],'N'], False],
    [[[False, True, False],'W'], False],
    [[[True, False, True],'S'], False],
    [[[False, False, True],'S'], False],
    [[[True, False, True],'W'], False],
    [[[False, False, True],'N'], False],
    [[[False, True, False],'E'], False],
    [[[True, True, False],'N'], False],
    [[[False, False, False],'N'], False],
    [[[True, False, True],'S'], False],
    [[[False, False, True],'W'], False],
    [[[False, False, True],'N'], False],
    [[[False, False, True],'E'], False],
    [[[False, True, False],'S'], False],
    [[[False, True, False],'E'], False],
    [[[True, True, False],'N'], False],
    [[[False, False, False],'N'], False],
    [[[True, False, True],'S'], False],
    [[[False, False, True],'W'], False],
    [[[False, True, False],'N'], False],
    [[[False, False, True],'W'], False],
    [[[False, False, True],'N'], False],
    [[[False, True, True],'E'], False],
    [[[True, True, True],'N'], True]
]

generator_data = Generator_Data()
for data in list_data:
    dir_m = generator_data.generate_node(data)
    print dir_m
print 'graph: ', generator_data.graph