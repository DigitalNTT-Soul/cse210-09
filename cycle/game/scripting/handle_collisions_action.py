import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point
from game.services.sound_service import SoundService

class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the cycle collides
    with the food, or the cycle collides with its segments, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False

    def get_game_over_bool(self):
        return self._is_game_over

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            self._handle_segment_collision(cast)
    
    def _handle_segment_collision(self, cast):
        """Sets the game over flag if the cycle collides with one of its segments.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
<<<<<<< HEAD
        cycles = cast.get_actors("cycles")
        cycle0 = cycles[0]
        cycle1 = cycles[1]
=======
        snake = cast.get_first_actor("snakes")
        head = snake.get_segments()[0]
        segments = snake.get_segments()[1:]
       
>>>>>>> 31488088f6863e9988c72dde3280a97eb4dc92f2

        head0 = cycle0.get_segments()[0]
        segments0 = cycle0.get_segments()[1:]

        head1 = cycle1.get_segments()[0]
        segments1 = cycle1.get_segments()[1:]
        
<<<<<<< HEAD
        for segment in segments0:
            if (head0.get_position().equals(segment.get_position()) or
                head1.get_position().equals(segment.get_position())):
                self._handle_game_over(cast, cycles)
        
        for segment in segments1:
            if (head0.get_position().equals(segment.get_position()) or
                head1.get_position().equals(segment.get_position())):
                self._handle_game_over(cast, cycles)
=======
        for segment in segments:
            if head_snake_two.get_position().equals(segment.get_position()):
                self._is_game_over = True
                welhelm = SoundService()
                welhelm.play_wilhelm()

        for seg in segments_snake_two:
            if head.get_position().equals(seg.get_position()):
                self._is_game_over = True
                welhelm = SoundService()
                welhelm.play_wilhelm()
        
        # Cyclist 1 loses if he runs into his own trail.        
        for segment in segments:
            if head.get_position().equals(segment.get_position()):
                self._is_game_over = True
                welhelm = SoundService()
                welhelm.play_wilhelm()


        # Cyclist 2 loses if he runs into his own trail
        for segment in segments_snake_two:
            if head_snake_two.get_position().equals(segment.get_position()):
                self._is_game_over = True
                welhelm = SoundService()
                welhelm.play_wilhelm()


>>>>>>> 31488088f6863e9988c72dde3280a97eb4dc92f2
        
    def _handle_game_over(self, cast, cycles):
        """Shows the 'game over' message and turns the cycle and food white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        segments0 = cycles[0].get_segments()
        segments1 = cycles[1].get_segments()

        x = int(constants.MAX_X / 2)
        y = int(constants.MAX_Y / 2)
        position = Point(x, y)

        message = Actor()
        message.set_text("Game Over!")
        message.set_position(position)
        cast.add_actor("messages", message)

        for segment in segments0:
            segment.set_color(constants.WHITE)

        for segment in segments1:
            segment.set_color(constants.WHITE)
           


        