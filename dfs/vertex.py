
class Vertex(object):

    def __init__(self, data_sensor=None, position=None):
        self.position = position
        self.edges = []
        #[North, south, east, westh]
        self.visitateds = [False, False, False, False]
        self.init_state = None
        #direction is char
        self.direction = None
        self.pre_visit = 0
        self.post_visit = 0
        self.POSITION_DIRECTION = {'N':0, 'S':1, 'E':2, 'W':3}
        self.DIRECTION = ['N', 'S', 'E', 'W']
        self.LEFT_RIGHT_DIRECTIONS = {'N':['N', 'W', 'E'], 'S':['S', 'E', 'W'], 'E':['E', 'N', 'S'], 'W':['W', 'S', 'N']}
        self.initialize_data(data_sensor)

    def set_position(self, position):
        self.position = position

    def initialize_data(self, data_sensor):
        try:
            if data_sensor and len(data_sensor) == 2:
                self.init_state = data_sensor[0]
                self.direction = data_sensor[1]
                self.mark(self.get_opposite(self.direction))
                self.mark_directions()
        except Exception as e:
            print 'vertex: ', e
        #print 'visiteds', self.visitateds

    def mark_directions(self):
        directions = self.LEFT_RIGHT_DIRECTIONS[self.direction]
        pos = 0
        for state in self.init_state:
            if not state:
               self.mark(directions[pos])
            pos += 1

    def get_opposite(self, direction):
        if direction == 'N':
            opposite_direction = 'S'
        elif direction == 'S':
            opposite_direction = 'N'
        elif direction == 'E':
            opposite_direction = 'W'
        else:
            opposite_direction = 'E'
        return opposite_direction

    def get_direction(self):
        return self.direction

    def get_direction_movement(self):
        try:
            value = self.visitateds.index(False)
            position = self.DIRECTION[value]
        except Exception as e:
            print 'exception of "get_direction_movement: "', e
            position = None
            #position = self.get_opposite(self.direction)
        return position

    def get_position(self):
        return self.position

    def get_visitateds(self, pos):
        return self.visitateds[pos]

    def set_pre_visit(self, value):
        self.pre_visit = value

    def set_post_visit(self, value):
        self.post_visit = value

    def set_visited(self, pos):
        self.visitateds[pos] = not self.visitateds[pos]

    def mark(self, direction):
        position = self.POSITION_DIRECTION[direction]
        self.visitateds[position] = True

    def __str__(self):
        return str(self.__dict__)

    def __eq__(self, other):
        answer = False
        if other is not None and isinstance(other, Vertex):
            #answer = self.__dict__ == other.__dict__
            answer = self.position == other.position
        return answer
