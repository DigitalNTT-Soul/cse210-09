import config
from game.scripting.action import Action
from game.shared.point import Point
from game.casting.cycle import Cycle

class ControlActorsAction(Action):
    """-
    An input action that controls the cycle.
    
    The responsibility of ControlActorsAction is to get the direction and move the cycle's head.

    Attributes:
        _keyboard_service (KeyboardService): An instance of KeyboardService.
    """

    def __init__(self, keyboard_service):
        """Constructs a new ControlActorsAction using the specified KeyboardService.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
        """
        self._keyboard_service = keyboard_service
        
        self._left = Point(-config.CELL_SIZE, 0)
        self._right = Point(config.CELL_SIZE, 0)
        self._up = Point(0, -config.CELL_SIZE)
        self._down = Point(0, config.CELL_SIZE)
        self._direction0 = self._up
        self._direction1 = self._up

    def execute(self, cast, script):
        """Executes the control actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """ 
        
        cycles = cast.get_actors("cycles")
        cycle0 = cycles[0]
        cycle1 = cycles[1]

        head0_velocity = cycle0.get_head().get_velocity()
        head1_velocity = cycle1.get_head().get_velocity()

        head0 = cycle0.get_head()
        head1 = cycle1.get_head()
        
        # # Player 1 horizontal velocity
        # x_vel = 0
        # if not (head0_velocity is self._left or head0_velocity is self._right):
        #     if not (self._keyboard_service.is_key_down('a') and self._keyboard_service.is_key_down('d')):   # make sure they're not both pressed at the same time

        # Cycle 0
        if self._direction0  is self._left:
            if self._keyboard_service.is_key_down('d'):
                self._direction0 = self._left

            if self._keyboard_service.is_key_down('a'):
                self._direction0 = self._left 

            if self._keyboard_service.is_key_down('w'):
                self._direction0 = self._up

            if self._keyboard_service.is_key_down('s'):
                self._direction0 = self._down 
              
        if  self._direction0 is self._right:
            if self._keyboard_service.is_key_down('a'):
                self._direction0 = self._right
           
            if self._keyboard_service.is_key_down('d'):
                self._direction0 = self._right

            if self._keyboard_service.is_key_down('w'):
                self._direction0 = self._up

            if self._keyboard_service.is_key_down('s'):
                self._direction0 = self._down       

        if  self._direction0 is self._up:
            if self._keyboard_service.is_key_down('s'):
                self._direction0 = self._up

            if self._keyboard_service.is_key_down('a'):
                self._direction0 = self._left 
 
            if self._keyboard_service.is_key_down('d'):
                self._direction0 = self._right

            if self._keyboard_service.is_key_down('w'):
                self._direction0 = self._up  

        if  self._direction0 is self._down:
            if self._keyboard_service.is_key_down('w'):
                self._direction0 = self._down
            
            if self._keyboard_service.is_key_down('a'):
                self._direction0 = self._left 
    
            if self._keyboard_service.is_key_down('d'):
                self._direction0 = self._right

            if self._keyboard_service.is_key_down('s'):
                self._direction0 = self._down

         # Cycle 1
        if self._direction1  is self._left:
            if self._keyboard_service.is_key_down('l'):
                self._direction1 = self._left

            if self._keyboard_service.is_key_down('j'):
                self._direction1 = self._left 

            if self._keyboard_service.is_key_down('i'):
                self._direction1 = self._up

            if self._keyboard_service.is_key_down('k'):
                self._direction1 = self._down 
              
        if  self._direction1 is self._right:
            if self._keyboard_service.is_key_down('j'):
                self._direction1 = self._right
           
            if self._keyboard_service.is_key_down('l'):
                self._direction1 = self._right

            if self._keyboard_service.is_key_down('i'):
                self._direction1 = self._up

            if self._keyboard_service.is_key_down('k'):
                self._direction1 = self._down 
               
        if  self._direction1 is self._up:
            if self._keyboard_service.is_key_down('k'):
                self._direction1 = self._up

            if self._keyboard_service.is_key_down('j'):
                self._direction1 = self._left 
 
            if self._keyboard_service.is_key_down('l'):
                self._direction1 = self._right

            if self._keyboard_service.is_key_down('i'):
                self._direction1 = self._up
            
        if  self._direction1 is self._down:
            if self._keyboard_service.is_key_down('i'):
                self._direction1 = self._down
            
            if self._keyboard_service.is_key_down('j'):
                self._direction1 = self._left 
    
            if self._keyboard_service.is_key_down('l'):
                self._direction1 = self._right

            if self._keyboard_service.is_key_down('k'):
                self._direction1 = self._down 
       

        # Cycle 0 
        
        # # left
        # if self._keyboard_service.is_key_down('a'):
        #     self._direction0 = self._left 
 
        # # right
        # if self._keyboard_service.is_key_down('d'):
        #     self._direction0 = self._right

        # # up
        # if self._keyboard_service.is_key_down('w'):
        #     self._direction0 = self._up

        # # down
        # if self._keyboard_service.is_key_down('s'):
        #     self._direction0 = self._down 

            
        # Cycle 1

        # # up
        # if self._keyboard_service.is_key_down('i'):
        #     self._direction1 = self._up
  
        # # down
        # if self._keyboard_service.is_key_down('k'):
        #     self._direction1 = self._down
  
        # # left
        # if self._keyboard_service.is_key_down('j'):
        #     self._direction1 = self._left
  
        # # right
        # if self._keyboard_service.is_key_down('l'):
        #     self._direction1 = self._right
        
        cycle0.turn_head(self._direction0)
        cycle1.turn_head(self._direction1)

    def reset_direction(self):
        self._direction0 = self._up
        self._direction1 = self._up