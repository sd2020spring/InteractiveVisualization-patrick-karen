#! /usr/bin/env python
import time
import os, sys
import pygame
import random
import sys
from pygame.locals import *
from helpers import *

if not pygame.font:
     print('Warning, fonts disabled')
if not pygame.mixer:
     print('Warning, sound disabled')

class PyManMain:
    """The Main PyMan Class - This class handles the main
    initialization and creating of the Game."""

    def __init__(self, width=640,height=480):
        """Initialize PyGame"""
        pygame.init()
        """Set the window Size"""
        self.width = width
        self.height = height
        """Create the Screen"""
        self.screen = pygame.display.set_mode((self.width, self.height))

    def MainLoop(self):
        """This is the Main Loop of the Game"""

        """Load All of our Sprites"""
        self.LoadSprites()

        """tell pygame to keep sending up keystrokes when they are
        held down"""
        pygame.key.set_repeat(500, 30)

        """Create the background"""
        self.background = pygame.Surface(self.screen.get_size())  # Set background size
        self.background = self.background.convert()
        self.background.fill((135,206,235)) # Set background color to sky blue

        """Wait for user to move the bird around. If key was held down, move bird according (L, R, U, D)"""
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == KEYDOWN:
                    if ((event.key == K_RIGHT)
                    or (event.key == K_LEFT)
                    or (event.key == K_UP)
                    or (event.key == K_DOWN)):
                        self.bird.move(event.key)

            """Check for collision between bird and obstacle"""
            lstCols = pygame.sprite.spritecollide(self.bird,self.obstacle_sprites,True)

            """Create an ending page with the option to play again or quit the game"""
            def play_again():
                bigfont = pygame.font.Font(None, 80)
                smallfont = pygame.font.Font(None, 45)
                text = bigfont.render("Play again?", 13, (0,0,0))
                textx = 175
                texty = 50
                text2 = smallfont.render("Yes [Y]  |  No [N]", 13, (0,0,0))
                textx2 = 200
                texty2 = 150

                self.screen.blit(self.background, (0, 0))
                self.screen.blit(text, (textx, texty))
                self.screen.blit(text2, (textx2, texty2))
                pygame.display.flip()

            """If a collision happens, go to the play again page, and register key input. If Y, restart game. If N, quit game."""
            if lstCols:
                play_again()
                while 1:
                    for event in pygame.event.get():
                        if event.type == KEYDOWN:
                            if event.key == K_y:
                                pygame.quit()
                                MainWindow = PyManMain()
                                MainWindow.MainLoop()
                            elif event.key == K_n:
                                pygame.quit()

            """Create game environment by setting the background, adding the bird, and placing the obstacles."""
            self.screen.blit(self.background, (0, 0))
            self.obstacle_sprites.draw(self.screen)
            self.bird_sprites.draw(self.screen)
            pygame.display.flip()

    def LoadSprites(self):
        """Load the sprites that we need"""
        self.bird = Bird()
        self.bird_sprites = pygame.sprite.RenderPlain((self.bird))

        """figure out how many obstacles we can display"""
        nNumHorizontal = int(self.width/64)
        nNumVertical = int(self.height/64)
        """Create the obstacle group"""
        self.obstacle_sprites = pygame.sprite.Group()
        """Create all of the obstacles and add them to the
        obstacle_sprites group -- randomize placement of obstacles"""
        for x in range(nNumHorizontal):
            if x!=0:
                if x!=2:
                    if x!=4:
                        if x!=6:
                            if x!=8:
                                for y in range(nNumVertical):
                                        if y!=random.randint(1,6):
                                                    self.obstacle_sprites.add(obstacle(pygame.Rect(x*64, y*64, 64, 64)))

class Bird(pygame.sprite.Sprite):
    """This is our sprite that will move around the screen.
    Use picture provided.
    Define movement according to keystrokes.
    """

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('bird.png',-1)
        self.obstacles = 0
        """Set the number of Pixels to move each time"""
        self.x_dist = 5
        self.y_dist = 5

    def move(self, key):
        """Move your self in one of the 4 directions according to key"""
        """Key is the pyGame define for either up,down,left, or right key
        we will adjust outselfs in that direction"""
        xMove = 0;
        yMove = 0;

        if (key == K_RIGHT):
            xMove = self.x_dist
        elif (key == K_LEFT):
            xMove = -self.x_dist
        elif (key == K_UP):
            yMove = -self.y_dist
        elif (key == K_DOWN):
            yMove = self.y_dist
        #self.rect = self.rect.move(xMove,yMove);
        self.rect.move_ip(xMove,yMove);

class obstacle(pygame.sprite.Sprite):
    """Create the obstacles of the game.
    Use picture provided. Define rectangle according to the image.
    """
    def __init__(self, rect=None):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('obstacle.png')
        if rect != None:
            self.rect = rect

if __name__ == "__main__":
    MainWindow = PyManMain()
    MainWindow.MainLoop()
