from vertex import Vertex

class Edge(object):
    def __init__(self, vertex_1, vertex_2):
        self.weigth = 0
        self.v1 = vertex_1
        self.v2 = vertex_2

    def get_vertexs(self):
        return [self.v1, self.v2]

    def get_weigth(self):
        return self.weigth

    def set_weigth(self, weigth_1):
        self.weigth = weigth_1

    def __str__(self):
        return str(self.__dict__)

    def __eq__(self, other):
        answer = None
        if other is not None:
            answer = self.__dict__ == other.__dict__
        return answer