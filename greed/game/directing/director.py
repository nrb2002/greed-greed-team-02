import random


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
    """

    def __init__(self, keyboard_service, video_service):
        """Constructs a new Director using the specified keyboard and video services.

        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
            video_service (VideoService): An instance of VideoService.
        """
        self._keyboard_service = keyboard_service
        self._video_service = video_service
        self._score = 0

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
        """Gets directional input from the keyboard and applies it to the robot.

        Args:
            cast (Cast): The cast of actors.
        """
        robot = cast.get_first_actor("robots")
        velocity = self._keyboard_service.get_direction()
        robot.set_velocity(velocity)

    def _do_updates(self, cast):
        """Updates the robot's position and resolves any collisions with artifacts.

        Args:
            cast (Cast): The cast of actors.
        """
        banner = cast.get_first_actor("banners")
        robot = cast.get_first_actor("robots")
        objects = cast.get_actors("objects")

        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        robot.move_next(max_x, max_y)
        
        for object in objects:
            object.move_next(max_x, max_y)
            position = object.get_position()
            y_value = position.get_y()
            if robot.get_position().equals(object.get_position()):
                self._score += object.get_points()
                cast.remove_actor("objects", object)
                banner.set_text(f"{self._score}")
            #when object is off screen, remove it
            elif y_value == max_y:
                cast.remove_actor("objects", object)

                  

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

    def new_object(self, cast):
        #true for rock, false for gem
        is_rock = random.choice([Gem, Rock])

        x = random.randint(1, COLS - 1)
        y = 1 #we will be changing this to the top of the screen
        position = Point(x, y)
        position = position.scale(CELL_SIZE)

        #check for collision with another generated object and make sure there is no conflict

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(r, g, b)

        object = is_rock()

        object.set_font_size(FONT_SIZE)
        object.set_color(color)
        object.set_position(position)
        cast.add_actor("objects", object)
        