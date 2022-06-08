from game.casting.actor import Actor
from game.shared.point import Point

class Gem(Actor):
    """
    A helpful object that falls from the sky.
    
    The responsibility of Gem is to remove itself and add a score point.

    Attributes:
        _text (string): The text to display
        _velocity (Point): The speed and direction
        _points (int): How much the game's score will change upon interaction
        
    """
    def __init__(self):
        """Constructs a new Gem."""
        super().__init__()
        self._text = "*"
        self._points = 1
        self._velocity = Point(0, 4)

    def get_points(self):
        """Returns:
            int: the value of the gem in score points
        """
        return self._points