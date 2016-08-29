
class Vertex(object):

    def __init__(self, imu, data_sensor=None):
        self.position = imu
        self.sensor_data = data_sensor
        #state of north, south, east, west
        self.states = [False, False, False, False]
        self.pre_visit = 0
        self.post_visit = 0

    def get_position(self):
        return self.position

    def get_state(self, pos):
        return self.states[pos]

    def set_pre_visit(self, value):
        self.pre_visit = value

    def set_post_visit(self, value):
        self.post_visit = value

    def set_state(self, pos):
        self.states[pos] = not self.states[pos]

    def __str__(self):
        return str(self.__dict__)

    def __eq__(self, other):
        answer = False
        if other is not None:
            answer = self.__dict__ == other.__dict__
        return answer




