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
        """Initialize"""
        """Initialize PyGame"""
        pygame.init()
        """Set the window Size"""
        self.width = width
        self.height = height
        """Create the Screen"""
        self.screen = pygame.display.set_mode((self.width
                                               , self.height))

    def MainLoop(self):
        """This is the Main Loop of the Game"""

        """Load All of our Sprites"""
        self.LoadSprites();
        """tell pygame to keep sending up keystrokes when they are
        held down"""
        pygame.key.set_repeat(500, 30)

        """Create the background"""
        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill((101,243,149))

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

            """Check for collision"""
            lstCols = pygame.sprite.spritecollide(self.bird
                                                 , self.obstacle_sprites
                                                 , True)

            """Create Restarter for if you lose"""
            def restarter():
                pygame.font.init()
                background_colour = (00,00,00)
                (width, height) = (600, 600)

                screen = pygame.display.set_mode((width, height))
                pygame.display.set_caption('You Lose. Restarting....')
                screen.fill(background_colour)

                pygame.display.flip()



            """Restart the game if loss is achieved"""
            if lstCols:
                restarter()
                time.sleep(3)
                pygame.quit()
                MainWindow = PyManMain()
                MainWindow.MainLoop()



            """Do the Instructions"""
            self.screen.blit(self.background, (0, 0))
            if pygame.font:
                font = pygame.font.Font(None, 36)
                text = font.render("Don't hit any obstacles %s" % ""
                                    , 1, (255, 0, 0))
                text2 = font.render("Stay in as long as possible %s" % ""
                                    , 1, (255, 0, 0))
                textpos = text.get_rect(centery=self.background.get_width()/2)
                textpos2 = text.get_rect(centerx=self.background.get_width()/2)


                self.screen.blit(text, textpos)
                self.screen.blit(text2, textpos2)

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
        obstacle_sprites group"""
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
    """This is our sprite that will move around the screen"""

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

    def __init__(self, rect=None):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('obstacle.png',-1)
        if rect != None:
            self.rect = rect

if __name__ == "__main__":
    MainWindow = PyManMain()
    MainWindow.MainLoop()
