import config
from game.scripting.control_actors_action import ControlActorsAction
from game.scripting.move_actors_action import MoveActorsAction
from game.scripting.handle_collisions_action import HandleCollisionsAction
from game.scripting.draw_actors_action import DrawActorsAction
from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService
from game.services.sound_service import SoundService
from game.casting.cast import Cast
from game.casting.cycle import Cycle
from game.casting.score import Score
from game.scripting.script import Script


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _video_service (VideoService): For providing video output.
    """

    def __init__(self):
        """Constructs a new Director using the specified video service.
        
        Args:
            video_service (VideoService): An instance of VideoService.
        """
        self._keyboard_service = KeyboardService()
        self._video_service = VideoService()
        self._sound_service = SoundService()
        self._cast = Cast()
        self._script = Script()
        
    def start_game(self):
        """Starts the game using the given cast and script. Runs the main game loop.

        Args:
            cast (Cast): The cast of actors.
            script (Script): The script of actions.
        """
        # self._sound_service.play_wilhelm()
        self._video_service.open_window()
        self._build_game()
        while self._video_service.is_window_open():
            self._sound_service.play_music()
            self._execute_actions("input")
            self._execute_actions("update")
            self._execute_actions("output")
        self._video_service.close_window()

    def _build_game(self):
        for i in range(config.PLAYER_COUNT):
            self._cast.add_actor("cycles", Cycle(i, config.PLAYER_COUNT))

        self._cast.add_actor("scores", Score())

        self._script.add_action("input", ControlActorsAction(self._keyboard_service))
        self._script.add_action("update", MoveActorsAction())
        self._script.add_action("update", HandleCollisionsAction())
        self._script.add_action("output", DrawActorsAction(self._video_service))

    def _execute_actions(self, group):
        """Calls execute for each action in the given group.
        
        Args:
            group (string): The action group name.
            cast (Cast): The cast of actors.
            script (Script): The script of actions.
        """
        actions = self._script.get_actions(group)    
        for action in actions:
            action.execute(self._cast, self._script)