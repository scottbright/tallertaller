import pygame
from pygame.locals import *

class Player(object):

    def __init__(self,Path,posX,posY):
        self.posX = posX
        self.posY = posY
        self.Zumo = pygame.image.load(Path)
        self.count = 0
    def update(self):
        pass
       
    def render(self, surface):
        surface.blit(self.Zumo,(self.posX,self.posY))
#########################################

