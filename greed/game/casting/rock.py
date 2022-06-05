from game.casting.actor import Actor
from game.shared.point import Point

class Rock(Actor):
    """
    A harmful object that falls from the sky.
    
    The responsibility of Rock is to remove itself and subtract a score point.

    Attributes:
        _text (string): The text to display
        _velocity (Point): The speed and direction
        _points (int): How much the game's score will change upon interaction
        
    """
    def __init__(self):
        super().__init__()
        self._text = "O"
        self._points = -1
        self._velocity = Point(0, 4)

    def get_points(self):
        return self._points