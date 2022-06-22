import constants
from game.casting.actor import Actor
from game.shared.point import Point


class Cycle(Actor):
    """
    A long limbless reptile.
    
    The responsibility of cycle is to move itself.

    Attributes:
        _points (int): The number of points the food is worth.
    """
    def __init__(self, player_num: int = 0):
        super().__init__()
        self._player_num = player_num
        self._segments = []
        if not self._player_num: # player 1 returns false
            self._primary_color = constants.GREEN
        else:
            self._primary_color = constants.RED
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
        if self._player_num == 0:
            x = int(constants.MAX_X * 1/4)
        else:
            x = int(constants.MAX_X * 3/4)
        y = int(constants.MAX_Y / 2)

        # for i in range(constants.TRAIL_LENGTH):
        #     # TODO certain things here should only happen for the head and not the trail
        #     segment = Actor()
        #     # head/trail changes
        #     if i == 0: # if head
        #         segment.set_velocity(Point(1 * constants.CELL_SIZE, 0))
        #         segment.set_text("O")
        #     else:
        #         segment.set_text("#")
        #     segment.set_color(self._primary_color)
        #     segment.set_position(Point(x, y + i * constants.CELL_SIZE))
        #     self._segments.append(segment)

        for i in range(constants.TRAIL_LENGTH):
            # TODO certain things here should only happen for the head and not the trail

            segment = Actor()
            # head/trail changes

            if i == 0: # if head
                
                segment.set_velocity(Point(1 * constants.CELL_SIZE, 0))
                segment.set_text("O")
                # segment.set_color(constants.RED)
            else:
                segment.set_text("#")
                    
            segment.set_position(Point(x - i * constants.CELL_SIZE, y))
            segment.set_velocity(Point(1 * constants.CELL_SIZE, 0))
            if self._player_num == 0:
                segment.set_color(constants.BLUE)
            else:
                segment.set_color(constants.YELLOW)
            self._segments.append(segment)

    def reset_body(self):
        self._segments = []
        self._prepare_body()
