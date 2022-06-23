# from game.scripting.action import Action

# class RestRoundAction(Action):

#     def __init__(self):
#         self._cycles = self._cast.get_actors("cycles")
#         self._cycle0 = self._cycles[0]
#         self._cycle1 = self._cycles[1]
#         self._scores = self._cast.get_actors("scores")
#         self._score0 = self._scores[0]
#         self._score1 = self._scores[0]
#         # self._collision = handle_collisions_action()

#     def execute(self, cast, script):

#         self._cycle0.reset_body()
#         self._cycle1.reset_body()
#         self._score0.reset_points()
#         self._score1.reset_points()
#         # self._cast.reset_collisions()