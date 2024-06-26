# import every game module if you are not sure which to use
import pygame
import pyzero
import pgzero
# importing random
from random import randint

# pgzrun /Users/bina/Code?/Exercise/Game?/"Shoot the apple"/"Shoot-the-Apple"/Shoot.py


# Introducing an Actor
"""In computer games development,
a sprite is an object, like a coin or an enemy character, 
that is controlled by code. Actors in Python are like Sprites in Scratch. 
An Actor can be drawn on the screen, moved around, 
and even interact with other Actors in the game. 
Each Actor is given a “script” (the Python code) to tell it how to behave in the game."""

apple = Actor('apple') # The apple inside Actor is an img name, this Actor will look for it self
# alien = Actor('what da dog doin')

score = 0

def draw():
    screen.clear()
    apple.draw()
    screen.draw.text("Screen" + str(score), color="white", topleft=(10, 10))
    screen.draw.text("Clicl on the apple to shoot!", color="white", topright=(590, 10))
    #alien.draw()

# Positiong Apple location / If not used then by defealt the location of apple is topleft.
def place_apple():
    """apple.x = 300
    apple.y = 200""" # use this mmethod if you want to provide fix position
# If you want an apple to be any random place than use Random module
def place_apple():
    apple.x = randint(10, 500)
    apple.y = randint(10, 500)

"""def place_alien():
    alien.x = randint(10, 500)
    alien.y = randint(10, 500)"""

# on_mouse_down(inbuilt fuction that detect click)
# pos is position 
def on_mouse_down(pos):
    global score #accesing a global score

    if apple.collidepoint(pos): # This code checks if the apple and the mouse cursor are in the same position. If they are, the message is displayed.
        print("Good Shoot!")
        score += 1
        place_apple()
    
    # What if you missed the shot!?
    else:
        if score < 5:
            print("Game Over")
            quit()
        else:
            print("Missed! - 5 points")
            score -= 5

# Running the Function
place_apple()
#place_alien()