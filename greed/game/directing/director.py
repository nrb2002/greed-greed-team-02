import random

from game.casting.rock import Rock
from game.casting.gem import Gem

from game.shared.color import Color
from game.shared.point import Point




"""
    Update the code and the comments as you change the code for your game.  You will be graded on following the
    Rules listed and your program meets all of the Requirements found on 
    https://byui-cse.github.io/cse210-course-competency/inheritance/materials/greed-specification.html
"""

    #Let's only do things to get_inputs and do_updates if we can help it

class Director:
    """A person who directs the game. 

    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _keyboard_service (KeyboardService): For getting directional input.
        _video_service (VideoService): For providing video output.
        _score (int): The current score of the game
        _timer
        _timer_interval
        _cell_size
        _cols
        _font
    """

    def __init__(self, keyboard_service, video_service, cell_size, font_size):
        """Constructs a new Director using the specified keyboard and video services.

        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
            video_service (VideoService): An instance of VideoService.
        """
        self._keyboard_service = keyboard_service
        self._video_service = video_service
        self._score = 0
        self._timer = 0
        self._timer_interval = 6
        self._cell_size = cell_size
        self._cols = self._video_service.get_width() / cell_size #number of columns
        self._font = font_size
        

    def start_game(self, cast):
        """Starts the game using the given cast. Runs the main game loop.

        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.open_window()
        while self._video_service.is_window_open():
            self._get_inputs(cast)
            self._do_updates(cast)
            
            self._do_outputs(cast)
        self._video_service.close_window()

    def _get_inputs(self, cast):
        """Gets directional input from the keyboard and applies it to the player.

        Args:
            cast (Cast): The cast of actors.
        """
        player = cast.get_first_actor("players")
        velocity = self._keyboard_service.get_direction()
        player.set_velocity(velocity)

    def _do_updates(self, cast):
        """Updates the player's position and resolves any collisions with artifacts.

        Args:
            cast (Cast): The cast of actors.
        """
        banner = cast.get_first_actor("banners")
        player = cast.get_first_actor("players")
        objects = cast.get_actors("objects")

        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        player.move_next(max_x, max_y)


        player_x = player.get_position().get_x()
        player_y = player.get_position().get_y()
        
        for object in objects:
            object.move_next(max_x, max_y)

            object_x = object.get_position().get_x()
            object_y = object.get_position().get_y()

            if ((object_x - self._font/2 < player_x < object_x + self._font/2) and (object_y - self._font/2 < player_y < object_y + self._font/2)):
                self._score += object.get_points()
                cast.remove_actor("objects", object)
                banner.set_text(f"SCORE: {self._score}")
            #when object is off screen, remove it
            elif player_y == max_y:
                cast.remove_actor("objects", object)

        self._timer += 1
        if self._timer % self._timer_interval == 0:
            self._new_object(cast)

        

                  

    def _do_outputs(self, cast):
        """Draws the actors on the screen.

        Args:
            cast (Cast): The cast of actors.
        """

        #Let's try not to touch or add anything here without good reason
        

        self._video_service.clear_buffer()
        actors = cast.get_all_actors()
        self._video_service.draw_actors(actors)
        self._video_service.flush_buffer()

    def _new_object(self, cast):
        #true for rock, false for gem
        is_rock = random.choice([Gem, Rock])

        x = random.randint(1, self._cols - 1)
        y = 1 #we will be changing this to the top of the screen
        position = Point(x, y)
        position = position.scale(self._cell_size)

        #check for collision with another generated object and make sure there is no conflict

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(r, g, b)

        object = is_rock()

        object.set_font_size(self._font)
        object.set_color(color)
        object.set_position(position)
        cast.add_actor("objects", object)
        