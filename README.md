# Greed
Greed is a game in which the player seeks to gather as many falling gems as possible. The game continues as long as the player wants more!

Rules
Greed is played according to the following rules.

Gems (*) and rocks (o) randomly appear and fall from the top of the screen.
The player (#) can move left or right along the bottom of the screen.
If the player touches a gem they earn a point.
If the player touches a rock they lose a point.
Gems and rocks are removed when the player touches them.
The game continues until the player closes the window.

## Getting Started
Make sure you have Python 3.8.0 or newer installed and running on your machine. Open a terminal and browse to the project's root folder. Start the program by running the following command.
```
python3 greed 
```
You can also run the program from an IDE like Visual Studio Code. Start your IDE and open the project folder. Select the main module inside the hunter folder and click the "run" icon.

## Project Structure
The project files and folders are organized as follows:
```
root                     (project root folder)
+-- greed               (source code for game)
  +-- game 
    +-- casting
        +-- actor           (specific classes)
        +-- cast            (specific classes)
        +-- gem             (specific classes)
        +-- rock            (specific classes)
    +-- directing
        +-- director        (specific classes) 
    +-- services
       +-- keyboard_service (specific classes)
       +-- video_service    (specific classes)
    +-- shared
        +-- color           (specific classes)
        +-- point           (specific classes) 
  +-- __main__.py       (program entry point)
+-- README.md           (general info)
```

## Required Technologies
* Python 3.8.0

## Authors
* George Blanchard
* Nathan Rolim