from game.casting.actor import Actor
from game.casting.cast import Cast

from game.directing.director import Director

from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService

from game.shared.color import Color
from game.shared.point import Point

FRAME_RATE = 12
MAX_X = 900
MAX_Y = 600
CELL_SIZE = 15
FONT_SIZE = 15
COLS = MAX_X / CELL_SIZE
ROWS = MAX_Y / CELL_SIZE
CAPTION = "Greed - Team 02"
WHITE = Color(255, 255, 255)


def main():

    # create the cast
    cast = Cast()

    # create the banner
    banner = Actor()
    banner.set_text("SCORE: ")
    banner.set_font_size(FONT_SIZE*2)
    banner.set_color(Color(255, 0, 0))
    banner.set_position(Point(CELL_SIZE, 0))
    cast.add_actor("banners", banner)

    #create the player
    x = int(MAX_X / 2) #middle of screen
    y = MAX_Y-100-(CELL_SIZE*2) # bottom of screen
    # Readjusting bottom Y minus 30 so the player is visible enough
    
    position = Point(x, y)

    player = Actor()

    # drawing a little spacial vessel
    player.set_text("\n |\ndb\n|  |") 
    
    player.set_font_size(FONT_SIZE)
    player.set_color(WHITE)
    player.set_position(position)
    cast.add_actor("players", player)

    # start the game
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(
        CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard_service, video_service, CELL_SIZE, FONT_SIZE)
    director.start_game(cast)


if __name__ == "__main__":
    main()
