from game.casting.actor import Actor


class Rock(Actor):
    """
    A harmful object that falls from the sky.
    
    The responsibility of Rock is to remove itself and subtract a score point.

    Attributes:
        
    """
    def __init__(self):
        super().__init__()
        self._text = "O"
        self._points = -1

