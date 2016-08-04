
class Vertex(object):
    def __init__(self, imu, data_sensor):
        self.position = imu
        self.sensor_data = data_sensor
        #state of north, south, east, west
        self.states = [False, False, False, False]

    def get_position(self):
        return self.position

    def __str__(self):
        return str(self.__dict__)

    def __eq__(self, other):
        answer = False
        if other is not None:
            answer = self.__dict__ == other.__dict__
        return answer





