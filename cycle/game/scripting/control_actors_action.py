import constants
from game.scripting.action import Action
from game.shared.point import Point
from game.casting.snake import Snake
from game.casting.snake_two import Snake_two


class ControlActorsAction(Action):
    """
    An input action that controls the snake.
    
    The responsibility of ControlActorsAction is to get the direction and move the snake's head.

    Attributes:
        _keyboard_service (KeyboardService): An instance of KeyboardService.
    """

    def __init__(self, keyboard_service):
        """Constructs a new ControlActorsAction using the specified KeyboardService.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
        """
        self._keyboard_service = keyboard_service
        self._direction = Point(constants.CELL_SIZE, 0)
        self._snake = Snake()
        self._snake_two = Snake_two()

    def execute(self, cast, script):
        """Executes the control actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        # left
        if self._keyboard_service.is_key_down('a'):
            self._direction = Point(-constants.CELL_SIZE, 0)

            for i in range(1):
                self._snake.grow_tail(i + 1)
        
        # right
        if self._keyboard_service.is_key_down('d'):
            self._direction = Point(constants.CELL_SIZE, 0)

            for i in range(1):
                self._snake.grow_tail(i + 1)

        # up
        if self._keyboard_service.is_key_down('w'):
            self._direction = Point(0, -constants.CELL_SIZE)

            for i in range(1):
                self._snake.grow_tail(i + 1)
        
        # down
        if self._keyboard_service.is_key_down('s'):
            self._direction = Point(0, constants.CELL_SIZE)

            for i in range(1):
                self._snake.grow_tail(i + 1)

        # up
        if self._keyboard_service.is_key_down('i'):
            self._direction = Point(0, -constants.CELL_SIZE)

            for i in range(1):
                self._snake_two.grow_tail(i + 1)
        
        # down
        if self._keyboard_service.is_key_down('k'):
            self._direction = Point(0, constants.CELL_SIZE)

            for i in range(1):
                self._snake_two.grow_tail(i + 1)
        
        # left
        if self._keyboard_service.is_key_down('j'):
            self._direction = Point(-constants.CELL_SIZE, 0)

            for i in range(1):
                self._snake_two.grow_tail(i + 1)
        
        # right
        if self._keyboard_service.is_key_down('l'):
            self._direction = Point(constants.CELL_SIZE, 0)
        
            for i in range(1):
                self._snake_two.grow_tail(i + 1)

        snake = cast.get_first_actor("snakes")
        # snake_two = cast.get_first_actor("snakes_two")
        snake.turn_head(self._direction)