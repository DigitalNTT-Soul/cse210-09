import config
from game.casting.actor import Actor
from game.shared.point import Point


class Cycle(Actor):
    """
    A long limbless reptile.
    
    The responsibility of cycle is to move itself.

    Attributes:
        _points (int): The number of points the food is worth.
    """
    def __init__(self, player_num: int = 0, player_count: int = 2):
        super().__init__()
        self._player_num = player_num
        self._player_count = player_count
        self._segments = []
        match player_num:
            case 0:
                self._primary_color = config.GREEN
            case 1:
                self._primary_color = config.RED
            case 2:
                self._primary_color = config.BLUE
            case 3:
                self._primary_color = config.YELLOW
        
        self._prepare_body()
        

    def get_segments(self):
        return self._segments

    def move_next(self):
        
        # move all segments
        for segment in self._segments:
            segment.move_next()
        # update velocities
        for i in range(len(self._segments) - 1, 0, -1):
            trailing = self._segments[i]
            previous = self._segments[i - 1]
            velocity = previous.get_velocity()
            trailing.set_velocity(velocity)
        self.grow_tail(1)

    def get_head(self):
        return self._segments[0]

    def grow_tail(self, number_of_segments):
        for i in range(number_of_segments):
            tail = self._segments[-1]
            velocity = tail.get_velocity()
            offset = velocity.reverse()
            position = tail.get_position().add(offset)
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text("#")
            segment.set_color(self._primary_color)
            self._segments.append(segment)

    def turn_head(self, velocity):
        self._segments[0].set_velocity(velocity)
    
    def _prepare_body(self):
        head = Actor()
        head.set_position(Point(int(config.MAX_X * (self._player_num + 1)/(self._player_count + 1)), int(config.MAX_Y / 2)))
        head.set_velocity(Point(config.CELL_SIZE, 0))
        head.set_text("O")
        head.set_color(config.WHITE)

        self._segments.append(head)

    def reset_body(self):
        self._segments = []
        self._prepare_body()
