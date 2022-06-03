from game.casting.actor import Actor
from game.shared.point import Point

class Gem(Actor):
    """
    A helpful object that falls from the sky.
    
    The responsibility of Gem is to remove itself and add a score point.

    Attributes:
        
    """
    def __init__(self):
        super().__init__()
        self._text = "*"
        self._points = 1
        self._velocity = Point(0, 3)

    def get_points(self):
        return self._points

