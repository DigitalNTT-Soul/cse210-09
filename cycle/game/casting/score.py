from game.casting.actor import Actor
from game.shared.point import Point
import config


class Score(Actor):
    """
    A record of points made or lost. 
    
    The responsibility of Score is to keep track of the points the player has earned by eating food.
    It contains methods for adding and getting points. Client should use get_text() to get a string 
    representation of the points earned.

    Attributes:
        _points (int): The points earned in the game.
    """
    def __init__(self, player_num: int = 0, player_count: int = 2):
        super().__init__()
        self._player_num = player_num
        self._player_count = player_count
        self._points = 0
        self.add_points(0)
        match player_num:
                    case 0:
                        self.set_color(config.GREEN)
                        self.set_position(Point(int(config.MAX_X + 5), int(config.MAX_Y)))
                        self.set_font_size(25)
                    case 1:
                        self.set_color(config.RED)
                        self.set_position(Point(int(790), int(config.MAX_Y)))
                        self.set_font_size(25)
                    case 2:
                        self.set_color(config.BLUE)
                        self.set_position(Point(int(config.MAX_X), int(600)))
                        self.set_font_size(25)
                    case 3:
                        self.set_color(config.YELLOW)
                        self.set_position(Point(int(800), int(600)))
                

    def add_points(self, points):
        """Adds the given points to the score's total points.
        
        Args:
            points (int): The points to add.
        """
        self._points += points
        self.set_text(f"Score: {self._points}")

    def reset_points(self):
        self._points = 0
