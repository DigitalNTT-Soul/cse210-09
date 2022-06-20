import constants
from game.casting.actor import Actor
from game.shared.point import Point


class Snake_two(Actor):
    """
    A long limbless reptile.
    
    The responsibility of Snake is to move itself.

    Attributes:
        _points (int): The number of points the food is worth.
    """
    def __init__(self):
        super().__init__()
        self._segments_snake_two = []
        self._prepare_body()

    def get_segments(self):
        return self._segments_snake_two

    def move_next(self):
        # move all segments
        for segment in self._segments_snake_two:
            segment.move_next()
        # update velocities
        for i in range(len(self._segments_snake_two) - 1, 0, -1):
            trailing = self._segments_snake_two[i]
            previous = self._segments_snake_two[i - 1]
            velocity = previous.get_velocity()
            trailing.set_velocity(velocity)

    def get_head(self):
        return self._segments_snake_two[0]

    def grow_tail(self, number_of_segments):
        for i in range(number_of_segments):
            tail = self._segments_snake_two[-1]
            velocity = tail.get_velocity()
            offset = velocity.reverse()
            position = tail.get_position().add(offset)
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text("#")
            segment.set_color(constants.GREEN)
            self._segments_snake_two.append(segment)

    def turn_head(self, velocity):
        self._segments[0].set_velocity(velocity)
    
    def _prepare_body(self):
        x = int(constants.MAX_X / 2 - 675)
        y = int(constants.MAX_Y / 2)

        for i in range(constants.SNAKE_LENGTH):
            position = Point(x - i * constants.CELL_SIZE, y)
            velocity = Point(1 * constants.CELL_SIZE, 0)
            text = "8" if i == 0 else "#"
            color = constants.YELLOW if i == 0 else constants.GREEN
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text(text)
            segment.set_color(color)
            self._segments_snake_two.append(segment)